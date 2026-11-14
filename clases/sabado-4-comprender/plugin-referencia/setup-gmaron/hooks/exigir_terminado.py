"""Hook Stop: no deja terminar si fallan los tests o ruff da avisos.

Versión para llevar a cualquier proyecto (la del sábado 3 suponía
../../.venv y un proyecto con tests). Busca un .venv subiendo desde la
carpeta del proyecto; si no hay, usa el Python y el ruff del sistema.
Si el proyecto no tiene tests, no corre pytest; si no hay ruff, no corre
ruff. Con nada que comprobar, deja terminar.

Si algo falla, devuelve {"decision": "block", "reason": ...} con la
salida, y Claude sigue trabajando. Cuando stop_hook_active es verdadero,
cuenta los intentos y, a partir del tercero, lo deja terminar con un
aviso para no quedar en bucle.
"""

import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

MAX_INTENTOS = 3
MAX_SALIDA = 4000
IGNORAR = {".venv", "venv", "node_modules", ".git"}


def buscar_venv(carpeta):
    """Devuelve la carpeta bin del primer .venv subiendo desde carpeta."""
    for actual in [carpeta, *carpeta.parents]:
        for nombre in ("bin", "Scripts"):
            candidato = actual / ".venv" / nombre
            if candidato.is_dir():
                return candidato
    return None


def tiene_tests(carpeta):
    """Indica si hay algún test_*.py fuera de las carpetas ignoradas."""
    for ruta in carpeta.rglob("test_*.py"):
        if not IGNORAR.intersection(ruta.parts):
            return True
    return False


def tiene_pytest(python):
    """Indica si ese Python tiene pytest instalado."""
    resultado = subprocess.run(
        [python, "-c", "import pytest"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return resultado.returncode == 0


def armar_comandos(carpeta, avisos):
    """Arma la lista de comandos que se pueden correr en este proyecto.

    Lo que no se puede comprobar (hay tests pero no hay pytest) no
    bloquea: se agrega a avisos para mostrárselo al usuario.
    """
    venv = buscar_venv(carpeta)
    python = sys.executable
    ruff = shutil.which("ruff")
    if venv:
        for nombre in ("python", "python.exe"):
            if (venv / nombre).exists():
                python = str(venv / nombre)
        for nombre in ("ruff", "ruff.exe"):
            if (venv / nombre).exists():
                ruff = str(venv / nombre)
    comandos = []
    if tiene_tests(carpeta):
        if tiene_pytest(python):
            comandos.append([python, "-m", "pytest", "-q"])
        else:
            avisos.append(
                f"Hay tests pero {python} no tiene pytest: no se "
                "comprobaron. Creá un .venv con pytest en el proyecto."
            )
    if ruff:
        comandos.append([ruff, "check", "."])
    return comandos


def correr(carpeta, comando):
    """Corre el comando en la carpeta y devuelve (código, salida)."""
    resultado = subprocess.run(
        comando,
        cwd=carpeta,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )
    salida = resultado.stdout
    if len(salida) > MAX_SALIDA:
        salida = "[...]\n" + salida[-MAX_SALIDA:]
    return resultado.returncode, salida


def archivo_intentos(sesion):
    """Devuelve la ruta del contador de intentos de esta sesión.

    Lleva el nombre del plugin para no pisarse con el contador del Stop
    del proyecto, si los dos están activos en la misma sesión.
    """
    nombre = f"claude-stop-intentos-setup-gmaron-{sesion}"
    return Path(tempfile.gettempdir()) / nombre


def leer_intentos(ruta):
    """Lee el contador; si no existe o está roto, devuelve 0."""
    try:
        return int(ruta.read_text())
    except (OSError, ValueError):
        return 0


def main():
    """Decide si Claude puede terminar."""
    datos = json.load(sys.stdin)
    carpeta = Path(
        os.environ.get("CLAUDE_PROJECT_DIR") or datos.get("cwd", ".")
    )
    contador = archivo_intentos(datos.get("session_id", "sin-sesion"))

    avisos = []
    fallas = []
    for comando in armar_comandos(carpeta, avisos):
        codigo, salida = correr(carpeta, comando)
        if codigo != 0:
            fallas.append(f"$ {' '.join(comando)}\n{salida}")

    if not fallas:
        contador.unlink(missing_ok=True)
        if avisos:
            print(json.dumps({"systemMessage": "Aviso: " + " ".join(avisos)}))
        return 0

    intentos = 1
    if datos.get("stop_hook_active"):
        intentos = leer_intentos(contador) + 1
    if intentos >= MAX_INTENTOS:
        contador.unlink(missing_ok=True)
        print(json.dumps({
            "systemMessage": (
                f"Aviso: Claude terminó tras {intentos} intentos con tests "
                "o ruff fallando. No está terminado."
            ),
        }))
        return 0

    contador.write_text(str(intentos))
    print(json.dumps({
        "decision": "block",
        "reason": (
            "No está terminado: tienen que pasar todos los tests y ruff "
            "check no puede dar avisos. Arreglalo o, si no corresponde "
            "tocarlo (por ejemplo, un test commiteado), avisale al "
            f"usuario. Intento {intentos} de {MAX_INTENTOS}.\n\n"
            + "\n\n".join(fallas)
        ),
    }))
    return 0


if __name__ == "__main__":
    sys.exit(main())
