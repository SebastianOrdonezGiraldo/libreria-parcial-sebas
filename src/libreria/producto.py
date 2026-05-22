from dataclasses import dataclass
from decimal import Decimal


MENSAJE_PRECIO_INVALIDO = "El precio base debe ser mayor que cero."
MENSAJE_DESCUENTO_INVALIDO = "El descuento debe estar entre 0% y 40%."


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
        if descuento < Decimal("0") or descuento > Decimal("40"):
            raise ValueError(MENSAJE_DESCUENTO_INVALIDO)
        self.descuento = descuento


def _a_decimal(valor):
    return Decimal(str(valor))


def _validar_precio_base(precio):
    if precio <= Decimal("0"):
        raise ValueError(MENSAJE_PRECIO_INVALIDO)
