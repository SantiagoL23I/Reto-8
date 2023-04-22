n = int(input("Escribe un número: ")) #Pide al usuario digitar el número inicial
if n % 2 == 1:#Si n es impar, se le resta 1 para obtener el número par más cercano 
    n -= 1
for i in range(n, 0, -2):# Números pares en forma descendente
    print(i) #Imprimir los números 