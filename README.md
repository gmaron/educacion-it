# Ingeniería de Software con IA y Coding Agents

Material de práctica del curso de EducaciónIT (comisión 86388). Son cuatro sábados, de 10:00 a 13:00 (hora de Argentina), del 24/10 al 14/11/2026.

> **Hacer software con criterio.** La IA escribe código rápido. El criterio lo ponés vos: saber qué pedir, comprobar que lo que devuelve está bien y poder explicar lo que tenés.

| Sábado | Pilar | Qué hacés |
| --- | --- | --- |
| 1 · 24/10 | Planificar | Escribís la especificación del divisor de gastos, con casos y resultados esperados |
| 2 · 31/10 | Construir | Un agente construye la app votada a partir de tu especificación |
| 3 · 07/11 | Verificar | Los casos de la especificación se convierten en tests |
| 4 · 14/11 | Comprender | Explicás tu código sin ayuda |

## Puesta en marcha

Necesitás Git, Python 3.11 o más nuevo y una cuenta sin costo en [Claude.ai](https://claude.ai) o [Gemini](https://gemini.google.com).

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
sabado-1/
  README.md                         La consigna del sábado 1
  plantilla-especificacion.md       La plantilla de la especificación
  ejemplo-especificacion-pomodoro.md  Un ejemplo bien hecho
  pomodoro/index.html               Un pomodoro hecho con un prompt vago, para leer
  explicar-codigo.md                Prompts para que la IA te explique código, de menos a más
  subir-tu-especificacion.md        Cómo mandar tu especificación con un pull request
alumnos/
  README.md                         La lista de la cursada: cada uno agrega su línea
  <tu-usuario>/                     Tu carpeta: acá va tu especificación
divisor/
  divisor.py                        La función que tenés que escribir
  tests/test_divisor.py             Los casos de tu especificación, como tests
```

## El proyecto del curso

El sábado 1 todos especifican el **divisor de gastos**. Al cierre votamos entre todos qué app construimos los sábados 2, 3 y 4. Gana una: todos hacemos la misma, cada uno la suya.

1. **Divisor de gastos:** quién le debe a quién después de una salida.
2. **Registro de gastos personales:** cuánto gastaste por categoría y por mes, guardado en un archivo CSV.
3. **Plan de estudio:** el promedio y la condición de cada materia (promociona, regulariza o recursa) y cuánto de la carrera llevás aprobado.

Si gana otra que no sea el divisor, esa semana cada uno escribe su especificación con la misma plantilla.

## Cómo trabajar con este repo

Este repo es para jugar con Git y con GitHub. El que quiera, participa; no es obligatorio.

1. Hacé un **fork**: tu copia del repo, en tu cuenta. Ahí podés crear branches, romper y rehacer lo que quieras.
2. Trabajá **solo en tu carpeta**, `alumnos/<tu-usuario-de-github>/`. Así tus cambios no se pisan con los de nadie.
3. Cuando quieras compartir algo, abrí un **pull request** (PR) hacia este repo. Gastón comenta algunos PRs y elige casos para devolver en clase.
4. Revisá el PR de otra persona: elegí 2 casos de su especificación, calculá el resultado sin preguntar y dejalo como comentario.

El paso a paso, desde el navegador o desde la terminal, está en [`sabado-1/subir-tu-especificacion.md`](sabado-1/subir-tu-especificacion.md).

**El repo es público.** Lo que subas, incluido tu usuario de GitHub, lo ve cualquiera. No subas datos personales.
