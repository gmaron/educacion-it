"""Hook PreToolUse: no deja tocar un archivo de tests ya commiteado.

Claude Code le pasa por stdin un JSON con la herramienta que quiere usar
y sus argumentos.

- Con Edit, Write o MultiEdit: si el archivo es un ``test_*.py`` que
  está en git y no tiene cambios, el commit es la aprobación. El hook
  sale con código 2 y el mensaje de stderr le llega al agente. Un test
  nuevo, o uno con cambios sin commitear, se puede editar.
- Con Bash: cualquier comando que mencione ``test_`` o ``tests`` se
  bloquea, salvo las dos invocaciones exactas de ``PERMITIDOS``. Buscar
  comandos peligrosos no alcanza (``sed -i``, ``python -c``, ``perl``,
  ``ruff check --fix``...), así que el hook falla del lado seguro. Para
  leer un test, el agente usa su herramienta Read, que no pasa por acá.

Es una barrera para el agente, no un sistema de seguridad: un comando
con comodines (``src/te*/*``) o un script que cambie los tests sin
nombrarlos la pasan. Lo que avisa siempre es git.
"""

import json
import re
import subprocess
import sys
from pathlib import Path

PERMITIDOS = {
    "../../.venv/bin/python -m pytest -q",
    "../../.venv/bin/ruff check .",
}

MENSAJE = (
    "es un test aprobado (está commiteado) y no se toca, tampoco desde la "
    "terminal. Si creés que el test está mal, avisale a la persona y no lo "
    "cambies. Los tests nuevos van en un archivo nuevo. Para correr los "
    "tests usá exactamente `../../.venv/bin/python -m pytest -q`."
)


def esta_aprobado(archivo: Path) -> bool:
    """Dice si el archivo está commiteado y sin cambios.

    Args:
        archivo: ruta absoluta al archivo que el agente quiere tocar.

    Returns:
        True si git lo conoce y no tiene cambios contra HEAD.
    """
    if not archivo.exists():
        return False
    carpeta = archivo.parent
    conocido = subprocess.run(
        ["git", "ls-files", "--error-unmatch", archivo.name],
        cwd=carpeta,
        capture_output=True,
    )
    if conocido.returncode != 0:
        return False
    sin_cambios = subprocess.run(
        ["git", "diff", "--quiet", "HEAD", "--", archivo.name],
        cwd=carpeta,
    )
    return sin_cambios.returncode == 0


def bash_toca_tests(comando: str) -> bool:
    """Dice si un comando de Bash menciona los tests y no está permitido."""
    if comando.strip() in PERMITIDOS:
        return False
    # Sin comillas ni barras y en minúsculas, para que t''est_ o TEST_
    # no se escapen. --fix reescribe archivos aunque no los nombre.
    normal = re.sub(r"[\"'\\]", "", comando).casefold()
    return any(m in normal for m in ("test_", "tests", "--fix"))


def main() -> int:
    """Lee el pedido del agente y decide si lo deja pasar.

    Returns:
        0 si lo deja pasar, 2 si lo bloquea.
    """
    pedido = json.load(sys.stdin)
    entrada = pedido.get("tool_input", {})

    if pedido.get("tool_name") == "Bash":
        if bash_toca_tests(entrada.get("command", "")):
            print(f"El comando menciona los tests: {MENSAJE}", file=sys.stderr)
            return 2
        return 0

    ruta = entrada.get("file_path", "")
    if not ruta:
        return 0
    archivo = Path(ruta)
    if not archivo.is_absolute():
        archivo = Path(pedido.get("cwd", ".")) / archivo
    archivo = archivo.resolve()
    nombre = archivo.name.casefold()
    es_test = nombre.startswith("test_") and nombre.endswith(".py")
    if es_test and esta_aprobado(archivo):
        print(f"{archivo.name} {MENSAJE}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
