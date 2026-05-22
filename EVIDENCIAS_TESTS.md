# Evidencias de ejecucion de pruebas

Fecha de verificacion local: 2026-05-22

## Pruebas unitarias y cobertura

Comando ejecutado:

```bash
.venv\Scripts\python -m pytest
```

Resultado:

```text
collected 10 items

tests\test_producto.py ..........                                        [100%]

---------- coverage: platform win32, python 3.13.5-final-0 -----------
Name                       Stmts   Miss  Cover   Missing
--------------------------------------------------------
src\libreria\__init__.py       0      0   100%
src\libreria\producto.py      42      0   100%
--------------------------------------------------------
TOTAL                         42      0   100%

============================= 10 passed in 0.13s ==============================
```

## Escenarios BDD

Comando ejecutado:

```bash
.venv\Scripts\python -m behave
```

Resultado:

```text
1 feature passed, 0 failed, 0 skipped
8 scenarios passed, 0 failed, 0 skipped
28 steps passed, 0 failed, 0 skipped, 0 undefined
```

