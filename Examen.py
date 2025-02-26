import os

def mostrar_menu():
    print("=== MENÚ DE EJERCICIOS ===")
    print("1.  Ejercicio 1 NOMBRE PERSONAL")
    print("2.  Ejercicio 2 AREA DEL CIRCULO")
    print("3.  Ejercicio 3 SUMAR NUERMOS")
    print("4. Ejercicio 4 NUMERO POSITIVO, NEGATIVO")
    print("5. Ejercicio 5 DATOS DEL USUARIO")
    print("6. Ejercicio 6 DATOS DE TIENDA")
    print("7. Ejercicio 7 MAYOR O NO MAYOR")
    print("8. Ejercicio 8 CLIENTE")
    print("9. Ejercicio 9 PAR Y IMPAR")
    print("10.Ejercicio 10 DESCUENTO")
    print("11.Ejercicio 11 RESTA Y MULTIPLICACION")
    print("12.Ejercicio 12 NUMERO ALEATORIO")
    print("13.Ejercicio 13 CALIFICACION")
    print("14.Ejercicio 14 TICKET")
    print("15.Ejercicio 15 TEMPERATURA")
    print("16.Ejercicio 16 SUMA DE NUMEROS PAR")
    print("17.Ejercicio 17 FOR ")
    print("18.Ejercicio 18 NODO")
    print("19.Ejercicio 19 HEURISTICA")
    print("20.Ejercicio 20 AGENTE")
    print("21.Ejercicio 21 GRAFO")
    print("22.Ejercicio 22 CONJUNTO DE NODOS VISITADOS")
    print("23.Ejercicio 23 VECINO")
    print("24.Ejercicio 24 SOLUCION OPTIMA")
    print("0. Salir")


ejercicio_seleccionado = None

while True:
    if ejercicio_seleccionado is None:
        mostrar_menu()  
    opcion = input("Seleccione una opción: ")
    
    if opcion.isdigit():
        opcion = int(opcion)
        
        if opcion == 0:
            print("Saliendo del programa...")
            break
        
        elif 1 <= opcion <= 27:
            ejercicio_seleccionado = opcion
            archivo = f"Ejercicio{opcion}.py"


            if os.path.exists(archivo):
                os.system(f"python {archivo}")
            else:
                print("El archivo no existe.")


        else:
            print("Opción no válida, intente de nuevo.")
    
    else:
        print("Por favor, ingrese un número válido.")
    
   
    input("Presione Enter para elegir otro ejercicio...")

    ejercicio_seleccionado = None  
