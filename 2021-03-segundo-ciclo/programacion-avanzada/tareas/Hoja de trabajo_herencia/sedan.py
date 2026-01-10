from vehiculo import Vehiculo

class Sedan(Vehiculo):
    def __init__(self, marca, linea, modelo, propietario):
        super().__init__(marca, linea, modelo)
        self.propietario = propietario
    
    def imprimir(self):
        print(self)

    def __str__(self):
        return f"{super().__str__()} - {self.propietario}"
        