
class Palabra:
    def __init__(self, texto, definicion):
        self.texto = texto.strip()
        self.definicion = definicion.strip()


class Nodo:
    def __init__(self, palabra):
        self.palabra = palabra
        self.izquierdo = None
        self.derecho = None


class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, palabra):
        if not self.raiz:
            self.raiz = Nodo(palabra)
            return
        actual, nuevo = self.raiz, palabra.texto.casefold()
        while True:
            if nuevo < actual.palabra.texto.casefold():
                if not actual.izquierdo:
                    actual.izquierdo = Nodo(palabra)
                    break
                actual = actual.izquierdo
            elif nuevo > actual.palabra.texto.casefold():
                if not actual.derecho:
                    actual.derecho = Nodo(palabra)
                    break
                actual = actual.derecho
            else:
                actual.palabra.definicion = palabra.definicion
                break

    def buscar_exacta(self, texto):
        return self._buscar_rec(self.raiz, texto.strip().casefold())

    def _buscar_rec(self, nodo, texto):
        if not nodo: return None
        actual = nodo.palabra.texto.casefold()
        if texto == actual: return nodo.palabra
        return self._buscar_rec(nodo.izquierdo if texto < actual else nodo.derecho, texto)

    def buscar_por_prefijo(self, prefijo):
        res, p = [], prefijo.strip().casefold()
        def _inorden(n):
            if n:
                _inorden(n.izquierdo)
                if n.palabra.texto.casefold().startswith(p): res.append(n.palabra)
                _inorden(n.derecho)
        _inorden(self.raiz)
        return res

    def obtener_todos(self):
        res = []
        def _inorden(n):
            if n:
                _inorden(n.izquierdo)
                res.append(n.palabra)
                _inorden(n.derecho)
        _inorden(self.raiz)
        return res


def cargar_diccionario(arbol):
    datos = [
        ("algoritmo", "Conjunto de pasos para resolver un problema."),
        ("almacenamiento", "Proceso de guardar informacion."),
        ("analisis", "Estudio detallado de un tema."),
        ("aplicacion", "Programa que realiza tareas."),
        ("arbol", "Estructura de datos con nodos."),
        ("base de datos", "Coleccion organizada de informacion."),
        ("binario", "Sistema que utiliza dos valores."),
        ("busqueda", "Proceso de localizar informacion."),
        ("codigo", "Instrucciones escritas en un lenguaje."),
        ("dato", "Representacion de un hecho o valor."),
        ("diccionario", "Coleccion de palabras y significados."),
        ("funcion", "Bloque de codigo reutilizable."),
        ("nodo", "Elemento de una estructura de datos."),
        ("programa", "Conjunto de instrucciones ejecutables."),
        ("variable", "Espacio para almacenar un valor.")
    ]
    for t, d in datos:
        arbol.insertar(Palabra(t, d))


def main():
    arbol = ArbolBinarioBusqueda()
    cargar_diccionario(arbol)
    
    while True:
        print("\n--- DICCIONARIO ---")
        print("1. Buscar palabra\n2. Buscar por prefijo\n3. Ver todas\n4. Salir")
        op = input("Elige una opcion (1-4): ").strip()

        if op == "1":
            p = arbol.buscar_exacta(input("Palabra: "))
            print(f"\n{p.texto}: {p.definicion}" if p else "\nNo encontrada.")
        elif op == "2":
            res = arbol.buscar_por_prefijo(input("Prefijo: "))
            print("\n".join([f"- {x.texto}: {x.definicion}" for x in res]) if res else "\nSin resultados.")
        elif op == "3":
            print("\n" + "\n".join([f"- {x.texto}: {x.definicion}" for x in arbol.obtener_todos()]))
        elif op == "4":
            break
        else:
            print("Opcion invalida.")


if __name__ == "__main__":
    main()