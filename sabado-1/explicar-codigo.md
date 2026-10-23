# Que la IA te explique el código, de menos a más

En el curso, la IA va a explicar cada vez menos y vos cada vez más. El sábado 4 explicás una parte de tu código sin ayuda.

**Regla para todos los niveles:** la explicación de la IA también es una salida que hay que verificar. Puede sonar muy convincente y estar mal. Si dice que una línea hace algo, cambiá esa línea y fijate si pasa lo que dijo.

## Nivel 1 · La IA explica (sábado 1, con el pomodoro)

Abrí [`pomodoro/index.html`](pomodoro/index.html) en el navegador y probalo. Después pegale el código a la IA con este prompt:

```
Tarea: explicame este código como si supiera usar una computadora pero no supiera programar.
Instrucciones: primero decime qué partes tiene (HTML, CSS y JavaScript) y para qué sirve cada una. Después explicá qué hace cada función, en una o dos oraciones. No me propongas mejoras todavía.
Contexto: es un pomodoro que generó una IA a partir del prompt "Haceme un pomodoro".

[pegá acá el código]
```

Para comprobar lo que te dijo, buscá en el código la respuesta a estas preguntas:
- ¿Cuánto dura cada tramo? ¿Dónde está escrito?
- ¿Hay descanso largo cada cuatro pomodoros?
- ¿El contador de pomodoros sube cuando termina el trabajo o cuando termina el descanso?
- ¿Qué pasa si cerrás la pestaña a mitad de un pomodoro?

Cada respuesta es una decisión que tomó la IA porque el prompt no la tomó.

## Nivel 2 · La IA explica qué recibe y qué devuelve (sábado 1, con el divisor)

Cuando la IA te escriba el divisor a partir de tu especificación:

```
Tarea: explicame la función principal de este código.
Instrucciones: decime qué parámetros recibe, de qué tipo es cada uno y qué devuelve. Después mostrame, paso a paso, qué hace con este caso: [pegá un caso de tu especificación].
Contexto: es un divisor de gastos. Esta es mi especificación: [pegala].

[pegá acá el código]
```

Compará los parámetros con la sección "Qué recibe" de tu especificación y el valor de salida con "Qué devuelve". Si no coinciden, alguno de los dos está mal.

## Nivel 3 · Vos explicás primero (desde el sábado 2)

1. Leé una función del código que generó el agente.
2. Escribí, sin ayuda, qué creés que hace: qué recibe, qué devuelve y qué decisión toma.
3. Recién después pedile la explicación a la IA:

```
Tarea: corregí mi explicación de esta función.
Instrucciones: decime qué entendí bien, qué entendí mal y qué me faltó. No reescribas la función.

Mi explicación: [pegala]

[pegá acá la función]
```

## Nivel 4 · Sin la IA (sábado 4)

Elegí una parte de tu código y explicala en voz alta, sin ayuda: qué recibe, qué devuelve, qué decisión toma y por qué la tomaste vos y no la IA.
