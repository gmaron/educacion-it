# Plan: divisor de gastos

Lo propuso el agente en plan mode a partir de `especificacion.md` y lo aprobé con los cambios marcados [DECIDÍ].

## Estructura

Un solo módulo, `src/divisor_gastos.py`. La interfaz pública son tres funciones; el resto es privado (`_`).

| Función | Firma | Requisitos |
|---|---|---|
| `dividir` | `dividir(pagos: list[Pago]) -> list[Transferencia]` | R1, R4 |
| `mostrar` | `mostrar(pagos: list[Pago]) -> str` | R1, R2, R4 |
| `explicar` | `explicar(pagos: list[Pago]) -> str` | R3 |
| `leer_monto` | `leer_monto(texto: str) -> Decimal` | R6 |

`Pago` es `tuple[str, float]`: nombre y monto. `Transferencia` es una `NamedTuple` con quién paga, a quién y cuánto.

## Decisiones por requisito

- **R1. Transferencias en pesos enteros.** Deudas y créditos se redondean para arriba. El sobrante del redondeo va al que más puso. El que más debe le paga primero al que más puso; los empates, por nombre y después por orden de carga.
  - [DECIDÍ] El agente propuso `float`. Lo cambié a `Decimal`: con `float`, $1001 / 2 puede dar $500,4999… y el redondeo para arriba falla en el borde.
- **R2. "Están a mano".** `dividir` devuelve una lista vacía y `mostrar` la traduce al mensaje. No hay un caso especial para una sola persona: sale solo.
- **R3. Las cuentas a la vista.** `explicar` arma el texto paso a paso y termina con lo que devuelve `mostrar`, para que las transferencias se calculen en un solo lugar.
- **R4. Errores.** Se valida todo antes de calcular y se lanza `ValueError` con el mensaje de la especificación. `mostrar` y `explicar` lo atrapan y devuelven `"Error: …"`.
  - [DECIDÍ] El agente propuso un diccionario `nombre → monto`. Lo cambié a una lista de personas con un alias (su posición): con un diccionario, dos Ana se pisan (C11).
- **R5. Colores.** Sin caso con resultado esperado. No se planifica hasta que la especificación tenga uno.
- **R6. Montos con coma.** `leer_monto` reemplaza la coma por punto y convierte a `Decimal`. Si no puede, lanza `ValueError("el monto tiene que ser un número")`. La usa `_leer_pagos`, que hoy hace `float(monto)` y se cae con `1500,50`.
  - [DECIDÍ] Sin separador de miles, como dice la especificación. No se intenta adivinar si `1.500` es mil quinientos.

## Tests

Un test por caso, con el número del caso en el nombre: `test_12_...`. Los tests no se cambian para que pasen.
