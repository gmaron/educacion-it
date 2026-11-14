# Divisor de gastos (gmaron)

## Fuente de verdad

- `docs/especificacion.md` manda. Los requisitos son R1, R2…; los casos, C1, C2…
- Si el código y la especificación no coinciden, frená y avisame. No elijas uno.
- Si el comportamiento tiene que cambiar, primero cambio yo la especificación y después vos el código.

## Cómo se corre y cómo se comprueba

```sh
../../.venv/bin/python -m pytest -q        # los tests
../../.venv/bin/ruff check .               # PEP 8 y docstrings
printf 'Ana 1000\nBeto 0\n\n' | ../../.venv/bin/python src/divisor_gastos.py
```

## Ciclo de trabajo

- Al empezar, leé `docs/HANDOFF.md`: dice en qué quedamos. Al cerrar la sesión, lo actualizo con `/handoff`.
- Las tareas están en `docs/historias.md`. "La próxima tarea" es la primera historia en Por hacer que no esté marcada [SIN CASO].
- Una historia por vez. Al empezarla, cambiá su estado a En curso y pasá su tarjeta a DOING. Antes de escribir código, decime en tres líneas qué vas a cambiar, siguiendo `docs/plan.md`.
- Por cada caso de la historia, primero el test (`test_<número del caso>_...`, en un archivo nuevo de `src/tests/`: los que ya están commiteados no se tocan), lo ves fallar y después escribís el código.
- Al terminar, escribí el informe de cierre y pedime autorización para pasarla a Hecho. El informe tiene:
  - **Qué se hizo:** qué archivos cambiaron y para qué, y las decisiones que tomaste que la especificación no cubre.
  - **Criterios de aceptación:** cada caso de la historia, con su test y si pasa o no. Al final, si están todos cumplidos o cuáles faltan.
  - **Definición de terminado:** si pasan todos los tests y si `ruff check .` da avisos.
- Recién cuando te digo que sí, publicá el informe como comentario en la tarjeta, cambiá el estado a Hecho y pasá la tarjeta a DONE. Sin mi sí, la historia queda En curso y la tarjeta en DOING. Si falta algún criterio, no la propongas para DONE: decime qué falta.

## Trello

- Tablero: [Ingenieria de Software + Coding Agents](https://trello.com/b/6UaYhkvn/ingenieria-de-software-coding-agents). Cada historia tiene una tarjeta con el mismo título que en `docs/historias.md` ("H7 · Repartir la cuenta desde otra app").
- Cada vez que cambia una historia en `docs/historias.md` (el estado, los requisitos, los criterios), actualizá su tarjeta:
  - **Descripción:** la historia tal como está en `docs/historias.md`, sin el título: las líneas de Como, quiero y para, una línea vacía y la lista de Requisitos, Criterios de aceptación y Estado.
  - **Lista:** Por hacer → TODO, En curso → DOING, Hecho → DONE. A DONE solo con mi autorización.
- Si no encontrás la tarjeta, avisame. No la crees.
- `docs/historias.md` manda: si la tarjeta dice otra cosa, se pisa con lo del archivo.

## Qué no se toca

- Los tests que ya existen. Si creés que uno está mal, avisame.
- Las historias [SIN CASO]: sin caso no hay cómo comprobarlas. Avisame que les falta.
- `docs/especificacion.md`: la cambio yo.
- Las firmas de `dividir`, `mostrar` y `explicar`.

## Cuándo una historia está terminada

- Pasan todos los tests: los de la historia y los que ya estaban.
- `ruff check .` no da avisos (PEP 8 y docstrings).
