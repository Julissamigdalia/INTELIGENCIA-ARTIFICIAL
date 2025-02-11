import random
import datetime


nombre_tienda = "Tienda COPPEL"
folio = random.randint(1000, 9999) 
fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  

nombretienda = input("Ingresa el nombre de la tienda: ")
nombre = input("Ingresa tu nombre: ")
producto = input("Ingresa el nombre del producto: ")
cantidad = int(input("Ingresa la cantidad del producto: "))
precio_unitario = float(input("Ingresa el precio unitario del producto: "))


total_compra = cantidad * precio_unitario

if total_compra > 100:
    descuento = total_compra * 0.10
    total_final = total_compra - descuento
else:
    descuento = 0
    total_final = total_compra


print("\n" + "=" * 40)
print("         TICKET DE COMPRA         ")
print("=" * 40)
print(f"Tienda: {nombre_tienda}")
print(f"Folio: {folio}")
print(f"Fecha y hora: {fecha_hora}")
print("-" * 40)
print(f"Cliente: {nombre}")
print(f"Producto: {producto}")
print(f"Total de la compra: ${total_compra:.2f}")
print(f"Descuento aplicado: ${descuento:.2f}")
print(f"Total a pagar: ${total_final:.2f}")
print("-" * 40)
print("¡Gracias por tu compra! ¡Vuelve pronto!")
print("=" * 40)
