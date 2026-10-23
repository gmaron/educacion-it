"""Los casos de tu especificación, convertidos en tests.

Cada fila de la tabla "Casos con número esperado" es un test.
El primero es el caso de ejemplo de la plantilla. Agregá los tuyos abajo.
"""

from divisor import dividir


def test_dos_personas_una_pago_todo():
    # Caso 1 de la plantilla: Ana pagó $2000 y Beto, $0.
    # Cada uno pone $1000. Beto le transfiere $1000 a Ana.
    assert dividir({"Ana": 2000, "Beto": 0}) == [("Beto", "Ana", 1000)]


# def test_tu_caso():
#     # Entrada: ...
#     # Resultado esperado: ...
#     assert dividir({...}) == [...]
