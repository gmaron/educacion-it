# Especificación: pomodoro (ejemplo bien hecho)

## 1. Qué hace
Un temporizador que alterna tramos de trabajo y de descanso para trabajar concentrado.

## 2. Qué recibe
- Un botón para iniciar, pausar y reanudar.
- Las duraciones son fijas en esta versión. No se configuran.

## 3. Qué devuelve
- El tiempo que queda del tramo actual, en minutos y segundos.
- Qué tramo está corriendo: trabajo, descanso corto o descanso largo.
- Un sonido al terminar cada tramo.

## 4. Casos con número esperado

| # | Entrada | Resultado esperado |
| --- | --- | --- |
| 1 | Inicio y espero 25 min | Suena y arranca un descanso de 5 min |
| 2 | Pauso en el minuto 10 y reanudo | El tramo termina 15 min después de reanudar |
| 3 | Termino el 4.º pomodoro | Arranca un descanso de 15 min |
| 4 | Termino el descanso largo | Arranca el pomodoro 1 de un ciclo nuevo |
| 5 | Cierro la pestaña en el minuto 12 | Al volver, arranca de cero |

## 5. Decisiones

| Decisión | Motivo |
| --- | --- |
| Trabajo de 25 min, descanso corto de 5 y descanso largo de 15 cada 4 pomodoros | Es la técnica original. Se puede cambiar en una versión 2 |
| Si cerrás la pestaña, se pierde el pomodoro en curso | Esta versión no guarda nada. Guardar el estado es una funcionalidad aparte |
| Al terminar un tramo, el siguiente arranca solo | Así no tenés que tocar nada. La alternativa era esperar un clic |

---

**De dónde salió cada campo:** las preguntas del debate de la clase.
- **"¿Cuánto dura cada pomodoro?"** se convirtió en una regla y en la primera decisión.
- **"¿Qué pasa si cierro la pestaña?"** se convirtió en el caso 5 y en una decisión escrita.
- **"¿Hicieron la misma app?"** explica por qué hace falta todo esto: sin especificación, cada IA decide distinto.
