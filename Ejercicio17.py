
numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))


print(f"\nTabla de multiplicar del {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

