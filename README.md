# Ingeniería de Software con IA y Coding Agents

Material de práctica del curso de EducaciónIT (comisión 86388). Son cuatro sábados, de 10:00 a 13:00 (hora de Argentina), del 24/10 al 14/11/2026.

> **Hacer software con criterio.** La IA escribe código rápido. El criterio lo ponés vos: saber qué pedir, comprobar que lo que devuelve está bien y poder explicar lo que tenés.

| Sábado | Pilar | Qué hacés |
| --- | --- | --- |
| 1 · 24/10 | Planificar | Escribís la especificación del divisor de gastos, con casos y resultados esperados |
| 2 · 31/10 | Construir | Un agente construye tu app a partir de la especificación |
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
  plantilla-especificacion.md       La plantilla que completás en pareja
  ejemplo-especificacion-pomodoro.md  Un ejemplo bien hecho
  pomodoro/index.html               Un pomodoro hecho con un prompt vago, para leer
  explicar-codigo.md                Prompts para que la IA te explique código, de menos a más
divisor/
  divisor.py                        La función que tenés que escribir
  tests/test_divisor.py             Los casos de tu especificación, como tests
```

## Las apps del curso

El sábado 1 todos especifican el **divisor de gastos**. Desde el sábado 2, cada uno construye una app de esta lista:

1. **Divisor de gastos:** quién le debe a quién después de una salida.
2. **Registro de gastos personales:** cuánto gastaste por categoría y por mes.
3. **Propinas y cuotas:** cuánto paga cada uno, o cada mes con interés.
4. **Promedio de notas:** si aprobás, recuperás o promocionás.
5. **Conversor de recetas:** escalar porciones y convertir unidades.
6. **Control de stock:** qué falta y cuándo hay que reponer.

Si elegís otra que no sea el divisor, escribís su especificación con la misma plantilla.

## Cómo trabajar con este repo

Hacé un fork o clonalo y trabajá en tu copia. No hace falta mandar cambios a este repo.
