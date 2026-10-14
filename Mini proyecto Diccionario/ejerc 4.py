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

    def es_completo(self):
        return self._verificar_completo(self.raiz)

    def _verificar_completo(self, nodo):
        if nodo is None:
            return True

        hijo_izq = nodo.izquierdo is not None
        hijo_der = nodo.derecho is not None

        if hijo_izq != hijo_der:
            return False

        return (
            self._verificar_completo(nodo.izquierdo)
            and self._verificar_completo(nodo.derecho)
        )


# Pruebas de ejecución
arbol = ArbolBinarioBusqueda()

for numero in [50, 30, 70, 20, 40, 60, 80]:
    arbol.insertar(numero)

print("Primer arbol:", arbol.es_completo())

otro_arbol = ArbolBinarioBusqueda()

for numero in [50, 30, 70, 20]:
    otro_arbol.insertar(numero)

print("Segundo arbol:", otro_arbol.es_completo())