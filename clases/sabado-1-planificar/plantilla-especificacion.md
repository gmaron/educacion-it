# Especificación: divisor de gastos

**Nombre:** _______________

## 1. Qué hace
En una frase, en lenguaje común.

> Dice cuánto le toca poner a cada persona después de una salida y quién le tiene que transferir a quién para quedar a mano.

*(Podés usar esta frase o escribir la tuya.)*

## 2. Qué recibe
¿Qué datos hay que cargar? ¿En qué formato?

- Nombre de cada persona: _______________
- Cuánto puso cada una: _______________
- Otro dato que haga falta: _______________

## 3. Qué devuelve
¿Qué muestra el programa al terminar? ¿Cómo lo muestra?

- _______________

## 4. Casos con número esperado
Cada caso tiene una entrada concreta y un resultado concreto. Otra persona tiene que poder calcular el mismo número sin preguntarte nada.

| # | Entrada | Resultado esperado |
| --- | --- | --- |
| 1 | Ana pagó $2000 y Beto, $0 | Cada uno pone $1000. Beto le transfiere $1000 a Ana |
| 2 | | |
| 3 | | |
| 4 | | |
| 5 | | |

**Caso borde que la IA no consideró:** _______________

Algunas pistas para buscar casos borde:
- ¿Qué pasa si la cuenta no divide justo?
- ¿Y si alguien no puso nada? ¿Y si todos pusieron lo mismo?
- ¿Y si cargan un monto que no tiene sentido?
- ¿Y si hay una sola persona?

## 5. Decisiones
Lo que elegiste vos, con su motivo. Si no lo decidís, lo decide la IA.

| Decisión | Motivo |
| --- | --- |
| | |

## Extensión (si ya programás)
**Simplificación de deudas.** Si Ana le debe a Beto y Beto le debe a Caro, ¿cuántas transferencias hacen falta como mínimo? Agregá un caso con varias deudas cruzadas y su resultado esperado. Decidí también:
- **Formato de entrada:** archivo CSV o datos que tipea el usuario.
- **Primera versión:** programa de terminal o Streamlit.

Justificá las dos decisiones.

## Checklist antes de entregar
- [ ] Al menos 5 casos, cada uno con un número esperado.
- [ ] Al menos 1 caso borde que la IA no consideró.
- [ ] Al menos 1 decisión con su motivo.
- [ ] Otra persona calculó 2 casos sin preguntarte nada y llegó al mismo número (en el chat de la clase o en un comentario de tu PR).
