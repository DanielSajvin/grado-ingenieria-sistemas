from nodo import Nodo

class Pila: 
    def __init__(self, max = -1):
        self.tope = None
        self.tamaño = 0
        self.max = max

    def insertar(self, nombre):
        if self.max == -1 or self.tamaño < self.max:
            # Puedo ingresar
            # Crear el nuevo Nodo
            nueva_pelicula = Nodo(nombre)
            # Enlazar al nodo viejo
            nueva_pelicula.siguiente = self.tope
            # Apuntar al nodo nuevo
            self.tope = nueva_pelicula
            # Aumentar tamaño de la pila
            self.tamaño += 1
        else:
            # Lanzar un error
            raise Exception('ERROR: Desbordamiento de pila')
    
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
            raise Exception('ERROR: Subdesbordamiento de pila')
        else:
            aux = self.tope
            self.tope = self.tope.siguiente
            aux.siguiente = None
            self.tamaño -= 1
            return aux

        