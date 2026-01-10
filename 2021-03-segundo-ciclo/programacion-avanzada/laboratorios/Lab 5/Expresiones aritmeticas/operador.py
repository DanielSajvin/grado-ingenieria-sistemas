from nodo import Nodo

class Operador:
    def __init__(self, max = -1):
        self.tope = None
        self.tamaño = 0
        self.max = max

    def insertar(self, operador):
        if self.max == -1 or self.tamanio < self.max:
            nuevo_operador = Nodo(operador)
            nuevo_operador.siguiente = self.tope
            self.tope = nuevo_operador
            self.tamaño += 1 
        else:
            raise Exception('Desbordamiento de pila')

    def recorrer(self):
        aux = self.tope
        while True:
            if aux == None:
                break
            else:
                print(end=''+str(aux))
                aux = aux.siguiente