# Implementación de un monticulo min-heap
# Brayan Sneider Sánchez Muñoz
class Monticulo:
    def __init__(self):
        self.heap = []

    def insertar(self, elemento):
        self.heap.append(elemento)
        self.subir(len(self.heap)-1)

    def subir(self, indice):
        padre = (indice-1)//2
        if indice > 0 and self.heap[indice] > self.heap[padre]:
            self.heap[indice], self.heap[padre] = self.heap[padre], self.heap[indice]
            self.subir(padre)

    def eliminar(self):
        if len(self.heap) == 0:
            print("Montículo vacio")
            return None
        elemento = self.heap[0]
        ultimo_elemento = self.heap.pop()
        if len(self.heap) > 0:
            self.heap[0] = ultimo_elemento
            self.bajar(0)
        return elemento

    def preorden(self):
        self.preorden_recursivo(0)

    def preorden_recursivo(self, indice):
        if indice < len(self.heap):
            print(self.heap[indice], end=" ")
            self.preorden_recursivo(2 * indice + 1)
            self.preorden_recursivo(2 * indice + 2)

    def por_niveles(self):
        for elemento in self.heap:
            print(elemento, end=" ")

    def bajar(self, indice):
        hijo_izquierdo = 2*indice+1
        hijo_derecho = 2*indice+2
        minimo=indice

        if hijo_izquierdo < len(self.heap) and self.heap[hijo_izquierdo] > self.heap[minimo]:
            minimo = hijo_izquierdo

        if hijo_derecho < len(self.heap) and self.heap[hijo_derecho] > self.heap[minimo]:
            minimo = hijo_derecho

        if minimo != indice:
            self.heap[indice], self.heap[minimo] = self.heap[minimo], self.heap[indice]
            self.bajar(minimo)


M= Monticulo()

M.insertar(10)
M.insertar(5)
M.insertar(15)
M.insertar(20)
M.insertar(8)
M.insertar(2)

print("Recorrido preorden:")
M.preorden()

print("\nRecorrido niveles:")
M.por_niveles()

print("\nElementos eliminados:")
print(M.eliminar())
print(M.eliminar())

print("\nRecorrido en preorden después de eliminar elementos:")
M.preorden()

print("\nInsertar elemento: 2")
M.insertar(2)
M.preorden()