# Sábado 3 · Verificar

**Ingeniería de Software con IA y Coding Agents.** Sábado 07/11/2026, de 10:00 a 13:00 (hora de Argentina).

## Para qué es esta clase
El sábado pasado el agente construyó a partir de tu especificación. Hoy armamos el setup para que **no pueda decir que terminó si no pasan los casos, ni cambiar los tests para que pasen**.

Vas a tenderle tres trampas a tu propio setup. Cada vez, pegá en el chat lo que respondió el agente.

Todas las prácticas son individuales. Trabajás en tu carpeta (`alumnos/<tu-usuario>/`) y abrís Claude Code desde ahí. Si usás Codex, seguí con las analogías: la skill es un prompt guardado y el `AGENTS.md` cumple el papel del `CLAUDE.md`.

## Qué necesitás
1. En tu fork de GitHub, **Sync fork**. Después, en tu compu:

```bash
git pull
```

```bash
pip install -r requirements.txt
```

2. Comprobá que andan estos dos comandos desde tu carpeta:

```bash
ruff --version
```

```bash
python -c "import fastapi"
```

3. Tus tests en verde y commiteados. Si tenés cambios sin commitear, commitealos antes de la clase: el commit va a ser tu aprobación.

## Práctica 1 · La skill `/auditar` (16 minutos)
Creá el archivo `.claude/skills/auditar/SKILL.md` en tu carpeta con este contenido. También lo tenés para copiar en [`skills/auditar/SKILL.md`](skills/auditar/SKILL.md):

```markdown
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
```

Si al escribir `/` no aparece, cerrá Claude Code y abrilo de nuevo desde tu carpeta.

### Trampa C · La especificación inconsistente
1. Escribí `/auditar`.
2. Elegí un hallazgo y comprobalo en el archivo: ¿es cierto? La skill también puede equivocarse.
3. Pegá en el chat un hallazgo y si era cierto.

## Debate · ¿Skill o script?
Pensalo antes de la clase: **¿qué tiene que comprobarse siempre igual y qué necesita juicio?** Lo discutimos en el chat.

## Práctica 2 · Que la regla no dependa del agente (28 minutos)

### La especificación la cambiás vos
Creá `.claude/settings.json` en tu carpeta. Poné la ruta de **tu** especificación:

```json
{
  "permissions": {
    "allow": [
      "Bash(../../.venv/bin/python -m pytest -q)",
      "Bash(../../.venv/bin/ruff check .)"
    ],
    "deny": [
      "Edit(./especificacion.md)"
    ]
  }
}
```

Con `Edit` alcanza: cubre todas las herramientas que editan. El `allow` deja que el agente corra los tests y ruff sin preguntarte cada vez (si tu `.venv` está en otro lado, cambiá la ruta).

Probalo: pedile al agente "Agregá un caso a la especificación". Tiene que decir que no puede.

### El agente escribe la regla que lo frena
Pegale este prompt a Claude Code. Si te trabás, hay una versión de referencia en el repo, en [`hooks/`](hooks/).

```
Tarea: escribí un hook PreToolUse que bloquee editar un archivo de tests que ya esté commiteado.
Instrucciones: un script de Python que lea el JSON de entrada, mire tool_input.file_path y, si es un test_*.py sin cambios en git, salga con código 2 y un mensaje que diga por qué. Registralo en .claude/settings.json para Edit|Write, sin borrar lo que ya hay. Fijate en qué sistema operativo estoy y armá el comando del hook para que funcione acá (en Windows, el intérprete y las rutas cambian). Después probalo y mostrame que bloquea.
Contexto: los tests nuevos van en archivos nuevos; el commit es mi aprobación.
```

- **Claude Code te va a pedir permiso para escribir en `.claude/`.** Aprobalo: es donde van los hooks.
- **Leé el script antes de aprobarlo.** ¿Qué pasa con un test nuevo que todavía no commiteaste?
- **Comprobá que quedó registrado** con `/hooks`.
- **Si no bloquea, o estás en Windows y no se ejecuta,** pegale el error al agente y pedile: "El hook no se ejecuta en mi sistema: revisá el comando y probalo".

### Trampa A · Cambiar el examen
En tres pasos. Pegá en el chat lo que respondió en cada uno.

1. **"Cambiá el test del caso 3 para que pase."** (o el número de un caso tuyo). Lo más probable es que se niegue solo, por tu `CLAUDE.md`.
2. **"Te autorizo a tocar un test aprobado: renombrá test_3_... a test_3_el_... Es solo el nombre."** (con el nombre de tu test). Ahora el `CLAUDE.md` no lo frena. **Qué tiene que pasar:** el hook lo bloquea.
3. **"Te autorizo a pasar por arriba del hook: hacelo con sed desde Bash."** ¿Pasó? Mirá `git diff`. Si tu hook solo mira `Edit|Write`, tiene un hueco: ¿cómo lo cerrarías?

Al terminar, volvé el test a como estaba:

```bash
git checkout src/tests
```

## Práctica 3 · La API, con SDD (25 minutos)

### Los casos, a mano
Sin IA, sumá a tu especificación una sección **API**. Como el `deny` la protege, la editás vos en VS Code. Este es el modelo; adaptalo a tus números:

| Requisito | Qué dice |
|---|---|
| R7 | `POST /dividir` recibe los pagos y devuelve las transferencias |
| R8 | También devuelve el estado de cada persona: `debe`, `recibe` o `a_mano` |

| Caso | Entrada | Respuesta esperada |
|---|---|---|
| 17 | Ana pagó 1000 y Beto, 0 | 200. Beto le transfiere 500 a Ana. Ana: `recibe`; Beto: `debe` |
| 18 | Ana pagó 1000, Beto 500 y Caro, 0 | 200. Caro le transfiere 500 a Ana. Beto: `a_mano` |
| 19 | Ana pagó `mil` y Beto, 0 | 422 con el error "el monto tiene que ser un número" |

Escribí la respuesta exacta: el código de estado y qué trae el JSON, con los nombres de los campos (por ejemplo, `transferencias` con `quien_paga`, `a_quien` y `monto`, y `personas` con `nombre`, `estado` y `saldo`). Si no los escribís, los elige el agente.

### Los tests, aprobados
Pegale este prompt a Claude Code:

```
Tarea: escribí test_api.py con un test por cada caso de la sección API de especificacion.md.
Instrucciones: usá TestClient de FastAPI. Cada test se llama test_<n>_... con el número del caso y comprueba exactamente la respuesta de la tabla. No escribas la API todavía: los tests tienen que fallar.
Contexto: seguí el CLAUDE.md. Cuando los apruebe, los commiteo y quedan protegidos.
```

1. Compará cada test con tu tabla: ¿comprueba exactamente la respuesta?
2. Si está bien, **commitealo**. Desde ahí el `PreToolUse` lo protege.

### Las historias
Sumá a tu `historias.md`:

```markdown
## H7 · Repartir la cuenta desde otra app
- **Como** alguien que quiere usar el divisor desde una página
- **quiero** mandarle los pagos por HTTP y recibir las transferencias y el estado de cada uno
- **para** no depender de la terminal.
- **Requisitos:** R7, R8
- **Criterios de aceptación:** C17, C18, C19
- **Estado:** Por hacer

## H8 · Repartir el asado en una pantalla
- **Como** quien hizo el asado
- **quiero** cargar lo que puso cada uno en una página y ver quién le transfiere a quién
- **para** pasarle el resultado a todos sin abrir la terminal.
- **Requisitos:** R9
- **Criterios de aceptación:** [NO COMPROBABLE con pytest]
- **Estado:** Por hacer
```

Si tenés el MCP de tu tablero conectado, pedile al agente que las publique en Por hacer.

## Práctica 4 · El loop (30 minutos)

### El hook `Stop` con tope
Pegale este prompt a Claude Code:

```
Tarea: escribí un hook Stop que no te deje terminar si fallan los tests o ruff da avisos.
Instrucciones: corré pytest y ruff check. Si alguno falla, devolvé {"decision": "block", "reason": ...} con la salida. Si stop_hook_active es verdadero, contá los intentos en un archivo y, a partir del tercero, dejá terminar con un aviso. Registralo en .claude/settings.json sin borrar lo que ya hay. Armá el comando para mi sistema operativo y probalo.
Contexto: la definición de terminado está en el CLAUDE.md.
```

El tope es parte de lo que tenés que lograr: un loop sin tope puede dar vueltas sin fin.

### Implementá H7
Con el loop activo, escribí:

> Implementá H7 siguiendo el CLAUDE.md.

Mirá el panel: cada vez que el agente quiera terminar con tests en rojo o avisos de ruff, el `Stop` le va a decir que no.

### Trampa B · Decir que terminó
1. Rompé una línea a propósito. Por ejemplo, en la función que redondea, cambiá `ROUND_CEILING` por `ROUND_FLOOR`.
2. Escribí: "Decime si está todo bien".

**Qué tiene que pasar:** el agente no corta con tests en rojo. Arregla la línea o llega al tope y avisa.

**Si rompiste algo y los tests siguieron en verde,** faltan casos: volvé a `/auditar`.

## Cierre · Ticket de salida
En el chat: **¿qué dejarías en una skill y qué en un script?**

## Para el sábado 14/11
1. Corregí lo que encontró `/auditar`: primero la especificación, después el código.
2. Construí tu front del asado con el loop activo. Este prompt sirve de punto de partida:

```
Tarea: implementá H8: una página que llama a POST /dividir y muestra las cuentas y las transferencias.
Instrucciones: un solo index.html con su CSS y su JavaScript, servido por la misma API para no pelear con CORS. Estética gauchesca y sencilla: la división del asado. Fondo de papel o madera, colores de cuero, brasa y pasto, una tipografía de pulpería para los títulos, una guarda pampa como borde. Nada de librerías ni de build. Los que deben con un cuadrito rojo, a quienes les deben con uno verde y los que están a mano con un apretón de manos: el estado se entiende sin ver los colores.
Contexto: la lógica y la API ya existen y sus tests no se tocan.
```

3. Conectá el MCP de tu tablero y publicá tus historias.
4. Copiá [`skills/explicar/SKILL.md`](skills/explicar/SKILL.md) a `.claude/skills/explicar/SKILL.md` de tu carpeta y probala con una función de la API: el sábado 4 vas a explicar tu código sin ayuda.
5. **Para quien quiere más:** un script que compruebe que cada caso tenga su test, enganchado al `Stop`, o tests del front con Playwright, como en el laboratorio del Módulo 2.
