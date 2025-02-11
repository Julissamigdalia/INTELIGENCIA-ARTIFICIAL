# Pedir datos al usuario
nombre = input("Ingrese su nombre completo: ")
carrera = input("Ingrese su carrera: ")
semestre = input("Ingrese su semestre: ")
materia = input("Ingrese la materia: ")

# Imprimir los datos
print("\n=== Datos del estudiante ===")
print(f"Nombre completo: {nombre}")
print(f"Carrera: {carrera}")
print(f"Semestre: {semestre}")
print(f"Materia: {materia}")
num = int(input("Ingresa un número: "))
if num % 2 == 0:
    print(f"{num} es par.")
else:
    print(f"{num} es impar.")
