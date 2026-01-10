from nodo import Nodo

class Pila:
    def __init__(self, max = -1):
        self.tope = None
        self.tamaño = 0
        self.max = max
    
    def insertar(self, letra):
        nueva_letra = Nodo(letra)
        nueva_letra.siguiente = self.tope
        self.tope = nueva_letra
        self.tamaño += 1
    
    def recorrer(self):
        aux = self.tope
        while True:
            if aux == None:
                break
            else:
                print(aux)
                aux = aux.siguiente
    
    def eliminar(self):
        if self.tope == None:
            raise Exception('ERROR: Subdesbordamiento')
        else:
            aux = self.tope
            self.tope = self.tope.siguiente
            aux.siguiente = None
            self.tamaño -= 1
            return aux