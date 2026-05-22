from decimal import Decimal

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


def test_acepta_descuento_minimo_de_cero_por_ciento():
    producto = Producto(nombre="Libro TDD", precio_base=50000)

    producto.aplicar_descuento(0)

    assert producto.descuento == Decimal("0")


def test_acepta_descuento_maximo_de_cuarenta_por_ciento():
    producto = Producto(nombre="Libro TDD", precio_base=50000)

    producto.aplicar_descuento(40)

    assert producto.descuento == Decimal("40")


def test_rechaza_descuento_mayor_a_cuarenta_por_ciento():
    producto = Producto(nombre="Libro TDD", precio_base=50000)

    with pytest.raises(ValueError, match="El descuento debe estar entre 0% y 40%."):
        producto.aplicar_descuento(41)


def test_rechaza_descuento_negativo():
    producto = Producto(nombre="Libro TDD", precio_base=50000)

    with pytest.raises(ValueError, match="El descuento debe estar entre 0% y 40%."):
        producto.aplicar_descuento(-1)
