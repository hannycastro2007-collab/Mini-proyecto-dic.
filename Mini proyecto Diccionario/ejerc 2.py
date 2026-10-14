from collections import deque


class NodoArbol:

    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


class ArbolBinarioBusqueda:

    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = NodoArbol(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierdo is None:
                nodo.izquierdo = NodoArbol(valor)
            else:
                self._insertar_recursivo(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            if nodo.derecho is None:
                nodo.derecho = NodoArbol(valor)
            else:
                self._insertar_recursivo(nodo.derecho, valor)

    def por_niveles(self):
        elementos = []

        if self.raiz is None:
            return elementos

        fila = deque([self.raiz])

        while fila:
            actual = fila.popleft()
            elementos.append(actual.valor)

            if actual.izquierdo is not None:
                fila.append(actual.izquierdo)

            if actual.derecho is not None:
                fila.append(actual.derecho)

        return elementos


# Pruebas de ejecución
arbol = ArbolBinarioBusqueda()

for numero in [50, 30, 70, 20, 40, 60, 80]:
    arbol.insertar(numero)

print("Recorrido por niveles:", arbol.por_niveles())