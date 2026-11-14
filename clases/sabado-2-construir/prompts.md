# Sábado 2 · Construir · Prompts

El agente construyó el divisor de gastos a partir de tu especificación: escribiste tu `CLAUDE.md`, armaste el plan en plan mode, pasaste las historias a `historias.md`, implementaste la primera con el agente y comprobaste que una sesión nueva sigue sola con la próxima tarea.

Todos los prompts se escriben en Claude Code abierto desde tu carpeta (`alumnos/<tu-usuario>/`), no desde la raíz del repo.

## Apertura: antes y después

### La pregunta a las dos versiones del repo

Se le hizo la misma pregunta a dos copias del mismo proyecto: una como quedó el sábado 1 y otra con `CLAUDE.md`, plan, historias y `HANDOFF.md`. Mirá la diferencia: la primera no sabe en qué quedamos y lista archivos; la segunda dice qué está hecho, qué sigue y qué hay que preguntar.

```text
¿En qué quedamos?
```

### Seguir sin explicar nada

En la versión organizada, una sola línea alcanza para que el agente tome la próxima historia, escriba los tests, los vea fallar e implemente. Es lo mismo que vas a probar vos al final de la clase.

```text
Seguí con la próxima tarea.
```

## Memoria del proyecto y contexto

### Tu `CLAUDE.md`, a mano (sin IA)

Esta parte no es un prompt: escribiste tu `CLAUDE.md` vos, sin el agente, respondiendo estas cuatro preguntas. La definición de terminado va una sola vez: pasan los tests de los casos de la historia y ruff no da avisos.

1. ¿Dónde está la fuente de verdad y qué hace el agente si el código no coincide con ella?
2. ¿Cómo se corre y cómo se comprueba? (los comandos exactos)
3. ¿Cómo es el ciclo de trabajo?
4. ¿Qué no se toca y cuándo una historia está terminada?

Un ejemplo terminado está en `codigo-paso-a-paso/sabado-2/CLAUDE.md`.

### `/init` y la comparación

Antes de correrlo, copiá tu `CLAUDE.md` a `CLAUDE-a-mano.md` (está en Comandos), porque `/init` modifica el que ya existe. Compará los dos: `/init` describe lo que hay (archivos, comandos, estructura); las decisiones (qué manda, qué no se toca, cuándo está terminado) las escribís vos.

```text
/init
```

### Ver qué ocupa la ventana de contexto

`/context` muestra qué ocupa la ventana: ahí aparecen el `AGENTS.md` de la raíz y tu `CLAUDE.md`. Después de `/clear`, volvé a mirar: la conversación se fue y los archivos de memoria siguen. Fijate cuánto ocupa tu `CLAUDE.md`.

```text
/context
```

```text
/clear
```

```text
/context
```

## Modelos y plan mode

### Elegir el modelo para planificar

Con `/model` ves los modelos de tu cuenta. El plan se hace con Opus, que es el que conviene para decisiones de diseño. Después entrás en plan mode con Shift+Tab hasta que aparezca "plan mode".

```text
/model
```

### El plan

En plan mode y con Opus. El agente no escribe código: propone una función por requisito, con su firma y la decisión técnica. Leé el plan entero antes de aprobarlo y buscá las marcas [DECIDÍ]: ahí decidís vos. Cambiá al menos una decisión antes de aprobar (por ejemplo, `float` o `Decimal` para la plata, o qué pasa con dos personas con el mismo nombre si usás un diccionario).

```text
**Tarea:** proponé un plan para construir el divisor de gastos a partir de `especificacion.md` y guardalo en `plan.md`.
**Instrucciones:** no escribas código. Para cada requisito, decí qué función lo resuelve, con su firma, y qué decisión técnica tomás (tipos, estructura de datos, manejo de errores). Marcá con [DECIDÍ] las decisiones que dependan de mí.
**Contexto:** seguí el `CLAUDE.md`. Ya hay código del sábado 1: decí qué se reusa y qué se cambia. Los casos de la especificación van a ser los tests.
```

Un plan terminado, con dos decisiones cambiadas, está en `codigo-paso-a-paso/sabado-2/docs/plan.md`.

## SDD: las tareas en `historias.md`

### Pasar el tablero a `historias.md`

Antes, numerá los requisitos de tu especificación como R1, R2… (los casos ya son C1, C2…). Pegá el prompt con el formato de abajo y las historias de tu tablero. Controlá cada criterio: tiene que ser un caso que existe en la especificación; uno que no está en la tabla es un invento. Una historia sin caso tiene que quedar marcada [SIN CASO].

```text
**Tarea:** pasá las historias de mi tablero a `historias.md` con este formato.
**Instrucciones:** los criterios de aceptación son IDs de casos de `especificacion.md`. No inventes casos ni requisitos: si una historia no tiene caso, marcala con [SIN CASO].
**Contexto:** estas son las historias del tablero: [pegarlas].
```

El formato de historia que va con el prompt:

```markdown
## H2 · Ver las cuentas antes de las transferencias
- **Como** alguien que tiene que pagar
- **quiero** ver cómo se calculó lo que me toca
- **para** confiar en el número.
- **Requisitos:** R3, R5
- **Criterios de aceptación:** C2, C3, C11
- **Estado:** Por hacer
```

Un `historias.md` terminado, con una historia en [SIN CASO], está en `codigo-paso-a-paso/sabado-2/docs/historias.md`.

## El agente construye

### Cambiar a Sonnet

Para implementar una historia con un plan claro alcanza Sonnet, el modelo de todos los días.

```text
/model
```

### La primera historia

El agente tiene que decir qué va a cambiar, escribir los tests de los casos, verlos fallar, implementar, correr los tests y marcar la historia como Hecho. Si un test falla, preguntate quién tenía razón, el test o el código. Si el agente cambia un test que ya existía para que pase, frenalo.

```text
Implementá la próxima historia de historias.md siguiendo el CLAUDE.md.
```

## La prueba de la sesión nueva

### Seguir desde una sesión en blanco

Es la evidencia de la clase. Borrá la conversación con `/clear` (o cerrá Claude Code y abrilo de nuevo desde tu carpeta) y escribí solo la segunda línea. Fijate qué historia tomó y si los tests quedaron en verde. Si tuviste que explicarle algo a mano, eso falta en tu `CLAUDE.md`.

```text
/clear
```

```text
Seguí con la próxima tarea.
```

## Conectores MCP

### Publicar las historias en el tablero

Con el MCP de tu tablero conectado (GitHub Projects, Notion o Trello), el agente publica las historias. El repo manda y el tablero muestra: las historias viven en `historias.md`. Revisá que cada una quede en la columna de su estado. La clave del conector va en tu configuración local, nunca en un archivo que se sube: el repo es público.

```text
Publicá las historias de historias.md en mi tablero, cada una en la columna de su estado.
```

## Skills

### `/explicar`: explicás vos primero

La skill no explica la función: te pide que la expliques vos y después corrige, con la línea, y avisa si la función contradice la especificación. Probala con una función que escribió el agente. Reemplazá `<función>` por el nombre de la función.

```text
/explicar <función>
```

Para usarla, creá `.claude/skills/explicar/SKILL.md` en tu carpeta con este contenido:

```markdown
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
```

### `/handoff`: dejar escrito en qué quedamos

Se corre al cerrar la sesión. Reescribe `HANDOFF.md` con qué se hizo, en qué quedamos, las decisiones, lo que hay que preguntar y cómo verificar. Es el archivo que leyó el agente en la apertura para saber en qué quedamos. Revisá el `HANDOFF.md` que te muestra antes de terminar.

```text
/handoff
```

El archivo completo de la skill está en `codigo-paso-a-paso/sabado-2/.claude/skills/handoff/SKILL.md`.

## Comandos

Copiar a tu carpeta lo del sábado 1, desde la raíz del repo (además de tu `especificacion.md`):

```bash
cp divisor/divisor.py divisor/tests/test_divisor.py alumnos/<tu-usuario>/
```

Abrir Claude Code desde tu carpeta:

```bash
cd alumnos/<tu-usuario>
claude
```

Guardar tu `CLAUDE.md` escrito a mano antes de correr `/init`:

```bash
cp CLAUDE.md CLAUDE-a-mano.md
```

Correr los tests, desde tu carpeta:

```bash
../../.venv/bin/python -m pytest -q
```

Revisar estilo y docstrings con ruff:

```bash
../../.venv/bin/ruff check .
```

Probar el programa con una entrada de ejemplo:

```bash
printf 'Ana 1000\nBeto 0\n\n' | ../../.venv/bin/python divisor.py
```

Traer el repo actualizado del curso (después de "Sync fork" en GitHub) e instalar ruff y el resto de las dependencias, desde la raíz del repo:

```bash
git pull
pip install -r requirements.txt
```
