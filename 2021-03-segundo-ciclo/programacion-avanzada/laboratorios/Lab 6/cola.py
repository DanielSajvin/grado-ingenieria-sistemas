from nodo import Nodo

class Cola:
    def __init__(self, max = -1):
        self.tamaño = 0
        self.frente = None
        self.fondo = None
        self.max = max
        #self.atentido = 0

    def insertar(self, nombre, carne, monto, tiempo):
        nuevo = Nodo(nombre, carne, monto, tiempo)
        if self.frente == None and self.fondo == None:
            self.frente = nuevo
            self.fondo = nuevo
        elif self.tamaño == self.max:
            raise Exception('ERROR: Desbordamiento de cola')
        else:
            self.fondo.siguiente = nuevo
            self.fondo = nuevo
        self.tamaño += 1
    
    def recorrer(self):
        resultado = ''
        aux = self.frente

        while aux != None:
            resultado = resultado + str(aux) + '\n'
            aux = aux.siguiente
        return resultado
    
    def eliminar(self):
        aux = self.frente
        
        if self.tamaño == 0:
            raise Exception('ERROR: Subdesbordamiento de cola')
        elif self.tamaño == 1:
            self.frente = None
            self.fondo = None
        else:
            self.frente = aux.siguiente
            aux.siguiente = None
        self.tamaño -= 1
        
        return aux
    
    def __str__(self):

        return f"No. estudiantes en cola: {self.tamaño}\n"