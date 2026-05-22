from dataclasses import dataclass
from decimal import Decimal


MENSAJE_PRECIO_INVALIDO = "El precio base debe ser mayor que cero."


@dataclass
class Producto:
    nombre: str
    precio_base: Decimal

    def __post_init__(self):
        precio = _a_decimal(self.precio_base)
        _validar_precio_base(precio)
        self.precio_base = precio


def _a_decimal(valor):
    return Decimal(str(valor))


def _validar_precio_base(precio):
    if precio <= Decimal("0"):
        raise ValueError(MENSAJE_PRECIO_INVALIDO)
