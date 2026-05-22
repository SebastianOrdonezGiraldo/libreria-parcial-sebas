# Libreria Parcial Sebas

Repositorio para el parcial de Pruebas de Software.

## Parte 1 - Analisis inicial

### Particiones de equivalencia - Regla 1

La Regla 1 indica que un producto tiene nombre y precio base, pero la condicion explicita de rechazo aplica al precio base. Por eso las particiones se enfocan en ese dato.

| Regla | Particion | Valor representativo | Resultado esperado |
|---|---|---:|---|
| Precio base | Valida: precio mayor que cero | 50000 | El producto se crea correctamente. |
| Precio base | Invalida: precio igual a cero | 0 | El sistema rechaza el producto con un mensaje claro. |
| Precio base | Invalida: precio menor que cero | -1000 | El sistema rechaza el producto con un mensaje claro. |

### Particiones de equivalencia - Regla 2

| Regla | Particion | Valor representativo | Resultado esperado |
|---|---|---:|---|
| Descuento porcentual | Valida: descuento entre 0% y 40% inclusive | 20 | El descuento se acepta y puede aplicarse. |
| Descuento porcentual | Invalida: descuento menor que 0% | -1 | El sistema rechaza el descuento con un mensaje claro. |
| Descuento porcentual | Invalida: descuento mayor que 40% | 41 | El sistema rechaza el descuento con un mensaje claro. |

### Analisis de valores limite - Regla 2

| Valor de descuento | Motivo | Resultado esperado |
|---:|---|---|
| -1 | Justo fuera del limite inferior | Rechazado |
| 0 | Limite inferior permitido | Aceptado |
| 1 | Justo dentro del rango por encima del minimo | Aceptado |
| 39 | Justo dentro del rango por debajo del maximo | Aceptado |
| 40 | Limite superior permitido | Aceptado |
| 41 | Justo fuera del limite superior | Rechazado |

### Pregunta para el administrador - Regla 3

Pregunta: cuando el calculo produzca decimales, ¿el precio final debe redondearse a centavos, a pesos enteros o conservar todos los decimales?

Justificacion: sin esa regla, dos implementaciones correctas podrian dar resultados distintos por manejo de moneda y redondeo.
