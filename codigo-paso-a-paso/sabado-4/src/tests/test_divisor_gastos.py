import subprocess
import sys
from decimal import Decimal
from pathlib import Path

import pytest

from divisor_gastos import (
    dividir,
    explicar,
    explicar_con_colores,
    leer_monto,
    mostrar,
)


def test_1_dos_personas_una_pago_todo():
    assert dividir([("Ana", 2000), ("Beto", 0)]) == [("Beto", "Ana", 1000)]


def test_2_redondeo_a_favor_del_que_pago():
    assert dividir([("Ana", 1001), ("Beto", 0)]) == [("Beto", "Ana", 501)]


def test_3_el_sobrante_va_al_que_mas_puso():
    assert dividir([("Ana", 1000), ("Beto", 0), ("Caro", 0)]) == [
        ("Beto", "Ana", 334),
        ("Caro", "Ana", 334),
    ]


def test_4_un_deudor_paga_a_dos():
    assert dividir([("Ana", 600), ("Beto", 400), ("Caro", 0)]) == [
        ("Caro", "Ana", 267),
        ("Caro", "Beto", 67),
    ]


def test_5_dos_deudores_dos_acreedores():
    pagos = [("Ana", 601), ("Beto", 400), ("Caro", 0), ("Dani", 0)]
    assert dividir(pagos) == [
        ("Caro", "Ana", 251),
        ("Dani", "Ana", 101),
        ("Dani", "Beto", 150),
    ]


def test_6_una_sola_persona():
    assert mostrar([("Ana", 1000)]) == "Están a mano"


def test_7_todos_en_cero():
    assert mostrar([("Ana", 0), ("Beto", 0), ("Caro", 0)]) == "Están a mano"


def test_8_todos_pusieron_lo_mismo():
    assert mostrar([("Ana", 500), ("Beto", 500)]) == "Están a mano"


def test_9_monto_negativo():
    with pytest.raises(ValueError, match="negativos"):
        dividir([("Ana", 1000), ("Beto", -500)])
    assert mostrar([("Ana", 1000), ("Beto", -500)]) == (
        "Error: no se aceptan montos negativos"
    )


def test_10_nombre_corto():
    with pytest.raises(ValueError, match="al menos 3"):
        dividir([("Al", 1000), ("Beto", 0)])


def test_11_nombres_repetidos():
    assert mostrar([("Ana", 1000), ("Ana", 0)]) == (
        "Ana (2) le transfiere $500 a Ana (1)"
    )


def test_11_nombres_repetidos_se_numeran_por_orden_de_carga():
    assert mostrar([("Ana", 0), ("Beto", 900), ("Ana", 0)]) == (
        "Ana (1) le transfiere $300 a Beto\nAna (2) le transfiere $300 a Beto"
    )


def test_12_monto_con_coma():
    assert leer_monto("1500,50") == Decimal("1500.50")
    assert leer_monto("1500.50") == Decimal("1500.50")
    pagos = [("Ana", leer_monto("1500,50")), ("Beto", leer_monto("0"))]
    assert dividir(pagos) == [("Beto", "Ana", 751)]


def test_13_monto_que_no_es_un_numero():
    with pytest.raises(ValueError, match="el monto tiene que ser un número"):
        leer_monto("mil")


def test_13_el_programa_muestra_el_error_y_no_calcula():
    resultado = subprocess.run(
        [sys.executable, Path(__file__).parents[1] / "divisor_gastos.py"],
        input="Ana mil\nBeto 0\n\n",
        capture_output=True,
        text=True,
    )
    assert "Error: el monto tiene que ser un número" in resultado.stdout
    assert "transfiere" not in resultado.stdout


def test_explicar_muestra_las_cuentas_y_el_redondeo():
    assert explicar([("Ana", 1000), ("Beto", 0), ("Caro", 0)]) == (
        "Entre todos pusieron $1000.\n"
        "Son 3 personas: a cada una le toca $1000 / 3 = $333,33.\n"
        "\n"
        "  Ana puso $1000: le devuelven $1000 - $333,33 = $666,67, "
        "redondeado para arriba: $667.\n"
        "  Beto puso $0: debe $333,33 - $0 = $333,33, "
        "redondeado para arriba: $334.\n"
        "  Caro puso $0: debe $333,33 - $0 = $333,33, "
        "redondeado para arriba: $334.\n"
        "\n"
        "Los centavos se redondean para arriba, a favor de quien pagó.\n"
        "Por el redondeo se juntan $1 de más: van a Ana, "
        "que es quien más puso, y recibe $668 en total.\n"
        "\n"
        "Beto le transfiere $334 a Ana\n"
        "Caro le transfiere $334 a Ana"
    )


def test_14_los_que_deben_en_rojo_y_los_que_reciben_en_verde():
    resultado = explicar_con_colores([("Ana", 1000), ("Beto", 0)])
    assert "  \U0001f7e9 \033[32mAna\033[0m puso $1000: le dev" in resultado
    assert "  \U0001f7e5 \033[31mBeto\033[0m puso $0: debe" in resultado


def test_14_las_transferencias_van_sin_color():
    pagos = [("Ana", 1000), ("Beto", 500), ("Caro", 0)]
    resultado = explicar_con_colores(pagos)
    assert "\U0001f91d" not in resultado.splitlines()[-1]
    assert resultado.endswith("Caro le transfiere $500 a Ana")


def test_14_sin_los_colores_el_texto_es_el_de_siempre():
    pagos = [("Ana", 1000), ("Beto", 500), ("Caro", 0)]
    texto = explicar_con_colores(pagos)
    marcas = (
        "\033[31m", "\033[32m", "\033[0m",
        "\U0001f7e5 ", "\U0001f7e9 ", "\U0001f91d ",
    )
    for marca in marcas:
        texto = texto.replace(marca, "")
    assert texto == explicar(pagos)


def test_15_cada_persona_lleva_el_mismo_color_en_el_cuadrito_y_en_el_nombre():
    pagos = [("Ana", 1000), ("Beto", 500), ("Caro", 0)]
    lineas = explicar_con_colores(pagos).splitlines()
    assert "  \U0001f7e9 \033[32mAna\033[0m puso $1000" in lineas[3]
    assert lineas[4].startswith("  \U0001f91d Beto puso $500: está a mano")
    assert "  \U0001f7e5 \033[31mCaro\033[0m puso $0" in lineas[5]


def test_16_quien_esta_a_mano_lleva_el_apreton_de_manos_sin_color():
    pagos = [("Ana", 1000), ("Beto", 500), ("Caro", 0)]
    resultado = explicar_con_colores(pagos)
    assert "  \U0001f91d Beto puso $500: está a mano." in resultado
    transferencias = resultado.split("\n\n")[-1]
    assert "\U0001f91d" not in transferencias
    assert "\033[" not in transferencias
