#EJERCICIOS BASICOS
import math

#1. Imprime “Hola, mundo” en pantalla.

print("Hola mundo")

#2.	Solicita un número e imprímelo en pantalla.

ex2= int(input("Introduce un número y te lo muestro por pantalla: "))

print (f"Numero seleccionado : {ex2}")

#3.	Solicita dos números e imprime su suma.
numero1 = int(input("Introduce el primer numerador: "))
numero2 = int(input("Introduce el segundo numerador : "))
resultado = int(numero1+numero2)
print (f"El resultado de {numero1} + {numero2} = {resultado}")

#4.	Solicita dos números e imprime su resta.
numero1 = int(input("Introduce el primer producto: "))
numero2 = int(input("Introduce el segundo producto: "))
resultado = int(numero1-numero2)
print (f"El resultado de {numero1} - {numero2} = {resultado}")

#5.	Solicita dos números e imprime su multiplicación.
numero1 = int(input("Introduce el primer producto : "))
numero2 = int(input("Introduce el segundo producto : "))
resultado = int(numero1+numero2)
print (f"El resultado de {numero1} * {numero2} = {resultado}")

#6.	Solicita dos números e imprime su división.
numero1 = int(input("Introduce el numerador: "))

while True:
    numero2 = int(input("Ingrese el denominador distinto de 0: "))
    if numero2 != 0:
        break
    print("El número no puede ser 0. Intenta nuevamente.")

resultado = numero1 / numero2
print(f"El resultado de {numero1} / {numero2} = {resultado}")

#7.	Solicita un número e imprime si es par o impar.
espar = int(input("Introduce un número y te diré si es par o no. "))
if espar %2 == 0 :
    print(f"El número {espar} es par")
else:
    print(f"El número {espar}  es impar")

#8.	Solicita un número e imprime si es positivo, negativo o cero.
tipoNumero = int(input("Introduce el número y te dire de que tipo es"))
if tipoNumero > 0 :
    print (f"{tipoNumero} es positivo")
elif tipoNumero < 0 :
    print(f"{tipoNumero} es negativo")
else:
    print(f"{tipoNumero} es 0")
#9.	Solicita dos números e imprime cuál es mayor.
numMenor=int(input("Introduce el primer numero y te dire cual es mayor"))
numMenor2=int(input("Introduce el segundo numero y te dire cual es mayor"))

if numMenor < numMenor2 :
    print(f"El numero {numMenor2} es mas grande")
else:
    print (f"f El numero {numMenor} es mas grande")

#10. Solicita tres números e imprime el mayor de los tres.
vector = [0] * 3
print("Introduce el primnero de los tres numeros y te imprimo el mayor: ")
for i in range (3) :
    numeroGuardado = int(input(f"Introduce el número que quieres guardar en la array en posicion {i}" ))
    vector [i] = numeroGuardado
    numeroMaximo = max(vector)
print(f"El numero mas alto es {numeroMaximo}")

#11. Solicita un número y muestra su tabla de multiplicar hasta el 10.
variable = int(input("Escribe un número y te daré su tabla de multiplicar hasta 10 \n"))
print (f"La taula del {variable} :  ")
for i in range (1,11):
   resultadoTabla = variable * i
   print(f" {variable} * {i} = {resultadoTabla} \n")
#12. Convierte grados Celsius a Fahrenheit.
celsius = float(input("Cuántos grados Celsius quieres pasar a Fahrenheit: "))
fahrenheit = float(celsius * 1.8 + 32.0)
print(f"{celsius}° Celsius son {fahrenheit}° Fahrenheit")
#13. Convierte kilómetros a millas.
km = float(input("Cuantos km quieres pasar a millas "))
millas = km / 1.60934
print(f"{km} km son {millas}mi")
#1,609,34 km = 1 mi
#14. Calcula el área de un triángulo dados su base y altura.
base = 2
altura = 2
area = base * altura /2
#15. Calcula el perímetro de un círculo dado su radio.
radio = 2
perimetro = 2 * radio * math.pi
print(f"El perimetro de un circulo con radio {radio} es de {perimetro}")
#16. Solicita un número e imprime si es múltiplo de 3.
numeromultiplo3 = int(input("Introduce un número y te diré si es multiplo de 3: \n"))
if (numeromultiplo3 % 3 == 0 ) :
    print(f"El número {numeromultiplo3}  es multiplo de 3")
else:
    print(f"El número {numeromultiplo3} no es multiplo de 3")
#17. Solicita un número e imprime si es múltiplo de 5.
numeromultiplo5 = int(input("Introduce un número y te diré si es multiplo de 5: \n"))
if (numeromultiplo5 % 5 == 0 ) :
    print(f"El número {numeromultiplo5}  es multiplo de 5")
else:
    print(f"El número {numeromultiplo5} no es multiplo de 5")
#18. Solicita un año e imprime si es bisiesto.
yearBisiesto = input("Introduce un año y te diré si es bisiesto o no")
if yearBisiesto % 4 != 0 :
    print("No es bisiesto")
elif yearBisiesto % 4 == 0 and yearBisiesto % 100 != 0:  # divisible entre 4 y no entre 100 o 400
    print("Es bisiesto")
elif yearBisiesto % 4 == 0 and yearBisiesto % 100 == 0 and yearBisiesto % 400 != 0:  # divisible entre 4 y 10 y no entre 400
    print("No es bisiesto")
elif yearBisiesto % 4 == 0 and yearBisiesto % 100 == 0 and yearBisiesto % 400 == 0:  # divisible entre 4, 100 y 400
    print("Es bisiesto")
#19. Solicita tres números e imprime si pueden formar un triángulo.

#20. Verifica si un número es un dígito (entre 0 y 9).

#21. Solicita una letra e imprime si es vocal o consonante.

#22. Verifica si un número tiene dos cifras.

#23. Solicita una contraseña y verifica si es "1234".

#24. Calcula el descuento en una compra según el monto total.

#25. Determina si un número es primo.

#26. Imprime los números del 1 al 10 con un while.

#27. Imprime los números del 1 al 10 con un for.

#28. Imprime los números pares del 1 al 20.

#29. Imprime los números impares del 1 al 20.

#30. Imprime la suma de los números del 1 al 100.

#31. Imprime la suma de los números pares del 1 al 100.

#32. Cuenta cuántos múltiplos de 3 hay entre 1 y 100.

#33. Pide números hasta que el usuario ingrese un 0.

#34. Pide números hasta que el usuario ingrese un negativo.

#35. Muestra la serie de Fibonacci hasta el término número 10.

#36. Cuenta cuántos números pares e impares hay en una lista de 10 números.

#37. Pide una palabra e imprime cada letra en una línea separada.

#38. Pide un número y muestra sus divisores.

#39. Calcula el factorial de un número.

#40. Invierte una cadena ingresada por el usuario.

#41. Crea una lista con los números del 1 al 10.

#42. Crea una lista de 5 palabras e imprímelas.

#43. Pide 5 números y guárdalos en una lista.

#44. Encuentra el número mayor en una lista de 10 números.

#45. Suma todos los números de una lista.

#46. Cuenta cuántas veces aparece un número en una lista.

#47. Imprime la lista en orden inverso.

#48. Elimina los elementos duplicados de una lista.

#49. Ordena una lista de números de menor a mayor.

#50. Encuentra el segundo número más grande de una lista.

#51. Une dos listas en una sola.

#52. Cuenta cuántas palabras tienen más de 5 letras en una lista.

#53. Sustituye todas las vocales de una palabra por "*".

#54. Cuenta cuántas veces aparece una letra en una frase.

#55. Verifica si una palabra es un palíndromo.

#56. Concatena los elementos de una lista en una sola cadena.

#57. Crea un archivo y escribe "Hola, mundo".

#58. Lee el contenido de un archivo de texto.

#59. Escribe 5 líneas en un archivo.

#60. Cuenta cuántas líneas tiene un archivo.

#61. Cuenta cuántas palabras hay en un archivo.

#62. Copia el contenido de un archivo en otro.

#63. Encuentra la palabra más larga en un archivo.

#64. Reemplaza una palabra específica en un archivo.

#65. Escribe una lista de números en un archivo y luego léelos.

#66. Crea una función que reciba un número y devuelva su cuadrado.

#67. Crea una función que reciba dos números y devuelva su suma.

#68. Crea una función que determine si un número es par.

#69. Crea una función que reciba una lista y devuelva el número mayor.

#70. Crea una función que determine si un número es primo.

#71. Crea una función que invierta una cadena.

#72. Crea una función que cuente cuántas vocales tiene una palabra.

#73. Crea una función que reciba una lista y devuelva la suma de sus elementos.

#74. Crea una función que verifique si un número es múltiplo de otro.

#75. Crea una función que reciba dos listas y devuelva una lista con los elementos comunes.

#76. Crea una función que devuelva la serie de Fibonacci hasta un número dado.

#77. Crea una función que devuelva la factorización de un número.

#78. Crea una función que elimine los espacios de una cadena.

#79. Crea una función que reciba un texto y cuente cuántas palabras tiene.

#80. Crea una función que reciba un texto y reemplace todas las vocales por una "x".

#81. Crea una función que reciba una lista de números y devuelva solo los pares.

#82. Crea una función que determine si una palabra está en una lista.

#83. Crea una función que ordene una lista de palabras alfabéticamente.

#84. Crea una función que reciba una lista y devuelva una nueva sin duplicados.

#85. Crea una función que reciba una lista y la divida en dos mitades.

#86. Crea un programa que simule una calculadora.

#87. Crea un programa que solicite contraseñas hasta que el usuario acierte.

#88. Crea un programa que pida números hasta que el usuario escriba "fin".

#89. Crea un programa que analice un texto y muestre las palabras más usadas.

#90. Crea un programa que verifique si una frase es un pangrama.

#91. Crea un programa que cuente cuántos números primos hay en una lista.

#92. Crea un programa que genere una lista de 100 números aleatorios y los ordene.

#93. Crea un programa que simule el juego de "Piedra, Papel o Tijera".

#94. Crea un programa que simule el juego de "Adivina el número".

#95. Crea un programa que cuente la cantidad de palabras en un archivo de texto.

#96. Crea un programa que genere una contraseña aleatoria.

#97. Crea un programa que convierta números romanos a enteros.

#98. Crea un programa que convierta enteros a números romanos.

#99. Crea un programa que determine si dos palabras son anagramas.

#100. Crea un programa que encripte y desencripte texto con un cifrado simple.