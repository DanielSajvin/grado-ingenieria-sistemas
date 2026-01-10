class Vehiculo:
    def __init__(self, marca, linea, modelo):
        self.marca = marca
        self.linea = linea
        self.modelo = modelo
    
    def __str__(self):
        return f"{self.marca} {self.linea} {self.modelo}"