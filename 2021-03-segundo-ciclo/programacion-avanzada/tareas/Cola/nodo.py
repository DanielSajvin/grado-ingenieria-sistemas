class Nodo:
    def __init__(self, nombre, edad):
        # Parte amarilla
        self.nombre = nombre
        self.edad = edad
        #Parte morada
        self.siguiente = None

    def __str__(self):
        return f"{self.nombre} - {self.edad} años"