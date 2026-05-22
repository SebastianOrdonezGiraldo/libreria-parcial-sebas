from decimal import Decimal

from behave import given, then, when

from libreria.producto import Producto


@given('existe un producto "{nombre}" con precio base {precio_base:g}')
def step_producto_valido(context, nombre, precio_base):
    context.producto = Producto(nombre=nombre, precio_base=precio_base)
    context.error = None
    context.precio_final = None


@when("aplico un descuento de {descuento:g} por ciento")
def step_aplicar_descuento(context, descuento):
    context.producto.aplicar_descuento(descuento)


@when("intento aplicar un descuento de {descuento:g} por ciento")
def step_intentar_descuento(context, descuento):
    try:
        context.producto.aplicar_descuento(descuento)
    except ValueError as error:
        context.error = error


@when("calculo el precio final")
def step_calcular_precio_final(context):
    context.precio_final = context.producto.calcular_precio_final()


@then("el descuento del producto debe ser {descuento:g} por ciento")
def step_validar_descuento(context, descuento):
    assert context.producto.descuento == Decimal(str(descuento))


@then('el sistema debe rechazar la operacion con el mensaje "{mensaje}"')
def step_validar_error(context, mensaje):
    assert context.error is not None
    assert str(context.error) == mensaje


@then("el precio final debe ser {precio_final}")
def step_validar_precio_final(context, precio_final):
    assert context.precio_final == Decimal(precio_final)


@then("el precio final no debe ser negativo")
def step_validar_precio_final_no_negativo(context):
    assert context.precio_final >= Decimal("0")
