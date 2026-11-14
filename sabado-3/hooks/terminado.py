"""Hook Stop: el agente no termina si fallan los tests o ruff da avisos.

Es la definición de terminado del CLAUDE.md, corrida de verdad. Si algo
falla, devuelve ``{"decision": "block", "reason": ...}`` y el agente
sigue trabajando: eso es el loop. Para no dar vueltas sin fin, cuenta
los intentos de la sesión y, a partir del tercero, lo deja terminar con
un aviso.
"""

import json
import subprocess
import sys
import tempfile
from pathlib import Path

TOPE = 3


def correr(comando: list[str], carpeta: str) -> tuple[bool, str]:
    """Corre un comando y devuelve si salió bien y las últimas líneas.

    Args:
        comando: el comando y sus argumentos.
        carpeta: dónde correrlo.

    Returns:
        (True si salió con código 0, últimas 30 líneas de la salida).
    """
    resultado = subprocess.run(
        comando, cwd=carpeta, capture_output=True, text=True
    )
    salida = (resultado.stdout + resultado.stderr).strip().splitlines()
    return resultado.returncode == 0, "\n".join(salida[-30:])


def main() -> int:
    """Comprueba la definición de terminado y decide si el agente termina.

    Returns:
        Siempre 0: la decisión va en el JSON de stdout.
    """
    pedido = json.load(sys.stdin)
    carpeta = pedido.get("cwd", ".")
    sesion = pedido.get("session_id", "sin-sesion")
    contador = Path(tempfile.gettempdir()) / f"claude-stop-{sesion}.txt"

    tests_ok, tests = correr(
        [sys.executable, "-m", "pytest", "-q"], carpeta
    )
    ruff_ok, ruff = correr(
        [sys.executable, "-m", "ruff", "check", "--output-format=concise"],
        carpeta,
    )

    if tests_ok and ruff_ok:
        contador.unlink(missing_ok=True)
        return 0

    intentos = 0
    if pedido.get("stop_hook_active") and contador.exists():
        intentos = int(contador.read_text() or 0)
    intentos += 1
    contador.write_text(str(intentos))

    if intentos > TOPE:
        contador.unlink(missing_ok=True)
        aviso = {
            "systemMessage": (
                f"El loop llegó al tope de {TOPE} intentos y todavía no "
                "pasan los tests o ruff. Revisalo vos."
            ),
        }
        print(json.dumps(aviso, ensure_ascii=False))
        return 0

    problemas = []
    if not tests_ok:
        problemas.append("Fallan los tests:\n" + tests)
    if not ruff_ok:
        problemas.append("ruff da avisos:\n" + ruff)
    bloqueo = {
        "decision": "block",
        "reason": (
            f"Todavía no terminaste (intento {intentos} de {TOPE}). "
            "Arreglá el código, no los tests.\n\n" + "\n\n".join(problemas)
        ),
    }
    print(json.dumps(bloqueo, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
