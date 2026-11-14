"""Hook PreToolUse: bloquea editar un test_*.py que ya está commiteado.

Lee el JSON del hook por stdin y mira tool_input.file_path. Si el archivo
es un test_*.py versionado en git y sin cambios respecto de HEAD, sale con
código 2: Claude Code cancela la herramienta y le muestra el motivo.
"""

import json
import subprocess
import sys
from pathlib import Path


def git(carpeta, *args):
    """Corre git en la carpeta dada y devuelve el código de salida."""
    return subprocess.run(
        ["git", "-C", str(carpeta), *args],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    ).returncode


def esta_commiteado_sin_cambios(ruta):
    """Indica si el archivo está en git y no difiere de HEAD."""
    carpeta = ruta.parent if ruta.parent.exists() else Path.cwd()
    if git(carpeta, "ls-files", "--error-unmatch", "--", str(ruta)) != 0:
        return False
    return git(carpeta, "diff", "--quiet", "HEAD", "--", str(ruta)) == 0


def main():
    """Decide si se permite la edición."""
    datos = json.load(sys.stdin)
    file_path = datos.get("tool_input", {}).get("file_path", "")
    ruta = Path(file_path)
    if not (ruta.name.startswith("test_") and ruta.suffix == ".py"):
        return 0
    if not ruta.is_absolute():
        ruta = Path(datos.get("cwd", ".")) / ruta
    if esta_commiteado_sin_cambios(ruta):
        print(
            f"Bloqueado: {file_path} es un test ya commiteado. El commit es "
            "la aprobación del usuario y los tests existentes no se tocan. "
            "Escribí el test nuevo en un archivo nuevo de src/tests/ o, si "
            "creés que este test está mal, avisale al usuario.",
            file=sys.stderr,
        )
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
