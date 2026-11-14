---
name: handoff
description: Actualiza HANDOFF.md al cerrar una sesión, para que la próxima arranque sin preguntar en qué quedamos.
disable-model-invocation: true
---
Vamos a cerrar la sesión. Reescribí `docs/HANDOFF.md` para quien abra la próxima, que no va a saber nada de esta conversación.

1. Leé `docs/historias.md`, corré los tests y mirá qué archivos cambiaron en esta sesión.
2. Escribí `docs/HANDOFF.md` con estas secciones, en una pantalla:
   - **Fecha.**
   - **Qué se hizo:** qué historias pasaron a Hecho y con qué casos en verde.
   - **En qué quedamos:** cuál es la próxima historia y si hay algo a medio hacer.
   - **Decisiones:** qué se decidió en esta sesión y por qué, si no está en `docs/plan.md`.
   - **Para preguntar:** lo que encontraste y no te tocaba resolver (huecos de la especificación, historias [SIN CASO]).
   - **Cómo verificar:** los comandos y su resultado esperado.
3. No copies la especificación ni las historias: nombralas con su ID (R6, C12, H5).
4. Mostrame el `docs/HANDOFF.md` antes de terminar.
