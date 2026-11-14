import pytest

from divisor_gastos import dividir, explicar, mostrar


def test_1_dos_personas_una_pago_todo():
    assert dividir([("Ana", 2000), ("Beto", 0)]) == [("Beto", "Ana", 1000)]


def test_2_redondeo_a_favor_del_que_pago():
    assert dividir([("Ana", 1001), ("Beto", 0)]) == [("Beto", "Ana", 501)]


def test_3_sobrante_va_al_que_mas_puso():
    assert dividir([("Ana", 1000), ("Beto", 0), ("Caro", 0)]) == [("Beto", "Ana", 334), ("Caro", "Ana", 334)]


def test_4_un_deudor_paga_a_dos():
    assert dividir([("Ana", 600), ("Beto", 400), ("Caro", 0)]) == [("Caro", "Ana", 267), ("Caro", "Beto", 67)]


def test_5_dos_deudores_dos_acreedores():
    assert dividir([("Ana", 601), ("Beto", 400), ("Caro", 0), ("Dani", 0)]) == [
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
    assert mostrar([("Ana", 1000), ("Beto", -500)]) == "Error: no se aceptan montos negativos"


def test_10_nombre_corto():
    with pytest.raises(ValueError, match="al menos 3"):
        dividir([("Al", 1000), ("Beto", 0)])


def test_11_nombres_repetidos():
    assert mostrar([("Ana", 1000), ("Ana", 0)]) == "Ana (2) le transfiere $500 a Ana (1)"


def test_11_nombres_repetidos_se_numeran_por_orden_de_carga():
    assert mostrar([("Ana", 0), ("Beto", 900), ("Ana", 0)]) == (
        "Ana (1) le transfiere $300 a Beto\nAna (2) le transfiere $300 a Beto"
    )


def test_explicar_muestra_las_cuentas_y_el_redondeo():
    assert explicar([("Ana", 1000), ("Beto", 0), ("Caro", 0)]) == (
        "Entre todos pusieron $1000.\n"
        "Son 3 personas: a cada una le toca $1000 / 3 = $333,33.\n"
        "\n"
        "  Ana puso $1000: le devuelven $1000 - $333,33 = $666,67, redondeado para arriba: $667.\n"
        "  Beto puso $0: debe $333,33 - $0 = $333,33, redondeado para arriba: $334.\n"
        "  Caro puso $0: debe $333,33 - $0 = $333,33, redondeado para arriba: $334.\n"
        "\n"
        "Los centavos se redondean para arriba, a favor de quien pagó.\n"
        "Por el redondeo se juntan $1 de más: van a Ana, que es quien más puso, y recibe $668 en total.\n"
        "\n"
        "Beto le transfiere $334 a Ana\n"
        "Caro le transfiere $334 a Ana"
    )
