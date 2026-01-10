class Conjunto: 
    def __init__(self, elemento):
        self.conjunto = elemento 
        self.elementos = []
    
    def agregar_elemento(self, element):
        self.elementos.append(element)

    def eliminar_elemento(self, no_eliminado):
        while no_eliminado in self.elementos:
            self.elementos.remove(no_eliminado)
    
    def vaciar_conj(self):
        self.elementos.clear()

    def interseccion(self):
       pass

    def __str__(self):
        return(f"{self.conjunto} - {self.elementos}")