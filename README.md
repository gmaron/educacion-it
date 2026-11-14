# Ingeniería de Software con IA y Coding Agents

Material de práctica del curso de EducaciónIT (comisión 86388). Son cuatro sábados, de 10:00 a 13:00 (hora de Argentina), del 24/10 al 14/11/2026.

> **Hacer software con criterio.** La IA escribe código rápido. El criterio lo ponés vos: saber qué pedir, comprobar que lo que devuelve está bien y poder explicar lo que tenés.

| Sábado | Pilar | Qué hacés |
| --- | --- | --- |
| 1 · 24/10 | Planificar | Escribís la especificación del divisor de gastos, con casos y resultados esperados |
| 2 · 31/10 | Construir | Un agente construye tu divisor a partir de tu especificación, con un setup que armás paso a paso |
| 3 · 07/11 | Verificar | El agente no puede dar por terminado algo que no pase los casos de tu especificación |
| 4 · 14/11 | Comprender | Explicás sin ayuda tu código y tu setup |

## Todo el material del curso

- **[`clases/`](clases/):** la presentación en PDF y los prompts de cada sábado, en el orden de la clase.
- **[`codigo-paso-a-paso/`](codigo-paso-a-paso/):** el divisor del docente al final de cada sábado, con sus skills, hooks y plugin.
- **Todo en un .zip:** en [Releases](https://github.com/gmaron/educacion-it/releases), el archivo `material-curso.zip`.

## Puesta en marcha

Necesitás Git, Python 3.11 o más nuevo y [Claude Code](https://docs.claude.com/en/docs/claude-code/overview). Si usás Codex, también sirve: lee los `AGENTS.md`.

```bash
git clone https://github.com/gmaron/educacion-it.git
cd educacion-it
python -m venv .venv
source .venv/bin/activate      # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest
```

El test falla. Está bien que falle: la función del divisor todavía no existe. Escribirla, con ayuda de la IA y contra tu especificación, es la práctica.

## Qué hay

```
AGENTS.md                           Las reglas del curso para el agente (las leen Claude Code y Codex)
ruff.toml                           El estilo del curso: PEP 8 y docstrings (se corre con `ruff check`)
sabado-1/
  README.md                         La consigna del sábado 1
  plantilla-especificacion.md       La plantilla de la especificación
  ejemplo-especificacion-pomodoro.md  Un ejemplo bien hecho
  pomodoro/index.html               Un pomodoro hecho con un prompt vago, para leer
  explicar-codigo.md                Prompts para que la IA te explique código, de menos a más
  subir-tu-especificacion.md        Cómo mandar tu especificación con un pull request
sabado-3/
  README.md                         La consigna del sábado 3: la auditoría, los hooks, la API y el loop
  skills/auditar/SKILL.md           La skill que audita tu especificación, para copiar a tu carpeta
  skills/explicar/SKILL.md          La skill que corrige tu explicación de una función
  hooks/                            Hooks y settings.json de referencia (ajustá las rutas a tu carpeta)
clases/                             El material de los cuatro sábados: la presentación en PDF y los prompts de cada clase
codigo-paso-a-paso/                 El divisor del docente como quedó al final de cada sábado, para comparar con el tuyo
alumnos/
  README.md                         La lista de la cursada: cada uno agrega su línea
  <tu-usuario>/                     Tu carpeta: acá va tu especificación
divisor/
  divisor.py                        La función que tenés que escribir
  tests/test_divisor.py             Los casos de tu especificación, como tests
```

## El proyecto del curso

El sábado 1 todos especificaron el **divisor de gastos**: quién le debe a quién después de una salida. En la votación del cierre ganó el divisor, así que es la app de los sábados 2, 3 y 4. Todos hacemos la misma, cada uno la suya, a partir de su especificación.

## Trabajar con el agente

Abrí Claude Code **desde tu carpeta**, no desde la raíz del repo:

```bash
cd alumnos/<tu-usuario-de-github>
claude
```

Desde ahí, el agente lee el `AGENTS.md` de la raíz, con las reglas del curso, y el `CLAUDE.md` de tu carpeta, con las de tu proyecto. También toma tus hooks y tus skills de `alumnos/<tu-usuario>/.claude/`. Si lo abrís desde la raíz, tus skills no aparecen.

Tu configuración personal (`settings.local.json`, `CLAUDE.local.md`) no se sube: está en el `.gitignore`.

## Cómo trabajar con este repo

Este repo es para jugar con Git y con GitHub. El que quiera, participa; no es obligatorio.

1. Hacé un **fork**: tu copia del repo, en tu cuenta. Ahí podés crear branches, romper y rehacer lo que quieras.
2. Trabajá **solo en tu carpeta**, `alumnos/<tu-usuario-de-github>/`. Así tus cambios no se pisan con los de nadie.
3. Cuando quieras compartir algo, abrí un **pull request** (PR) hacia este repo. Gastón comenta algunos PRs y elige casos para devolver en clase.
4. Revisá el PR de otra persona: elegí 2 casos de su especificación, calculá el resultado sin preguntar y dejalo como comentario.

El paso a paso, desde el navegador o desde la terminal, está en [`sabado-1/subir-tu-especificacion.md`](sabado-1/subir-tu-especificacion.md).

**El repo es público.** Lo que subas, incluido tu usuario de GitHub, lo ve cualquiera. No subas datos personales.
