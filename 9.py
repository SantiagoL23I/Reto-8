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
