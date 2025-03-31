#EJERCICIOS BASICOS

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
