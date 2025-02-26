def es_par(num):
    """Verifica si un numero es par."""
    return num % 2 == 0

def suma_de_pares(a, b):
    """Verifica si la suma de dos numeros pares es par."""
    if es_par(a) and es_par(b):
        suma = a + b
        return True, suma
    return False, None


print("Bienvenido a la demostracion del teorema: La suma de dos numeros pares es siempre par.")
numero1 = int(input("Introduce el primer numero par: "))
numero2 = int(input("Introduce el segundo numero par: "))  # Cambié el texto aquí

if es_par(numero1) and es_par(numero2):
    es_suma_par, resultado = suma_de_pares(numero1, numero2)
    if es_suma_par:
        print(f"La suma de {numero1} y {numero2} es {resultado}, que es un numero par.")
    else:
        print(f"Error: la suma de {numero1} y {numero2} no es par.")
else:
    print("Al menos uno de los numeros no es par. Asegurate de ingresar numeros pares.")  # Corregí la indentación aquí
