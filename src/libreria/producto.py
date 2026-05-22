from dataclasses import dataclass


@dataclass
class Producto:
    nombre: str
    precio_base: float

    def __post_init__(self):
        if self.precio_base <= 0:
            raise ValueError("El precio base debe ser mayor que cero.")
