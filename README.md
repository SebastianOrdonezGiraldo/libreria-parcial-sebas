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

## Parte 2 - Casos de prueba

| ID | Regla | Descripcion | Precondicion | Datos de entrada | Pasos | Resultado esperado | Tipo |
|---|---|---|---|---|---|---|---|
| TC-01 | Regla 1 | Crear un producto con precio base valido | No existe producto creado | Nombre: "Libro TDD"; precio base: 50000 | Crear el producto | El producto queda creado con nombre y precio base | Positivo |
| TC-02 | Regla 1 | Rechazar precio base igual a cero | No existe producto creado | Nombre: "Cuaderno"; precio base: 0 | Intentar crear el producto | Se lanza un error con el mensaje "El precio base debe ser mayor que cero." | Borde |
| TC-03 | Regla 1 | Rechazar precio base negativo | No existe producto creado | Nombre: "Agenda"; precio base: -1000 | Intentar crear el producto | Se lanza un error con el mensaje "El precio base debe ser mayor que cero." | Negativo |
| TC-04 | Regla 2 | Aceptar descuento minimo permitido | Existe un producto valido | Descuento: 0 | Aplicar descuento | El descuento se guarda como 0% | Borde |
| TC-05 | Regla 2 | Aceptar descuento maximo permitido | Existe un producto valido | Descuento: 40 | Aplicar descuento | El descuento se guarda como 40% | Borde |
| TC-06 | Regla 2 | Rechazar descuento mayor al maximo | Existe un producto valido | Descuento: 41 | Intentar aplicar descuento | Se lanza un error con el mensaje "El descuento debe estar entre 0% y 40%." | Negativo |
| TC-07 | Regla 2 | Rechazar descuento negativo | Existe un producto valido | Descuento: -1 | Intentar aplicar descuento | Se lanza un error con el mensaje "El descuento debe estar entre 0% y 40%." | Negativo |
| TC-08 | Regla 3 | Calcular precio final con descuento intermedio | Existe un producto valido | Precio base: 100000; descuento: 10 | Aplicar descuento y calcular precio final | El precio final es 107100.00 | Positivo |
| TC-09 | Regla 3 | Calcular precio final con descuento de 0% | Existe un producto valido | Precio base: 100000; descuento: 0 | Aplicar descuento y calcular precio final | El precio final es 119000.00 | Borde |
| TC-10 | Regla 3 | Calcular precio final con descuento de 40% | Existe un producto valido | Precio base: 100000; descuento: 40 | Aplicar descuento y calcular precio final | El precio final es 71400.00 y no es negativo | Borde |

## Ejecucion de pruebas

Instalar dependencias:

```bash
python -m venv .venv
.venv\Scripts\python -m pip install -r requirements-dev.txt
```

Ejecutar pruebas unitarias con cobertura:

```bash
.venv\Scripts\python -m pytest
```

Output de cobertura:

```text
============================= test session starts =============================
platform win32 -- Python 3.13.5, pytest-8.3.4, pluggy-1.6.0
rootdir: C:\Users\sebas\Desktop\libreria-parcial-sebas
configfile: pyproject.toml
testpaths: tests
plugins: cov-6.0.0
collected 10 items

tests\test_producto.py ..........                                        [100%]

---------- coverage: platform win32, python 3.13.5-final-0 -----------
Name                       Stmts   Miss  Cover   Missing
--------------------------------------------------------
src\libreria\__init__.py       0      0   100%
src\libreria\producto.py      42      0   100%
--------------------------------------------------------
TOTAL                         42      0   100%

============================= 10 passed in 0.10s ==============================
```

Ejecutar escenarios BDD:

```bash
.venv\Scripts\python -m behave
```
