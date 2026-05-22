# Seccion teorica

## Preguntas de seleccion multiple

### SM-1

Respuesta correcta: C.

### SM-2

Respuesta correcta: B.



## Preguntas abiertas

### PA-1
En TDD, el paso Green consiste en hacer el cambio más pequeño para que la prueba pase. No se trata de escribir mal código, sino de no adelantarse a problemas que todavía no están probados. Primero confirmo el comportamiento y después, en Refactor, mejoro el diseño con la seguridad de los tests.

### PA-2

TDD ayuda a construir código con pruebas pequeñas y concretas, escribiendo solo lo necesario y mejorando el diseño con seguridad. BDD, en cambio, sirve para acordar el comportamiento esperado usando un lenguaje más cercano al negocio y al usuario. No se reemplazan: BDD define qué debe pasar y TDD ayuda a construir cómo hacerlo bien.

### PA-3

Tener 95% de cobertura no significa que no haya bugs. La cobertura solo muestra que las pruebas ejecutaron mucho código, pero no que hayan verificado bien los resultados. Sirve para detectar zonas sin probar, pero no demuestra que el sistema esté correcto ni que cubra reglas de negocio o casos límite.


### PA-4

Probar solo el 20% es débil porque está en medio del rango y no revisa los límites. Yo probaría **0 y 40** como valores válidos extremos, y **-1 y 41** como inválidos fuera del rango. También usaría **20** como caso normal. Así no pruebo solo un ejemplo cómodo, sino particiones y bordes donde suelen aparecer errores.


### PA-5

TDD y BDD ayudan a tener una suite automatizada que se puede ejecutar en cada push o merge. TDD detecta fallos técnicos cerca del código, mientras BDD valida reglas de negocio completas. Para mí, CI/CD sin buenos tests solo mueve código más rápido, pero no garantiza calidad; incluso puede propagar errores más rápido.

