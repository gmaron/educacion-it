---
name: auditar
description: Audita especificacion.md contra historias.md y los tests. No corrige nada.
disable-model-invocation: true
---
Revisá `especificacion.md`, `historias.md` y los tests, y devolvé una tabla con estos hallazgos:

1. [SIN CASO] Requisito sin ningún caso.
2. [SIN TEST] Caso sin un test `test_<n>_…`, o test sin número de caso.
   [NO COINCIDE] Test con el número de un caso que comprueba otra cosa.
3. [CONTRADICCIÓN] Dos casos que para la misma entrada esperan cosas distintas.
4. [SIN HISTORIA] Caso que no es criterio de ninguna historia.
5. [NO COMPROBABLE] Requisito que pytest no puede comprobar (pantalla, colores, navegador).
6. [DOCSTRING] Docstring que no dice lo que hace la función.

No cambies ningún archivo. Por cada hallazgo, decí en una línea qué tendría que decidir yo.
