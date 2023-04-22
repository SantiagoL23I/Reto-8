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