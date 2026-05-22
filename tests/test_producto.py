import pytest

from libreria.producto import Producto


def test_crea_producto_con_precio_base_mayor_que_cero():
    producto = Producto(nombre="Libro TDD", precio_base=50000)

    assert producto.nombre == "Libro TDD"
    assert producto.precio_base == 50000


def test_rechaza_producto_con_precio_base_igual_a_cero():
    with pytest.raises(ValueError, match="El precio base debe ser mayor que cero."):
        Producto(nombre="Cuaderno", precio_base=0)


def test_rechaza_producto_con_precio_base_negativo():
    with pytest.raises(ValueError, match="El precio base debe ser mayor que cero."):
        Producto(nombre="Agenda", precio_base=-1000)
