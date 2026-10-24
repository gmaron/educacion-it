# Sábado 1 · Planificar

**Pedile a la IA algo que puedas verificar.** Sábado 24/10/2026, de 10:00 a 13:00 (hora de Argentina).

Hoy trabajamos la primera parte del criterio: **escribir una especificación que se pueda verificar**. El sábado que viene, un agente va a programar a partir de ella.

Todas las prácticas son individuales. Tu compañera de trabajo es la IA, y los demás están en el chat.

## Práctica 1 · Un pomodoro en 15 minutos

1. Abrí Claude.ai o Gemini.
2. Escribí solo esto: **Haceme un pomodoro**
3. Cuando aparezca, probalo.

Después lo conversamos: ¿qué decidió la IA por vos?

**Para ir más lejos:** compará el tuyo con [`pomodoro/index.html`](pomodoro/index.html) y pedile a la IA que te explique el código con el nivel 1 de [`explicar-codigo.md`](explicar-codigo.md).

## Práctica 2 · La especificación del divisor de gastos (25 minutos)

Con la [plantilla](plantilla-especificacion.md), escribí la especificación de un programa que diga quién le debe a quién después de un asado. Para ver cómo es una especificación bien hecha, mirá el [ejemplo del pomodoro](ejemplo-especificacion-pomodoro.md).

1. Empezá por el caso más simple: dos personas.
2. Después, buscá los casos donde el programa se rompe.

**Lo que tenés que entregar:**
- Al menos 5 casos, cada uno con un número esperado.
- Al menos 1 caso borde que la IA no haya considerado.
- Al menos 1 decisión propia, con su motivo.

### La IA como entrevistadora

Si te quedás sin ideas, que la IA te haga las preguntas:

```
Tarea: entrevistame como analista para encontrar los casos borde de una app que divide gastos entre amigos.

Instrucciones: hacé una pregunta por vez. No escribas código. Al final, listá los casos que surgieron en una tabla con entrada y resultado esperado, y marcá con [DUDA] los que dependan de una decisión mía.

Contexto: es para un asado entre amigos; cada uno puso una cantidad distinta y algunos no pusieron nada.
```

**Ojo:** cada número que proponga la IA, calculalo a mano. Con el redondeo suele equivocarse.

## Práctica 3 · ¿Le da el número? (20 minutos)

1. Pegale la especificación completa a la IA y pedile el código.
2. Elegí 2 casos de tu tabla y compará el resultado con el número esperado.

**Si clonaste el repo:** pedí que el código respete la firma de [`divisor/divisor.py`](../divisor/divisor.py), pegalo ahí, pasá tus casos a [`divisor/tests/test_divisor.py`](../divisor/tests/test_divisor.py) y corré `pytest`. Después pedile a la IA que te explique la función con el nivel 2 de [`explicar-codigo.md`](explicar-codigo.md).

## Cierre · ¿Se entiende sin vos?

Pegá en el chat la **entrada** de uno de tus casos, sin el resultado. Los demás lo calculan y responden con su número.
- **Si todos llegan al mismo número,** el caso está claro.
- **Si aparecen números distintos,** el caso es ambiguo y hay que reescribirlo.

## Cierre · ¿Qué construimos entre todos?

Al final de la clase votamos en Mentimeter la app que construimos los sábados 2, 3 y 4 (las tres opciones están en el [README principal](../README.md#el-proyecto-del-curso)). Gana una: todos hacemos la misma, cada uno la suya. Un agente la construye, la testeamos y la explicás.

## Para el sábado 31/10

1. Terminá la especificación del divisor.
2. Si en la votación ganó otra app, escribí también su especificación con la misma plantilla.
3. **Opcional:** subila al repo con un pull request y revisá el de otra persona. El paso a paso está en [`subir-tu-especificacion.md`](subir-tu-especificacion.md).
4. Instalá Python con la guía de EducaciónIT y cloná este repo (o tu fork).
5. Ticket de salida, en el chat: un caso borde que la IA no consideró.
