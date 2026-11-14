# Handoff

**Fecha:** 31/10/2026.

## Qué se hizo

- H5 (montos con coma) y H6 (colores) pasaron a Hecho. H1 a H6 están hechas: C1 a C14 en verde.
- Hay tests también para C15 (cuadrito y nombre con el mismo color) y C16 (🤝 para quien está a mano), y pasan.
- No se tocó la especificación en esta sesión; los casos C14 a C16 ya estaban escritos.

## En qué quedamos

- No quedan historias en Por hacer. No hay nada a medio hacer.
- C15 y C16 no figuran como criterio de aceptación de ninguna historia (H6 solo cita C14).

## Decisiones

- Los colores y emojis son solo del texto de la pantalla; sin ellos el texto es el de antes (C14). El resto está en `plan.md`.
- Significado de los marcadores: 🟩 a quien le deben plata, 🟥 a quien debe, 🤝 a quien está a mano. Esto último no figura en la tabla de decisiones de la especificación.

## Para preguntar

- **C14 contradice a C15 y C16.** C14 dice que Ana lleva solo el nombre en verde, y C15/C16 dicen que lleva 🟩 y el nombre en verde. El código sigue C15/C16. Hay que corregir C14 en la especificación.
- **C15 y C16 sin historia.** ¿Se suman a los criterios de H6 o se crea una historia nueva (por ejemplo, para quien está a mano)?
- **R5 desactualizada.** Habla de rojo y verde, pero no del 🤝.
- Falta una fila en la tabla de decisiones con el significado de los marcadores 🟩/🟥/🤝.
- Sigue pendiente el chequeo del último ítem de la lista de entrega: que otra persona calcule 2 casos y llegue al mismo número.
- `ruff check .` da 26 avisos (líneas largas y un docstring); quedan para el sábado 3.

## Cómo verificar

```sh
../../.venv/bin/python -m pytest -q   # 21 passed
../../.venv/bin/ruff check .          # Found 26 errors.
printf 'Ana 1000\nBeto 0\n\n' | ../../.venv/bin/python src/divisor_gastos.py
```
