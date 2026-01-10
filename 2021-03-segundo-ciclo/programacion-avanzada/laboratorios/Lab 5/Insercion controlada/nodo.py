class Nodo:
    def __init__(self, nombre, editorial, isbn):
        self.nombre = nombre
        self.editorial = editorial
        self.isbn = isbn
        self.siguiente = None
    
    def __str__(self):
        return f"{self.nombre}, {self.editorial}, {self.isbn}"
