datos_temperatura = {
    "Oaxaca": 15,
    "Tlaxiaco": 20,
    "Puebla": 15,
    "Guadalajara": 25
}

def buscar_ciudades_por_temperatura(temperatura):
    ciudades = []
    
    if temperatura == datos_temperatura["Oaxaca"]:
        ciudades.append("Oaxaca")
    if temperatura == datos_temperatura["Tlaxiaco"]:
        ciudades.append("Tlaxiaco")
    if temperatura == datos_temperatura["Puebla"]:
        ciudades.append("Puebla")
    if temperatura == datos_temperatura["Guadalajara"]:
        ciudades.append("Guadalajara")
    
    return ciudades


temperatura = float(input("Ingrese la temperatura: "))


ciudades_encontradas = buscar_ciudades_por_temperatura(temperatura)


if ciudades_encontradas:
    print(f"La temperatura de {temperatura}ºC se encuentra en: {', '.join(ciudades_encontradas)}.")
else:
    print("No hay ciudades registradas con esa temperatura.")
