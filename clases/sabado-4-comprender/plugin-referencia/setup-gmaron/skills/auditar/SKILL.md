---
name: auditar
description: Audita especificacion.md contra historias.md y los tests. No corrige nada.
disable-model-invocation: true
allowed-tools: Read, Grep, Glob
---
Revisá `docs/especificacion.md`, `docs/historias.md` y los tests de `src/tests/`, y devolvé una tabla con estos hallazgos:

1. [SIN CASO] Requisito sin ningún caso.
2. [SIN TEST] Caso sin un test `test_<n>_…`, o test sin número de caso.
3. [NO COINCIDE] Test con el número de un caso que comprueba otra cosa.
4. [CONTRADICCIÓN] Dos casos que para la misma entrada esperan cosas distintas.
5. [SIN HISTORIA] Caso que no es criterio de ninguna historia.
6. [NO COMPROBABLE] Requisito que pytest no puede comprobar (pantalla, colores, navegador).
7. [DOCSTRING] Docstring que no dice lo que hace la función.
8. [SIN DECISIÓN] Requisito que no tiene una decisión en la sección "5. Decisiones" de `docs/especificacion.md`.

No cambies ningún archivo. Por cada hallazgo, decí en una línea qué tendría que decidir yo.
