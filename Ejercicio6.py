nombre = input("Ingresa el nombre de la tienda: ")
nombre = input("Ingresa tu nombre: ")
producto = input("Ingresa el nombre del producto: ")
total_compra = float(input("Ingresa el total de tu compra: "))

if total_compra > 100:
    descuento = total_compra * 0.10
    total_final = total_compra - descuento
    print(f"¡Felicidades {nombre}! Tienes un descuento del 10% en tu producto {producto}.")
    print(f"El total a pagar es: {total_final:.2f}")
else:
    print(f"{nombre}, el total a pagar por tu producto {producto} es: {total_compra:.2f}")
