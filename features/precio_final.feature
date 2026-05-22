Feature: Calculo de precios para la Libreria del Centro
  Como administrador de la libreria
  quiero aplicar descuentos controlados y calcular el precio final con IVA
  para vender productos con reglas claras y verificables.

  Background:
    Given existe un producto "Libro TDD" con precio base 100000

  @descuento @borde
  Scenario Outline: Aceptar descuentos validos en los bordes
    When aplico un descuento de <descuento> por ciento
    Then el descuento del producto debe ser <descuento> por ciento

    Examples:
      | descuento |
      | 0         |
      | 40        |

  @descuento @error
  Scenario: Rechazar un descuento superior al permitido
    When intento aplicar un descuento de 41 por ciento
    Then el sistema debe rechazar la operacion con el mensaje "El descuento debe estar entre 0% y 40%."

  @descuento @error
  Scenario: Rechazar un descuento negativo
    When intento aplicar un descuento de -1 por ciento
    Then el sistema debe rechazar la operacion con el mensaje "El descuento debe estar entre 0% y 40%."

  @precio_final @calculo
  Scenario Outline: Calcular precio final aplicando descuento antes del IVA
    When aplico un descuento de <descuento> por ciento
    And calculo el precio final
    Then el precio final debe ser <precio_final>

    Examples:
      | descuento | precio_final |
      | 10        | 107100.00    |
      | 0         | 119000.00    |
      | 40        | 71400.00     |

  @precio_final @borde
  Scenario: Mantener el precio final no negativo con descuento maximo
    When aplico un descuento de 40 por ciento
    And calculo el precio final
    Then el precio final no debe ser negativo

