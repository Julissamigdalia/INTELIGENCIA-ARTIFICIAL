import heapq

def a_estrella(grafo, inicio, fin, heuristica):
    abierta = [] 
    cerrada = set()
    heapq.heappush(abierta, (0 + heuristica(inicio), 0, inicio, []))
    
    while abierta:
        _, costo, nodo, camino = heapq.heappop(abierta)
        if nodo in cerrada:
            continue
        camino = camino + [nodo]
        if nodo == fin:
            return camino
        cerrada.add(nodo)
        for vecino, peso in grafo.get(nodo, []):
            if vecino not in cerrada:
                heapq.heappush(abierta, (costo + peso + heuristica(vecino), costo + peso, vecino, camino))
    return None

# Ejemplo de grafo: claves son nodos, valores son listas de tuplas (vecino, peso)
grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

# Heurística simple: la distancia entre el nodo y el nodo 'D'
def heuristica(nodo):
    distancias = {'A': 3, 'B': 2, 'C': 1, 'D': 0}
    return distancias.get(nodo, float('inf'))  # Devuelve infinito si el nodo no está en el diccionario

# Llamada a la función
inicio = 'A'
fin = 'D'
camino = a_estrella(grafo, inicio, fin, heuristica)

if camino:
    print(f"Camino encontrado: {camino}")
else:
    print("No se encontró un camino.")
