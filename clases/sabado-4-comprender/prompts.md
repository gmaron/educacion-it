# Sábado 4 · Comprender · Prompts

Cerramos H8, vimos contexto y RAG con el laboratorio del Módulo 3, empaquetamos el setup como plugin (con el subagente revisor y su hook), revisamos una interfaz con un modelo multimodal y con Impeccable, hablamos de deuda cognitiva y cada uno explicó su código y su setup sin ayuda.

Todo se hace en tu carpeta del divisor (`alumnos/<tu-usuario>/`), con `claude` abierto ahí, salvo donde se indica otra carpeta.

## 1 · Apertura: cerrar H8

### Retomar la sesión
Para que el agente diga en qué estado quedó el proyecto. Mirá que aparezca H8 En curso y lo que quedó [NO COMPROBABLE].

```text
¿En qué quedamos?
```

### Informe de cierre de H8
Pedile el informe antes de dar la historia por terminada. Leelo entero: qué casos están en verde y qué no se pudo comprobar.

```text
Escribí el informe de cierre de H8.
```

### Pasar H8 a Hecho
Solo si el informe te convence. La tarjeta tiene que pasar a DONE en Trello.

```text
Sí, pasala a Hecho
```

## 2 · Contexto, RAG y el laboratorio del Módulo 3

### Grep como recuperación
Una pregunta por significado, sin la palabra exacta. Mirá cómo el agente arma la búsqueda con sinónimos y llega a la función que maneja los saldos.

```text
¿Dónde se maneja que alguien no deba nada? Respondé en tres líneas con archivo y línea.
```

### El script del laboratorio: concatenar.py
El agente escribe un script que junta todo el proyecto en un solo archivo. Mirá cuántos caracteres y tokens da y qué parte de eso es ruido (por ejemplo, plantillas que nunca usaste).

```text
Tarea: escribí concatenar.py, que junte todos los archivos de este proyecto en un solo proyecto.txt.
Instrucciones: recorré la carpeta, saltá .venv, __pycache__, .pytest_cache y .git, y antes de cada archivo poné una línea con su ruta. Al final imprimí cuántos archivos juntó, cuántos caracteres y una estimación de tokens (caracteres / 4). No lo agregues a git.
Contexto: es el laboratorio del Módulo 3: después le voy a pasar proyecto.txt a un chat para hacerle preguntas sobre el proyecto.
```

### Las preguntas del laboratorio (para casa)
Subí `proyecto.txt` a un chat y hacele estas dos preguntas. Después hacele lo mismo al agente en tu carpeta: ¿cuál respondió mejor? ¿Cuál leyó menos?

```text
¿Cuál es el propósito general del proyecto?
```

```text
¿Qué tecnologías se usan y cómo?
```

### Cuánto te cuesta el setup
Antes de escribir nada, mirá cuánto ocupan las herramientas de los MCP, el `CLAUDE.md` y las descripciones de las skills. ¿Qué es lo que más te ocupa? ¿Lo usás?

```text
/context
```

## 3 · El setup como plugin

### Armar el plugin
El agente empaqueta tus skills y tus hooks en `plugin/`. Aprobá los permisos para crear archivos. Mirá si detecta lo que cada hook da por sentado de este proyecto (rutas fijas, el `.venv`, que haya tests) y si `claude plugin validate` pasa al final.

```text
Tarea: armá un plugin de Claude Code con mi setup, para usarlo en otro proyecto.
Instrucciones: creá la carpeta plugin/ con .claude-plugin/plugin.json (nombre setup-<mi usuario>), mis skills de .claude/skills (sin las speckit-*, que son de terceros) y mis hooks de .claude/settings.json pasados a hooks/hooks.json, con las rutas de los scripts en ${CLAUDE_PLUGIN_ROOT}. Sumá plugin/.claude-plugin/marketplace.json para poder instalarlo. Antes de copiar cada hook, fijate qué supone de este proyecto (rutas, el .venv, que haya tests) y hacelo funcionar en una carpeta que no tenga nada de eso. Armá los comandos para mi sistema operativo. Al final corré claude plugin validate sobre plugin/.
Contexto: el CLAUDE.md y docs/ no van al plugin: son de este proyecto.
```

El plugin completo de referencia está en `clases/sabado-4-comprender/plugin-referencia/`.

### Prueba 3: ver las skills en la carpeta vacía
Ya dentro de `claude` en la carpeta vacía (el comando está en "Comandos"), cuando pregunte si confiás en la carpeta elegí Yes. Escribí esto y elegí del menú: las skills de un plugin llevan su nombre como prefijo (`setup-<tu-usuario>:explicar`).

```text
/setup
```

### Prueba 3: ver los hooks del plugin
Primero muestra la lista de eventos. Entrá a `PreToolUse`, `PostToolUse` y `Stop` con Enter para ver los hooks que vinieron con el plugin. Pegá en el chat lo que te muestra.

```text
/hooks
```

### Prueba 3: ¿el Stop deja terminar?
En una carpeta sin tests, el `Stop` tiene que dejar terminar. Si se traba, es porque copió una ruta fija o supone un `.venv`: ese es el hallazgo.

```text
Hola, ¿terminaste?
```

### Ver el subagente revisor
Para comprobar que el plugin trajo el subagente. Tiene que aparecer `setup-<tu-usuario>:revisor` en la lista.

```text
¿Qué subagentes tenés disponibles?
```

### Instalar el plugin de verdad
Para quien quiera instalarlo con un marketplace en lugar de usar `--plugin-dir`.

```text
/plugin marketplace add <ruta a plugin/>
```

```text
/plugin install setup-<tu-usuario>@<nombre del marketplace>
```

### Provocar al revisor del hook PostToolUse
Con el plugin cargado en tu carpeta del divisor. El pedido contradice la especificación a propósito y le dice que no lea `docs/` antes. Mirá cómo el revisor responde citando el requisito y los casos, y cómo el agente deshace el cambio. Si el agente lee la especificación igual y se frena solo, fue el `CLAUDE.md`: el hook es la red para cuando no lo hace.

```text
En src/divisor_gastos.py cambiá MENSAJE_A_MANO a "Quedaron a mano", sin leer docs/ antes. Si algo te avisa que contradice la especificación, deshacelo y contame qué te avisó.
```

El prompt del revisor que corre en ese hook está en `clases/sabado-4-comprender/plugin-referencia/setup-gmaron/hooks/hooks.json` (el `PostToolUse` de tipo `agent`), y el subagente en `clases/sabado-4-comprender/plugin-referencia/setup-gmaron/agents/revisor.md`.

### Pedirle una revisión al subagente
El subagente trabaja con su propio contexto y solo puede leer. Mirá la tabla de requisitos y casos con archivo y línea, y que avise que no puede correr pytest porque no tiene Bash.

```text
Usá el subagente revisor para revisar H7 contra la especificación.
```

## 4 · Interfaces con IA

### Revisión multimodal de la captura
Arrastrá a Claude una captura de tu front (o de tu Streamlit) y pegá esto. Es una segunda opinión sobre lo que pytest no ve, no un test.

```text
Mirá esta captura. ¿Se entiende quién debe, quién recibe y quién está a mano sin ver los colores? Si no, decime qué cambiarías. No toques el código.
```

Contra esa opinión, Impeccable mide con reglas fijas: el comando está en "Comandos". Mirá el contraste que marca en números y comparalo con lo que dijo el multimodal.

## 6 · Ensayo y presentaciones

### Corregir tu explicación de una función
Para entrenar la prueba 1, no como muleta: primero explicás vos la función y la skill corrige lo que dijiste, con la línea, y te propone un cambio chico para comprobarlo. En un plugin se llama `/setup-<tu-usuario>:explicar`.

```text
/explicar <nombre de la función>
```

## 8 · Segunda iteración: cuando el proyecto crece

### graphify
Arma un grafo del repo que el agente consulta antes de buscar archivos. Medí con `/context` antes y después: en un repo chico ahorra casi nada.

```text
/graphify .
```

### El revisor en GitHub Actions
El mismo subagente revisor, corriendo con `claude -p` en cada PR. El workflow completo está en `clases/sabado-4-comprender/segunda-iteracion/revisar-pr.yml` y necesita el secreto `ANTHROPIC_API_KEY`.

```bash
claude -p "Usá el subagente revisor para revisar los archivos de src/ que cambian en este PR contra docs/especificacion.md. Devolvé la tabla en markdown." \
  --allowedTools "Agent,Read,Grep,Glob" \
  --max-turns 30 >> "$GITHUB_STEP_SUMMARY"
```

## Extra

### Un Gantt en Mermaid
Diagramación con IA a partir de tus historias. Sirve para ver cómo funciona y como crítica: un Gantt de algo que ya se hizo no planifica nada.

```text
Leé docs/historias.md y armame un diagrama de Gantt en Mermaid con H1 a H8, en el orden en que se hicieron. Marcá la ruta crítica y un riesgo por historia.
```

### Un modelo local
En Open WebUI (http://localhost:3000) con `qwen3:8b` corriendo en Ollama. Mirá cuánto piensa antes de responder y a qué velocidad escribe. Si le subís el `proyecto.txt` chico, notá que la ventana por defecto es de 4.096 tokens: lo que no entra, no existe.

```text
¿Qué es RAG? En una oración.
```

## Comandos

Desde tu carpeta `alumnos/<tu-usuario>/` dentro del repo del divisor, salvo donde se indica.

Tests y ruff en verde antes de empezar:

```bash
../../.venv/bin/python -m pytest -q && ../../.venv/bin/ruff check .
```

Correr el script del laboratorio:

```bash
../../.venv/bin/python concatenar.py
```

Validar el plugin que armó el agente:

```bash
claude plugin validate plugin/
```

Prueba 3: abrir Claude en una carpeta vacía con tu plugin (en Windows, creá la carpeta a mano en otro lugar):

```bash
cd /tmp && mkdir -p carpeta-vacia && cd carpeta-vacia && git init -q && claude --plugin-dir "<ruta a tu carpeta>/plugin"
```

Abrir tu proyecto con el plugin de referencia (para la demo del revisor):

```bash
claude --plugin-dir "<ruta a>/clases/sabado-4-comprender/plugin-referencia/setup-gmaron"
```

Levantar el front del asado:

```bash
../../.venv/bin/python -m uvicorn api:app --app-dir src
```

Impeccable sobre los archivos del front (usá el archivo, no la página renderizada):

```bash
npx -y impeccable detect src/
```

Instalar Impeccable (trae `/impeccable critique` y `/impeccable audit`, la parte con LLM, y ofrece un hook):

```bash
npx impeccable install
```

```text
/plugin marketplace add pbakaus/impeccable
```

Cobertura de tests: qué líneas no cubre ningún caso:

```bash
pytest --cov
```

Segunda iteración, graphify:

```bash
uv tool install graphifyy && graphify install
```

Segunda iteración, los MCP de Context7 y Playwright (el `.mcp.json` equivalente está en `clases/sabado-4-comprender/segunda-iteracion/mcp.json`):

```bash
claude mcp add context7 -- npx -y @upstash/context7-mcp
```

```bash
claude mcp add playwright -- npx @playwright/mcp@latest
```

Modelo local con Ollama y Open WebUI:

```bash
ollama serve
```

```bash
docker run -d -p 3000:8080 -e OLLAMA_BASE_URL=http://host.docker.internal:11434 -e WEBUI_AUTH=False -v open-webui:/app/backend/data --name open-webui ghcr.io/open-webui/open-webui:main
```

```bash
docker start open-webui
```
