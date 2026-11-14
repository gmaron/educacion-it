"""Hook Stop: no deja terminar si fallan los tests o ruff da avisos.

Corre pytest y ruff check desde la carpeta del proyecto. Si alguno falla,
devuelve {"decision": "block", "reason": ...} con la salida, y Claude
sigue trabajando. Cuando stop_hook_active es verdadero, Claude ya está
reintentando por este mismo hook: cuenta los intentos en un archivo y, a
partir del tercero, lo deja terminar con un aviso para no quedar en bucle.

No supone nada del proyecto: busca un .venv (o venv) subiendo desde la
carpeta del proyecto y, si no hay, usa python3 y ruff del PATH. Si pytest
no está instalado o no hay tests, saltea pytest; si no hay ruff, saltea
ruff. Si no queda nada para comprobar, deja terminar.
"""

import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

VENVS = (".venv", "venv")
MAX_INTENTOS = 3
MAX_SALIDA = 4000
TIEMPO_MAXIMO = 100
SIN_TESTS = 5  # Código de pytest cuando no encuentra ningún test.


def buscar(carpeta, programa):
    """Busca el programa en un venv de la carpeta o sus padres, o en PATH."""
    for actual in (carpeta, *carpeta.parents):
        for venv in VENVS:
            candidato = actual / venv / "bin" / programa
            if candidato.is_file() and os.access(candidato, os.X_OK):
                return str(candidato)
    return shutil.which(programa)


def correr(carpeta, comando):
    """Corre el comando en la carpeta y devuelve (código, salida)."""
    try:
        resultado = subprocess.run(
            comando,
            cwd=carpeta,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            timeout=TIEMPO_MAXIMO,
        )
    except subprocess.TimeoutExpired:
        return 1, f"Se cortó a los {TIEMPO_MAXIMO} segundos."
    salida = resultado.stdout
    if len(salida) > MAX_SALIDA:
        salida = "[...]\n" + salida[-MAX_SALIDA:]
    return resultado.returncode, salida


def tiene_pytest(carpeta, python):
    """Indica si ese python puede importar pytest."""
    codigo, _ = correr(carpeta, [python, "-c", "import pytest"])
    return codigo == 0


def comprobaciones(carpeta):
    """Devuelve los comandos que se pueden correr en esta carpeta."""
    comandos = []
    python = buscar(carpeta, "python") or buscar(carpeta, "python3")
    if python and tiene_pytest(carpeta, python):
        comandos.append([python, "-m", "pytest", "-q"])
    ruff = buscar(carpeta, "ruff")
    if ruff:
        comandos.append([ruff, "check", "."])
    return comandos


def archivo_intentos(sesion):
    """Devuelve la ruta del contador de intentos de esta sesión."""
    return Path(tempfile.gettempdir()) / f"claude-stop-intentos-{sesion}"


def leer_intentos(ruta):
    """Lee el contador; si no existe o está roto, devuelve 0."""
    try:
        return int(ruta.read_text())
    except (OSError, ValueError):
        return 0


def main():
    """Decide si Claude puede terminar."""
    try:
        datos = json.load(sys.stdin)
    except ValueError:
        datos = {}
    carpeta = os.environ.get("CLAUDE_PROJECT_DIR") or datos.get("cwd", ".")
    carpeta = Path(carpeta).resolve()
    contador = archivo_intentos(datos.get("session_id", "sin-sesion"))

    fallas = []
    for comando in comprobaciones(carpeta):
        codigo, salida = correr(carpeta, comando)
        if comando[-1] == "-q" and codigo == SIN_TESTS:
            continue
        if codigo != 0:
            fallas.append(f"$ {' '.join(comando)}\n{salida}")

    if not fallas:
        contador.unlink(missing_ok=True)
        return 0

    intentos = 1
    if datos.get("stop_hook_active"):
        intentos = leer_intentos(contador) + 1
    if intentos >= MAX_INTENTOS:
        contador.unlink(missing_ok=True)
        print(json.dumps({
            "systemMessage": (
                f"Aviso: Claude terminó tras {intentos} intentos con tests "
                "o ruff fallando. El trabajo no está terminado."
            ),
        }))
        return 0

    contador.write_text(str(intentos))
    print(json.dumps({
        "decision": "block",
        "reason": (
            "No está terminado: tienen que pasar todos los tests y ruff "
            "check no puede dar avisos. Arreglalo o, si no corresponde "
            "tocarlo (por ejemplo, un test commiteado), avisale al usuario. "
            f"Intento {intentos} de {MAX_INTENTOS}.\n\n"
            + "\n\n".join(fallas)
        ),
    }))
    return 0


if __name__ == "__main__":
    sys.exit(main())
