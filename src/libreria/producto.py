from dataclasses import dataclass
from decimal import Decimal


MENSAJE_PRECIO_INVALIDO = "El precio base debe ser mayor que cero."
MENSAJE_DESCUENTO_INVALIDO = "El descuento debe estar entre 0% y 40%."
DESCUENTO_MINIMO = Decimal("0")
DESCUENTO_MAXIMO = Decimal("40")
IVA = Decimal("0.19")
CIEN = Decimal("100")
CENTAVO = Decimal("0.01")


@dataclass
class Producto:
    nombre: str
    precio_base: Decimal
    descuento: Decimal = Decimal("0")

    def __post_init__(self):
        precio = _a_decimal(self.precio_base)
        _validar_precio_base(precio)
        self.precio_base = precio

    def aplicar_descuento(self, descuento):
        descuento = _a_decimal(descuento)
        _validar_descuento(descuento)
        self.descuento = descuento

    def calcular_precio_final(self):
        precio_con_descuento = self.precio_base * (Decimal("1") - self.descuento / CIEN)
        precio_con_iva = precio_con_descuento * (Decimal("1") + IVA)
        precio_final = max(precio_con_iva, Decimal("0"))
        return precio_final.quantize(CENTAVO)


def _a_decimal(valor):
    return Decimal(str(valor))


def _validar_precio_base(precio):
    if precio <= Decimal("0"):
        raise ValueError(MENSAJE_PRECIO_INVALIDO)


def _validar_descuento(descuento):
    if descuento < DESCUENTO_MINIMO or descuento > DESCUENTO_MAXIMO:
        raise ValueError(MENSAJE_DESCUENTO_INVALIDO)
