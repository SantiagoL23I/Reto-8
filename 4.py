n = int(input("Introduce un número: "))#Pide al usuario digitar el número inicial
for i in range(1, n+1): #Recorre los números desde 1 hasta el número dado (n+1)
    factorial = 1 #Variable empieza en 1
    for f in range(1, i+1): #Recorre los números desde 1 hasta los números de i
        factorial *= f #multiplica los números por sus antecesores hasta llegar al 1
    print(i,"! = ", factorial) #imprime el número y su factorial

