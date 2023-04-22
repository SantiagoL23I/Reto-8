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
