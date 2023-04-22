x = float(input("Introduce el número: "))
n = int(input("Introduce el indice: "))
r = 1
for i in range(n):
    r *= x
print(x, "elevado a la potencia", n, "es", r)
