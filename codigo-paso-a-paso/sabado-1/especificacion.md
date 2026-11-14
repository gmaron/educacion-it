# Especificación: divisor de gastos

**Nombre:** gmaron

## 1. Qué hace
Dice cuánto le toca poner a cada persona después de una salida y quién le tiene que transferir a quién para quedar a mano.

## 2. Qué recibe
- Nombre de cada persona: texto de al menos 3 caracteres. Puede haber nombres repetidos.
- Cuánto puso cada una: un monto en pesos, mayor o igual a $0. El $0 es lo que pone quien no pagó nada.
- Otro dato que haga falta: ninguno. La cuenta se divide en partes iguales entre todos los que se cargan.

## 3. Qué devuelve
- La lista de transferencias: quién paga, a quién le paga y cuánto, en pesos enteros.
- Si la lista queda vacía, la pantalla muestra **"Están a mano"**.
- Antes de las transferencias, la pantalla muestra las cuentas: el total, cuánto le toca a cada uno, cuánto puso y cuánto debe o le devuelven a cada persona, el redondeo y a quién va el sobrante. Así cualquiera puede verificar lo que le toca pagar.
- Si un monto es negativo o un nombre tiene menos de 3 caracteres, el programa no calcula nada y muestra un error.
- En la pantalla, los que deben aparecen en rojo y los que pagaron de más, en verde. Los colores son cosa de la pantalla, no del cálculo.

## 4. Casos con número esperado

| # | Entrada | Resultado esperado |
| --- | --- | --- |
| 1 | Ana pagó $2000 y Beto, $0 | Cada uno pone $1000. Beto le transfiere $1000 a Ana |
| 2 | Ana pagó $1001 y Beto, $0 | A cada uno le toca $500,50. Beto le transfiere $501 a Ana |
| 3 | Ana pagó $1000, Beto $0 y Caro $0 | A cada uno le toca $333,33. Beto le transfiere $334 a Ana y Caro le transfiere $334 a Ana |
| 4 | Ana pagó $600, Beto $400 y Caro $0 | A cada uno le toca $333,33. Caro le transfiere $267 a Ana y $67 a Beto |
| 5 | Ana pagó $601, Beto $400, Caro $0 y Dani $0 | A cada uno le toca $250,25. Caro le transfiere $251 a Ana. Dani le transfiere $101 a Ana y $150 a Beto |
| 6 | Ana pagó $1000 y no hay nadie más | "Están a mano" |
| 7 | Ana $0, Beto $0 y Caro $0 | "Están a mano" |
| 8 | Ana pagó $500 y Beto, $500 | "Están a mano" |
| 9 | Ana pagó $1000 y Beto, −$500 | Error: no se aceptan montos negativos |
| 10 | Al pagó $1000 y Beto, $0 | Error: el nombre tiene que tener al menos 3 caracteres |
| 11 | Ana pagó $1000 y otra Ana, $0 | En pantalla: "Ana (2) le transfiere $500 a Ana (1)". Por atrás, cada Ana tiene su propio alias y se calculan como dos personas distintas |

**Caso borde que la IA no consideró:** nombres repetidos (caso 11). Por atrás cada uno tiene un alias distinto, así que la plata no se mezcla. En la pantalla se numeran según el orden en que se cargaron, para saber quién es quién. También los nombres de menos de 3 caracteres (caso 10).

## 5. Decisiones

| Decisión | Motivo |
| --- | --- |
| Quien debe redondea siempre para arriba, al peso entero | El que pagó hizo los mandados, así que el redondeo queda a su favor |
| Cada uno de los que pagaron recibe su crédito redondeado para arriba. Si entra más de lo que se reparte, el sobrante va al que más puso | El que puso más, recibe más |
| El que más debe le paga primero al que más puso. Si hay empate, se ordena alfabéticamente | Porque deben plata |
| Se aceptan montos mayores o iguales a $0. Los negativos dan error | El $0 es el punto de partida de cada uno |
| Los nombres tienen al menos 3 caracteres. Los repetidos se distinguen con un alias interno | Para que dos personas con el mismo nombre no se confundan en la cuenta |
| En la pantalla, los nombres repetidos llevan un número según el orden de carga: "Ana (1)", "Ana (2)". Los que no se repiten van sin número | Si no, "Ana le transfiere a Ana" no dice cuál le paga a cuál |
| Si nadie le debe a nadie, se muestra "Están a mano" | Vale igual para una sola persona, para todos en $0 y para todos con el mismo monto |

## Checklist antes de entregar
- [x] Al menos 5 casos, cada uno con un número esperado.
- [x] Al menos 1 caso borde que la IA no consideró.
- [x] Al menos 1 decisión con su motivo.
- [ ] Otra persona calculó 2 casos sin preguntarte nada y llegó al mismo número (en el chat de la clase o en un comentario de tu PR).
