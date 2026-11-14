"""Tests de la API: un test por cada caso de la sección API (C17 a C19)."""

from fastapi.testclient import TestClient


def _cliente():
    """Devuelve un cliente de prueba para la app de `api.py`."""
    from api import app

    return TestClient(app)


def _pagos(*pagos):
    """Arma el cuerpo de POST /dividir a partir de pares (nombre, monto)."""
    return {"pagos": [{"nombre": n, "monto": m} for n, m in pagos]}


def test_17_dos_personas_transferencias_y_estados():
    """C17: Ana 1000 y Beto 0."""
    pagos = _pagos(("Ana", "1000"), ("Beto", "0"))
    respuesta = _cliente().post("/dividir", json=pagos)

    assert respuesta.status_code == 200
    assert respuesta.json() == {
        "transferencias": [
            {"quien_paga": "Beto", "a_quien": "Ana", "monto": 500},
        ],
        "personas": [
            {"nombre": "Ana", "puso": 1000, "estado": "recibe", "saldo": 500},
            {"nombre": "Beto", "puso": 0, "estado": "debe", "saldo": 500},
        ],
    }


def test_18_quien_esta_a_mano():
    """C18: Ana 1000, Beto 500 y Caro 0."""
    pagos = _pagos(("Ana", "1000"), ("Beto", "500"), ("Caro", "0"))
    respuesta = _cliente().post("/dividir", json=pagos)

    assert respuesta.status_code == 200
    cuerpo = respuesta.json()
    assert cuerpo["transferencias"] == [
        {"quien_paga": "Caro", "a_quien": "Ana", "monto": 500},
    ]
    beto = next(p for p in cuerpo["personas"] if p["nombre"] == "Beto")
    assert beto["estado"] == "a_mano"
    assert beto["saldo"] == 0


def test_19_monto_que_no_es_numero():
    """C19: Ana mil y Beto 0."""
    pagos = _pagos(("Ana", "mil"), ("Beto", "0"))
    respuesta = _cliente().post("/dividir", json=pagos)

    assert respuesta.status_code == 422
    assert respuesta.json() == {"error": "el monto tiene que ser un número"}
