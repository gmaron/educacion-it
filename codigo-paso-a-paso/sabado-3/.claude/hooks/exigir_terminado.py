"""Hook Stop: no deja terminar si fallan los tests o ruff da avisos.

Corre pytest y ruff check desde la carpeta del proyecto. Si alguno falla,
devuelve {"decision": "block", "reason": ...} con la salida, y Claude
sigue trabajando. Cuando stop_hook_active es verdadero, Claude ya está
reintentando por este mismo hook: cuenta los intentos en un archivo y, a
partir del tercero, lo deja terminar con un aviso para no quedar en bucle.
"""

import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

VENV = Path("../../.venv/bin")
COMANDOS = [
    [str(VENV / "python"), "-m", "pytest", "-q"],
    [str(VENV / "ruff"), "check", "."],
]
MAX_INTENTOS = 3
MAX_SALIDA = 4000


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
    datos = json.load(sys.stdin)
    carpeta = os.environ.get("CLAUDE_PROJECT_DIR") or datos.get("cwd", ".")
    contador = archivo_intentos(datos.get("session_id", "sin-sesion"))

    fallas = []
    for comando in COMANDOS:
        codigo, salida = correr(carpeta, comando)
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
                "o ruff fallando. La historia no está terminada según el "
                "CLAUDE.md."
            ),
        }))
        return 0

    contador.write_text(str(intentos))
    print(json.dumps({
        "decision": "block",
        "reason": (
            "No está terminado: según el CLAUDE.md tienen que pasar todos "
            "los tests y ruff check no puede dar avisos. Arreglalo o, si "
            "no corresponde tocarlo (por ejemplo, un test commiteado), "
            f"avisale al usuario. Intento {intentos} de {MAX_INTENTOS}.\n\n"
            + "\n\n".join(fallas)
        ),
    }))
    return 0


if __name__ == "__main__":
    sys.exit(main())
