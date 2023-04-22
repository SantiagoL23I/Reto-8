# Reto-8
## 1. Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.
```pseudocode
for i in range(1, 101): #Números ascendentes hasta el 100
    print("El cuadrado del número " + str(i) + " es " + str(i**2)) #Imprime el número y su respectivo cuadrado
```
## 2. Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.
```pseudocode
print("Los números impares son:") #Imprime el texto inicial
for i in range(1, 1000, 2): #Números impares en forma ascendente hasta 999
    print(i) #Imprime los números

print("Los números pares son:") #Imprime el texto inicial
for i in range(2, 1001, 2): #Números pares en forma ascendente hasta 1000
    print(i) #Imprime los números
```
## 3.Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado
```pseudocode
n = int(input("Escribe un número: ")) #Pide al usuario digitar el número inicial
if n % 2 == 1:#Si n es impar, se le resta 1 para obtener el número par más cercano 
    n -= 1
for i in range(n, 0, -2):# Números pares en forma descendente
    print(i) #Imprimir los números 
```
## 4. Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial
```pseudocode
n = int(input("Introduce un número: "))#Pide al usuario digitar el número inicial
for i in range(1, n+1): #Recorre los números desde 1 hasta el número dado (n+1)
    factorial = 1 #Variable empieza en 1
    for f in range(1, i+1): #Recorre los números desde 1 hasta los números de i
        factorial *= f #multiplica los números por sus antecesores hasta llegar al 1
    print(i,"! = ", factorial) #imprime el número y su factorial
```
## 5. Calcular el valor de 2 elevado a la potencia n usando ciclos for.
```pseudocode
n=int(input("Escriba un número:"))
x=1
for i in range(n):
   x*=2
print(x)  
```
## 6. Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for.
```pseudocode
x = float(input("Introduce el número: "))
n = int(input("Introduce el indice: "))
r = 1
for i in range(n):
    r *= x
print(x, "elevado a la potencia", n, "es", r)
```
## 7. Diseñe un programa que muestre las tablas de multiplicar del 1 al 9.
```pseudocode
for i in range(1, 10):     # Recorre los números del 1 al 9
    print("Tabla del", i)   #imprime la tabla que seesta viendo
    for x in range(1, 11):    # Recorre los números del 1 al 10
        r = i * x    # Calcula el resultado de la multiplicación
        print(i, "multiplicado por", x, "=", r) #Imprime los números quese multiplican y suresultado
    print()   # Imprime una línea en blanco para separar las tablas
```
## 8. Diseñar una función que permita calcular una aproximación de la función exponencial alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. nota: use math para traer la función exponencial y mostrar la diferencia entre el valor real y la aproximación.
```pseudocode
import math

def Aproximación(x, n): 
    r = 0#variable empieza en 0
    for i in range(n): #recorre hasta el numero n-1
        r += x**i / math.factorial(i) #serie de Maclaurin
    return r 

x =int(input("escribe el número:")) #Pide un número a el usuario
n = int(input("escribe el número de series:")) #Pide el número de series 
a = Aproximación(x, n) #llama la función de aproximación
r= math.exp(x) #toma el valor real 
print(a) #imprime la aproximación
print(r) #imprime el valor real
print("diferencia:"+str(r-a)) #imprime la diferencia entre los dos valoes
```
## 9. Diseñar una función que permita calcular una aproximación de la función seno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. nota: use math para traer la función seno y mostrar la diferencia entre el valor real y la aproximación.
```pseudocode
import math

def aproximacionSeno(x, n): #define la función
    a = 0
    for i in range(n): #recorre todos los números hasta n-1 
        s = (-1) ** i #cambia signo y eleva por los numeros del for
        t = (x ** (2 * i + 1)) / math.factorial(2 * i + 1)#Calcula una aproximación de la función seno para x utilizando los primeros n términos de la serie de Maclaurin
        a += s * t #calcula todos los datos para dar la aproximación guardada en a
    return a

x = int(input("ingrese un número")) #pide al usuario el número
n = int(input("ingrese un número")) #pide al usuario las series
a = aproximacionSeno(x, n) #llama la función
r = math.sin(x) #resultado real

print("Aproximación:"+str (a)) #imprime la aproxcimación
print("Valor real:"+str(r)) #imprime la el valor real
print("Diferencia:"+str(r - a)) #imprimer la diferencia entre los dos valores
```
## 10.Diseñar una función que permita calcular una aproximación de la función arcotangente alrededor de 0 para cualquier valor x en el rango [-1, 1], utilizando los primeros n términos de la serie de Maclaurin. nota: use math para traer la función arctan y mostrar la diferencia entre el valor real y la aproximación.
```pseudocode
import math

def aproximacionArcotangente(x, n): #define la función
    
    if abs(x) > 1: #limita los valores que soporta
        raise ValueError("x debe estar en el rango [-1, 1]")#genera el error al poner valoresfuera de los rangos
    a = 0 #variable empieza en 0
    for i in range(n): #recorre los números hasta n-1 
        s = (-1) ** i #cambia signo y eleva por los numeros del for
        t = (x ** (2 * i + 1)) / (2 * i + 1) #Calcula una aproximación de la función arcotangente para x utilizando los primeros n términos de la serie de Maclaur
        a += s * t #calcula todoslos datos para dar la aproximación guardada en a
    return a 
x = int(input("ingrese un número")) #pide al usuario el número
n = int(input("ingrese un número")) #pide al usuario las series
a= aproximacionArcotangente(x, n) #llama la función
real = math.atan(x) #valor real

print("Aproximación:"+str(a)) #imprime la aproximación
print("Valor real:"+str(real)) #imprime el valor real
print("Diferencia:"+str(real - a)) #imprime la diferencia entre los dos valores

```
