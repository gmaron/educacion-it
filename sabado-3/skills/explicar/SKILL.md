---
name: explicar
description: Corrige la explicación que el alumno da de una función. No explica primero.
disable-model-invocation: true
argument-hint: <nombre de la función>
---
El alumno va a explicar la función $ARGUMENTS con sus palabras.

1. Si todavía no la explicó, pedile que lo haga. No la expliques vos.
2. Compará lo que dijo con el código. Marcá lo que está bien y lo que no, con la línea.
3. Por cada error, proponé un cambio chico en esa línea para que compruebe qué pasa.
4. Si la función contradice especificacion.md, decilo.
