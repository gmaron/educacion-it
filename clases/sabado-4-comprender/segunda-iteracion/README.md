# Segunda iteración: cuando el proyecto crece

Ejemplos para mostrar en el cierre del sábado 4. No se instalan en clase: cada uno entra cuando aparece el problema que resuelve, y se mide antes.

| Herramienta | Problema que resuelve | Cómo se ve |
|---|---|---|
| graphify | El repo es tan grande que el agente gasta contexto buscando | `uv tool install graphifyy && graphify install`, después `/graphify .` en Claude Code. Deja `graphify-out/` con el grafo y un `GRAPH_REPORT.md` que el agente consulta antes de leer archivos. Medir con `/context` antes y después: en un repo de tres archivos ahorra casi nada |
| Context7 (MCP) | El agente escribe con la versión vieja de una librería (Streamlit, FastAPI) | `claude mcp add context7 -- npx -y @upstash/context7-mcp`. Se le pide "usá context7" y trae la documentación actual |
| Playwright (MCP) | Nadie prueba la pantalla: pytest no ve el front (H8 [NO COMPROBABLE]) | `claude mcp add playwright -- npx @playwright/mcp@latest`. El agente abre el navegador, carga los pagos y mira el resultado |
| `claude -p` en GitHub Actions | La revisión depende de que alguien se acuerde de pedirla | `revisar-pr.yml`: en cada PR corre el subagente revisor y deja la tabla en el resumen del job. La versión oficial es `anthropics/claude-code-action@v1` (`/install-github-app`) |

`mcp.json` es el `.mcp.json` equivalente a los dos `claude mcp add`, para commitearlo en el proyecto. `revisar-pr.yml` va en `.github/workflows/` y necesita el secreto `ANTHROPIC_API_KEY` en el repo.
