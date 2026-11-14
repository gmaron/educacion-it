# Código paso a paso

El divisor de gastos del docente, como quedó al final de cada sábado. Es la misma carpeta (`alumnos/gmaron/`) en cuatro momentos: comparalas para ver qué agregó cada clase.

| Carpeta | Al final del | Qué hay de nuevo | Tests |
| --- | --- | --- | --- |
| [`sabado-1/`](sabado-1/) | Sábado 1 · Planificar | La especificación (`especificacion.md`), el divisor (`divisor_gastos.py`) y sus casos como tests | 13 |
| [`sabado-2/`](sabado-2/) | Sábado 2 · Construir | La memoria del proyecto (`CLAUDE.md`), `docs/` con especificación, historias, plan y `HANDOFF.md`, el código en `src/`, las skills `explicar` y `handoff`, y Spec Kit (`.specify/` y las skills `speckit-*`) | 21 |
| [`sabado-3/`](sabado-3/) | Sábado 3 · Verificar | La skill `auditar`, los hooks que protegen los tests (`PreToolUse`) y no dejan terminar con tests o ruff fallando (`Stop`), la API (`src/api.py`) con sus tests y la pantalla del asado (`src/index.html`) | 24 |
| [`sabado-4/`](sabado-4/) | Sábado 4 · Comprender | `concatenar.py` (el laboratorio del Módulo 3) y el setup empaquetado como plugin (`plugin/`) | 24 |

El plugin de referencia completo, con el subagente revisor y el hook `PostToolUse`, está en [`clases/sabado-4-comprender/plugin-referencia/`](../clases/sabado-4-comprender/plugin-referencia/).

## Correrlo

Desde la raíz del repo, con el entorno del curso:

```bash
python -m venv .venv
source .venv/bin/activate      # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Después entrá a la carpeta del sábado que quieras ver:

```bash
cd codigo-paso-a-paso/sabado-3
pytest -q
ruff check .
```

Para ver la pantalla del asado (sábados 3 y 4), levantá la API y abrí http://127.0.0.1:8000:

```bash
uvicorn api:app --app-dir src
```

## Para comparar dos sábados

En VS Code: clic derecho en una carpeta → **Select for Compare**, y clic derecho en la otra → **Compare with Selected**. Desde la terminal:

```bash
diff -r codigo-paso-a-paso/sabado-2 codigo-paso-a-paso/sabado-3 -x '.specify' -x 'speckit-*'
```

## Si abrís Claude Code acá

Cada carpeta tiene su `.claude/` con las skills y los hooks de ese momento, así que funciona igual que en tu carpeta de `alumnos/`: abrí `claude` desde adentro de la carpeta del sábado. Los hooks buscan el entorno en `../../.venv`, que desde acá es el `.venv` de la raíz del repo.

Es el proyecto del docente: los nombres (`gmaron`, `setup-gmaron`) y las decisiones de la especificación son suyos. Úsalo para comparar con el tuyo, no para copiarlo.
