from nodo import Nodo

class Cola:
    def __init__(self, max = -1):
        self.tamaño = 0
        self.frente = None
        self.fondo = None
        self.max = max

    def insertar(self, nombre, edad):
        # 1. Construir el nodo
        nuevo = Nodo(nombre, edad)
        # 2. Anclar el nuevo nodo
        # 3. Consultar si la cola está vacía
        # 3.1. Frente y fondo apuntar a nuevo
        if self.frente == None and self.fondo == None:
            self.frente = nuevo
            self.fondo = nuevo
            # 3.2 Consultar si la cola está llena
        elif self.tamaño == self.max:
            raise Exception('Error: Desbordamiento de cola')
        # 3.3 Todo lo demás
        else:
            # 3.a Fondo siguiente apunta a nuevo 
            self.fondo.siguiente = nuevo
            # 3.b Fondo apunta a nuevo 
            self.fondo = nuevo 
        # 4. Actualizar datos
        self.tamaño += 1
    
    def recorrer(self):
        resultado = ''
        # 1. Colocar el auxiliar en el frente 
        aux = self.frente
        
        while aux != None:
            #2. Visitar el nodo
            resultado = resultado + str(aux) + '\n'
            # 3. Mover el auxiliar
            aux = aux.siguiente
        return resultado
    
    def buscar_nodo(self, nombre):
        aux = self.frente
        vistos = 0
        while vistos < self.tamaño:
            if nombre == aux.nombre:
                return aux
            else:
                aux = aux.siguiente
                vistos += 1
                
        if vistos == self.tamaño:
            raise Exception('ERROR: El elemento no existe dentro de la cola')

    def eliminar(self):
        # 1. Crear el auxiliar (señalar al frente)
        aux = self.frente

        if self.tamaño == 0:
            raise Exception('ERROR: Subdesbordamiento de cola')
        elif self.tamaño == 1:
            self.frente = None
            self.fondo = None
        else: 

            #2. Mover el frente al siguiente elemento
            self.frente = aux.siguiente

            #3. Quitar enlaces
            aux.siguiente = None

        # 4. Disminuir tamaño
        self.tamaño -= 1

        # 5. Devolver el nodo eliminado
        return aux

    def __str__(self):
        return f"Tamaño: {self.tamaño}\nMax: {self.max}\nFrente: {self.frente}\nFondo: {self.fondo}"
