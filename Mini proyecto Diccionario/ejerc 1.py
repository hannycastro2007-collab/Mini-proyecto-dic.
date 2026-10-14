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

    def eliminar(self, valor):
        self.raiz = self._eliminar_recursivo(self.raiz, valor)

    def _eliminar_recursivo(self, nodo, valor):
        if nodo is None:
            return None

        if valor < nodo.valor:
            nodo.izquierdo = self._eliminar_recursivo(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            nodo.derecho = self._eliminar_recursivo(nodo.derecho, valor)
        else:
            # Caso 1: el nodo no tiene hijos
            if nodo.izquierdo is None and nodo.derecho is None:
                return None

            # Caso 2: el nodo tiene un solo hijo
            if nodo.izquierdo is None:
                return nodo.derecho

            if nodo.derecho is None:
                return nodo.izquierdo

            # Caso 3: el nodo cuenta con dos hijos
            auxiliar = nodo.derecho
            while auxiliar.izquierdo is not None:
                auxiliar = auxiliar.izquierdo

            nodo.valor = auxiliar.valor
            nodo.derecho = self._eliminar_recursivo(nodo.derecho, auxiliar.valor)

        return nodo

    def inorden(self):
        resultado = []
        self._inorden_recursivo(self.raiz, resultado)
        return resultado

    def _inorden_recursivo(self, nodo, resultado):
        if nodo is not None:
            self._inorden_recursivo(nodo.izquierdo, resultado)
            resultado.append(nodo.valor)
            self._inorden_recursivo(nodo.derecho, resultado)


# Pruebas de ejecución
arbol = ArbolBinarioBusqueda()

for numero in [50, 30, 70, 20, 40, 60, 80]:
    arbol.insertar(numero)

print("Árbol original:", arbol.inorden())

arbol.eliminar(20)
print("Después de eliminar 20:", arbol.inorden())

arbol.eliminar(30)
print("Después de eliminar 30:", arbol.inorden())

arbol.eliminar(70)
print("Después de eliminar 70:", arbol.inorden())