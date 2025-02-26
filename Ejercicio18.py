class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

n1 = Nodo(10)
n2 = Nodo(20)
n3 = Nodo(30)
n1.siguiente = n2 
n2.siguiente = n3


actual = n1
while actual:
    print(actual.dato," ->", end=" ")
    actual = actual.siguiente
print(" ")
