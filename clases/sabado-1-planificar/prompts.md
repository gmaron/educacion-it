# Sábado 1 · Planificar · Prompts

Le pedimos un pomodoro a la IA sin especificar nada, vimos todo lo que decidió por nosotros y escribimos la especificación del divisor de gastos, con casos y números esperados, para probarla después contra el código que devuelve la IA.

## Práctica 1 · Un pomodoro en 15 minutos

### Haceme un pomodoro

Es zero-shot: la tarea sola, sin nada más. Escribilo en Claude.ai o Gemini, probá lo que aparece y fijate qué decidió la IA por vos (cuánto dura cada tramo, si hay descanso largo, qué pasa si cerrás la pestaña).

```text
Haceme un pomodoro
```

### Que la IA te explique tu pomodoro

Pegale el código de tu pomodoro junto con este prompt. Con la explicación en mano, buscá en el código dónde dice cuánto dura cada tramo, si hay descanso largo y cuándo sube el contador.

```text
Explicame este código como si no supiera programar: qué partes tiene (HTML, CSS y JavaScript) y qué hace cada función. No me propongas mejoras.
```

### Explicar el código, nivel 1 (versión completa, con tarea, instrucciones y contexto)

Es la versión del repo del mismo pedido, armada con TIC. Sirve para tu pomodoro o para el del repo (`sabado-1/pomodoro/index.html`). La explicación también hay que verificarla: si dice que una línea hace algo, cambiala y fijate si pasa lo que dijo.

```text
Tarea: explicame este código como si supiera usar una computadora pero no supiera programar.
Instrucciones: primero decime qué partes tiene (HTML, CSS y JavaScript) y para qué sirve cada una. Después explicá qué hace cada función, en una o dos oraciones. No me propongas mejoras todavía.
Contexto: es un pomodoro que generó una IA a partir del prompt "Haceme un pomodoro".

[pegá acá el código]
```

## Práctica 2 · La especificación del divisor de gastos

### La IA como entrevistadora

Si te quedás sin ideas para los casos borde, que la IA te haga las preguntas. El prompt tiene tarea, instrucciones y contexto (TIC). Mirá la tabla final y los casos marcados con [DUDA]: cada número que proponga, calculalo a mano, porque con el redondeo suele equivocarse.

```text
Tarea: entrevistame como analista para encontrar los casos borde de una app que divide gastos entre amigos.

Instrucciones: hacé una pregunta por vez. No escribas código. Al final, listá los casos que surgieron en una tabla con entrada y resultado esperado, y marcá con [DUDA] los que dependan de una decisión mía.

Contexto: es para un asado entre amigos; cada uno puso una cantidad distinta y algunos no pusieron nada.
```

La plantilla y el ejemplo del pomodoro están en `clases/sabado-1-planificar/` (`plantilla-especificacion.md` y `ejemplo-especificacion-pomodoro.md`).

## Práctica 3 · Del chat al repo: ¿le da el número?

Acá le pegás tu especificación completa a la IA y le pedís el código. Al pasarle la tabla de casos estás haciendo few-shot. Después comparás 2 casos de tu tabla con el resultado y, si clonaste el repo, los pasás a `divisor/tests/test_divisor.py` y corrés `pytest`.

### Primeros pasos en el repo: qué hace el test

Con el repo abierto en VS Code, preguntale a la IA por el test que trae el esqueleto.

```text
¿Qué hace este test, línea por línea?
```

### Por qué falla pytest

Que el test falle al principio está bien: la función todavía no existe. Que la IA te lo confirme leyendo el error.

```text
¿Por qué falla pytest?
```

### Qué recibe y qué devuelve la función

Compará la respuesta con las secciones "Qué recibe" y "Qué devuelve" de tu especificación.

```text
¿Qué recibe y qué devuelve la función? ¿Coincide con mi especificación?
```

### Explicar el código, nivel 2: parámetros, salida y un caso paso a paso

Cuando la IA te escriba el divisor. Compará los parámetros con "Qué recibe" y el valor de salida con "Qué devuelve": si no coinciden, alguno de los dos está mal.

```text
Tarea: explicame la función principal de este código.
Instrucciones: decime qué parámetros recibe, de qué tipo es cada uno y qué devuelve. Después mostrame, paso a paso, qué hace con este caso: [pegá un caso de tu especificación].
Contexto: es un divisor de gastos. Esta es mi especificación: [pegala].

[pegá acá el código]
```

## Cierre · Del documento al tablero

### Partir la especificación en historias de usuario

Cada historia lleva sus criterios de aceptación, que son los casos de tu tabla, y va al tablero (Por hacer, En curso, Hecho). Verificá igual que antes: cada criterio tiene que tener un número, y ninguno puede ser un caso que no esté en tu tabla.

```text
Partí esta especificación en historias de usuario con criterios de aceptación. No inventes casos que no estén en la tabla.
```

## Tarea opcional · Subir tu especificación con un pull request

### Pedirle el PR a un agente

Si hiciste el camino por la terminal, podés pedirle a un agente que abra el PR. Leé qué comandos corre antes de aceptarlos.

```text
abrí un PR de esta branch hacia gmaron/educacion-it
```

## Comandos

### Clonar el repo y preparar el entorno

El test falla al principio: la función del divisor todavía no existe.

```bash
git clone https://github.com/gmaron/educacion-it.git
cd educacion-it
python -m venv .venv
source .venv/bin/activate      # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest
```

### Subir tu especificación desde la terminal (camino B)

Antes, hacé un fork del repo en tu cuenta de GitHub.

```bash
git clone https://github.com/<tu-usuario>/educacion-it.git
cd educacion-it
git checkout -b especificacion-divisor
mkdir -p alumnos/<tu-usuario>
cp sabado-1/plantilla-especificacion.md alumnos/<tu-usuario>/especificacion.md
# completá la especificación y agregá tu línea en alumnos/README.md
git add alumnos/
git commit -m "Especificación del divisor de <tu-usuario>"
git push -u origin especificacion-divisor
```

### Mantener tu fork al día

```bash
git remote add upstream https://github.com/gmaron/educacion-it.git
git pull upstream main
```

### Leer la historia del repo

```bash
git log --oneline --graph
```
