"""Divisor de gastos: quién le debe a quién después de una salida.

Esta función la escribís vos, con ayuda de la IA, a partir de tu especificación.
Antes de pedirle el código, fijate que tu especificación responda lo mismo que esta firma:

- "Qué recibe" (sección 2) son los parámetros.
- "Qué devuelve" (sección 3) es el valor de salida.
- Cada caso con número esperado (sección 4) es un test en tests/test_divisor.py.
"""

Transferencia = tuple[str, str, float]
"""(quién paga, a quién le paga, cuánto)."""


def dividir(pagos: dict[str, float]) -> list[Transferencia]:
    """Recibe cuánto puso cada persona y devuelve las transferencias para quedar a mano.

    Ejemplo: {"Ana": 2000, "Beto": 0} -> [("Beto", "Ana", 1000)]

    Decisiones que tu especificación tiene que tomar antes de escribir esto:
    - ¿Qué pasa con los centavos que sobran?
    - ¿Qué pasa con un monto negativo o un nombre repetido?
    - ¿En qué orden se devuelven las transferencias?
    - ¿float alcanza para plata, o conviene Decimal?
    """
    raise NotImplementedError("Escribí esta función a partir de tu especificación.")
