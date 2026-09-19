import pytest
from main import Calculator


def test_sums_2_numbers():
    assert Calculator().suma(2, 2) == 4


def test_resta_2_numbers():
    assert Calculator().resta(5, 3) == 2


def test_multiplicacion_2_numbers():
    assert Calculator().multiplicacion(3, 4) == 12


def test_division_2_numbers():
    assert Calculator().division(10, 2) == 5.0


def test_division_por_cero():
    with pytest.raises(ValueError, match="No se puede dividir por cero"):
        Calculator().division(10, 0)


def test_historial_operaciones():
    calc = Calculator()
    calc.suma(5, 5)
    calc.resta(10, 4)
    calc.multiplicacion(2, 3)
    calc.division(8, 2)

    historial = calc.obtener_historial()
    assert len(historial) == 4
    assert historial[0] == "5 + 5 = 10"
    assert historial[1] == "10 - 4 = 6"
    assert historial[2] == "2 * 3 = 6"
    assert historial[3] == "8 / 2 = 4.0"


def test_limpiar_historial():
    calc = Calculator()
    calc.suma(1, 1)
    assert len(calc.obtener_historial()) == 1
    calc.limpiar_historial()
    assert calc.obtener_historial() == []
