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
- Una historia por vez. Antes de escribir código, decime en tres líneas qué vas a cambiar, siguiendo `docs/plan.md`.
- Por cada caso de la historia, primero el test (`test_<número del caso>_...` en `src/tests/test_divisor_gastos.py`), lo ves fallar y después escribís el código.
- Al terminar, cambiá el estado de la historia a Hecho y decime qué casos quedaron en verde.

## Qué no se toca

- Los tests que ya existen. Si creés que uno está mal, avisame.
- Las historias [SIN CASO]: sin caso no hay cómo comprobarlas. Avisame que les falta.
- `docs/especificacion.md`: la cambio yo.
- Las firmas de `dividir`, `mostrar` y `explicar`.

## Cuándo una historia está terminada

- Pasan todos los tests: los de la historia y los que ya estaban.
- `ruff check .` no suma avisos nuevos. Los 27 que hay hoy (líneas largas y un docstring) quedan para el sábado 3: no los arregles ahora.
