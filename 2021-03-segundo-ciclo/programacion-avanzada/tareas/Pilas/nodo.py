class Nodo:
    def __init__(self, nombre):
        # Parte amarilla
        self.nombre = nombre
        # Parte morada
        self.siguiente = None
        
    def __str__(self):
        return self.nombre