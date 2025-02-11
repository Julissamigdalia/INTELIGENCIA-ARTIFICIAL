import math


radio = float(input("Introduce el radio del círculo en metros:\n"))

# Calcular el área del círculo (A = π * r^2)
area = math.pi * (radio ** 2)


print(f"\nEl área del círculo con radio {radio:.1f} metros es: {area:.2f} metros cuadrados.")