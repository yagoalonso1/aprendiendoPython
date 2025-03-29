#EJERCICIOS BASICOS

#1. Imprime “Hola, mundo” en pantalla.

print("Hola mundo")

#2.	Solicita un número e imprímelo en pantalla.

ex2= int(input("Ingrese un numero: "))

print (f"Numero seleccionado : {ex2}")

#3.	Solicita dos números e imprime su suma.
numero1 = int(input("Introduce un numero: "))
numero2 = int(input("Introduce un numero: "))
resultado = int(numero1+numero2)
print (f"El resultado de {numero1} + {numero2} = {resultado}")

#4.	Solicita dos números e imprime su resta.
numero1 = int(input("Introduce un numero: "))
numero2 = int(input("Introduce un numero: "))
resultado = int(numero1+numero2)
print (f"El resultado de {numero1} - {numero2} = {resultado}")

#5.	Solicita dos números e imprime su multiplicación.
numero1 = int(input("Introduce un numero: "))
numero2 = int(input("Introduce un numero: "))
resultado = int(numero1+numero2)
print (f"El resultado de {numero1} * {numero2} = {resultado}")

#6.	Solicita dos números e imprime su división.
numero1 = int(input("Introduce un numero: "))

while True:
    numero2 = int(input("Ingrese un número distinto de 0: "))
    if numero2 != 0:
        break
    print("El número no puede ser 0. Intenta nuevamente.")

resultado = numero1 / numero2
print(f"El resultado de {numero1} / {numero2} = {resultado}")

#7.	Solicita un número e imprime si es par o impar.
espar = int(input("Introduce un numero"))
if espar %2 == 0 :
    print(f"El numero {espar} es par")
else:
    print(f"El numero {espar}  es impar")

#8.	Solicita un número e imprime si es positivo, negativo o cero.
tipoNumero = int(input("Introduce el numero y te dire de que tipo es"))
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
#11. Solicita un número y muestra su tabla de multiplicar hasta el 10.
#12. Convierte grados Celsius a Fahrenheit.
#13. Convierte kilómetros a millas.
#14. Calcula el área de un triángulo dados su base y altura.
#15. Calcula el perímetro de un círculo dado su radio.