from vehiculo import Vehiculo

class Camioneta(Vehiculo):
    def __init__(self, marca, linea, modelo, es_chocado):
        super().__init__(marca, linea, modelo)
        self.es_chocado = es_chocado

    def imprimir(self):
        print(self)

    def __str__(self):
        return f"{super().__str__()} - {self.es_chocado}"