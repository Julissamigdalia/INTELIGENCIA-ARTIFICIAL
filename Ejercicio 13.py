
nombre = "Julissa Migdalia"
materia = "IA"
# Imprimir información
print(f"Nombre: {nombre}")
print(f"Materia: {materia}")

# Ingresar la calificación
calificacion = int(input("Ingresa la calificación del alumno: "))

# Verificar el rango de la calificación e imprimir el mensaje correspondiente
if 95 <= calificacion <= 100:
    print(f"La calificación de {calificacion} es excelente.")
elif 85 <= calificacion <= 94:
    print(f"La calificación de {calificacion} es notable.")
elif 75 <= calificacion <= 84:
    print(f"La calificación de {calificacion} es buena.")
elif 70 <= calificacion <= 74:
    print(f"La calificación de {calificacion} es suficiente.")
else:
    print(f"La calificación de {calificacion} indica que el alumno está reprobado.")
