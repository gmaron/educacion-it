"""API HTTP del divisor de gastos (R7, R8 y R9 de docs/especificacion.md).

Se levanta desde `src/` con `uvicorn api:app`.
"""

from decimal import Decimal
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel

from divisor_gastos import leer_monto, resumir

app = FastAPI(title="Divisor de gastos")

PAGINA = Path(__file__).parent / "index.html"


class PagoEntrada(BaseModel):
    """Un pago tal como llega: el monto es texto, con coma o con punto."""

    nombre: str
    monto: str


class Pedido(BaseModel):
    """El cuerpo de POST /dividir."""

    pagos: list[PagoEntrada]


@app.get("/")
def pagina() -> FileResponse:
    """Devuelve la página que carga los pagos y muestra el resultado (R9)."""
    return FileResponse(PAGINA, media_type="text/html")


@app.post("/dividir")
def dividir(pedido: Pedido) -> JSONResponse:
    """Devuelve las transferencias y el estado de cada persona.

    Si un dato está mal, responde 422 con el mensaje de error.
    """
    try:
        pagos = [
            (p.nombre, float(leer_monto(p.monto))) for p in pedido.pagos
        ]
        resumen = resumir(pagos)
    except ValueError as error:
        return JSONResponse({"error": str(error)}, status_code=422)
    return JSONResponse({
        "transferencias": [t._asdict() for t in resumen.transferencias],
        "personas": [
            {**p._asdict(), "puso": _numero(p.puso)} for p in resumen.personas
        ],
    })


def _numero(monto: Decimal) -> int | float:
    """1000 si es entero; 1500.5 si tiene centavos."""
    if monto == monto.to_integral_value():
        return int(monto)
    return float(monto)
