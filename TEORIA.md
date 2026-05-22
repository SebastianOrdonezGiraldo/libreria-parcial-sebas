# Seccion teorica

## Preguntas de seleccion multiple

### SM-1

Respuesta correcta: C.

### SM-2

Respuesta correcta: B.



## Preguntas abiertas

### PA-1

En TDD el paso Green busca pasar del rojo al verde con el cambio mas pequeno que pruebe la idea.  
La razon no es escribir codigo malo por gusto, sino evitar resolver problemas que todavia no estan demostrados por una prueba.  
Si el desarrollador intenta dejar todo limpio y completo desde el primer Green, puede mezclar implementacion, diseno y suposiciones no verificadas.  
Eso debilita el ciclo porque ya no sabe si el codigo existe por una necesidad real o por una intuicion anticipada.  
El orden correcto permite primero confirmar comportamiento y luego mejorar estructura en Refactor con la proteccion de los tests.  
Asi el diseno aparece de forma incremental, no como una apuesta grande hecha al inicio.

### PA-2

TDD ayuda principalmente al desarrollador a construir codigo guiado por pruebas pequenas y concretas.  
Su problema central es tecnico: escribir solo el codigo necesario, detectar regresiones y mejorar el diseno con seguridad.  
BDD se enfoca mas en alinear el comportamiento esperado con el lenguaje del negocio y con las personas que entienden la necesidad.  
Por eso sus escenarios suelen expresar ejemplos de uso, reglas y resultados visibles para el usuario, no detalles internos.  
No se reemplazan porque miran niveles distintos del mismo producto: TDD cuida unidades y diseno interno; BDD cuida entendimiento compartido.  
Un equipo puede usar BDD para acordar que debe pasar y TDD para construir como hacerlo de manera segura.

### PA-3

Decir que 95% de cobertura significa que no hay bugs confunde ejecucion de lineas con calidad de las verificaciones.  
La cobertura solo indica que las pruebas pasaron por gran parte del codigo, no que revisaron los resultados correctos.  
Por ejemplo, una prueba puede ejecutar `calcular_precio_final()` con descuento del 10% y solo verificar que devuelve un numero.  
Esa prueba subiria cobertura, pero no detectaria si el sistema aplica primero el IVA y despues el descuento, que cambia la regla del negocio.  
Tambien pueden faltar casos limite, como descuento 0%, 40% o 41%, aunque el porcentaje de cobertura sea alto.  
La cobertura es una senal util para encontrar zonas no probadas, pero no demuestra ausencia de defectos.

### PA-4

Probar solo 20% es debil porque 20 esta en el centro de una particion valida y no tensiona los bordes de la regla.  
Los errores suelen aparecer cerca de los limites, por ejemplo usar `< 40` en vez de `<= 40`, o aceptar `-1` por no validar el minimo.  
Yo probaria 0 y 40 porque son valores validos en los extremos permitidos.  
Tambien probaria -1 y 41 porque son los valores invalidos inmediatamente por fuera del rango.  
Como valor representativo interno usaria 20 para confirmar que un caso normal funciona.  
Asi se cubren particiones y limites, no solo un ejemplo conveniente.

### PA-5

TDD y BDD producen una suite automatizada que puede ejecutarse muchas veces sin depender de revision manual.  
Esa suite es una base practica para CI/CD porque cada push o merge puede validar si las reglas siguen funcionando.  
TDD aporta pruebas pequenas y rapidas para detectar fallos tecnicos cerca del codigo que los causa.  
BDD aporta escenarios entendibles que verifican reglas de negocio completas, como descuento e IVA.  
Si el pipeline de CI/CD no tiene tests solidos, solo automatiza el movimiento del codigo, pero no da confianza real sobre su calidad.  
En ese caso puede desplegar mas rapido, pero tambien puede propagar defectos mas rapido.
