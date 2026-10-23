# Sábado 1 · Planificar

**Pedile a la IA algo que puedas verificar.** Sábado 24/10/2026, de 10:00 a 13:00 (hora de Argentina).

Hoy trabajamos la primera parte del criterio: **escribir una especificación que se pueda verificar**. El sábado que viene, un agente va a programar a partir de ella.

## Práctica 1 · Un pomodoro en 15 minutos (en parejas)

1. Abran Claude.ai o Gemini.
2. Escriban solo esto: **Haceme un pomodoro**
3. Cuando aparezca, pruébenlo.

Después lo conversamos: ¿qué decidió la IA por ustedes?

**Para ir más lejos:** comparen el suyo con [`pomodoro/index.html`](pomodoro/index.html) y pídanle a la IA que les explique el código con el nivel 1 de [`explicar-codigo.md`](explicar-codigo.md).

## Práctica 2 · La especificación del divisor de gastos (en parejas, 25 minutos)

Con la [plantilla](plantilla-especificacion.md), escriban la especificación de un programa que diga quién le debe a quién después de un asado. Para ver cómo es una especificación bien hecha, miren el [ejemplo del pomodoro](ejemplo-especificacion-pomodoro.md).

1. Empiecen por el caso más simple: dos personas.
2. Después, busquen los casos donde el programa se rompe.

**Lo que tienen que entregar:**
- Al menos 5 casos, cada uno con un número esperado.
- Al menos 1 caso borde que la IA no haya considerado.
- Al menos 1 decisión propia, con su motivo.

### Si se quedan sin ideas: la IA como entrevistadora

```
Tarea: entrevistame como analista para encontrar los casos borde de una app que divide gastos entre amigos.

Instrucciones: hacé una pregunta por vez. No escribas código. Al final, listá los casos que surgieron en una tabla con entrada y resultado esperado, y marcá con [DUDA] los que dependan de una decisión mía.

Contexto: es para un asado entre amigos; cada uno puso una cantidad distinta y algunos no pusieron nada.
```

**Ojo:** cada número que proponga la IA, calculalo a mano. Con el redondeo suele equivocarse.

## Práctica 3 · ¿Le da el número? (en parejas, 20 minutos)

1. Péguenle la especificación completa a la IA y pídanle el código.
2. Elijan 2 casos de su tabla y comparen el resultado con el número esperado.

**Si clonaron el repo:** pidan que el código respete la firma de [`divisor/divisor.py`](../divisor/divisor.py), péguenlo ahí, pasen sus casos a [`divisor/tests/test_divisor.py`](../divisor/tests/test_divisor.py) y corran `pytest`. Después pídanle a la IA que les explique la función con el nivel 2 de [`explicar-codigo.md`](explicar-codigo.md).

## Cierre · Intercambio

Pásenle su especificación a otra pareja. Esa pareja elige 2 casos y calcula el resultado sin preguntar nada.
- **Si llega al mismo número,** el caso está claro.
- **Si llega a otro número,** el caso es ambiguo y hay que reescribirlo.

## Para el sábado 31/10

1. Terminen la especificación del divisor y súbanla.
2. Elijan la app que van a construir desde el sábado 2 (la lista está en el [README principal](../README.md#las-apps-del-curso)). Si no es el divisor, escriban su especificación con la misma plantilla.
3. Instalen Python con la guía de EducaciónIT y clonen este repo.
4. Ticket de salida, en el chat: un caso borde que la IA no consideró.
