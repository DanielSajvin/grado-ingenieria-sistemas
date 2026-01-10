from vehiculo import Vehiculo


class Pickup(Vehiculo):
    def __init__(self, marca, linea, modelo, kilometraje):
        super().__init__(marca, linea, modelo)
        self.kilometraje = kilometraje

    def imprimir(self):
        print(self)

    def __str__(self):
        return f"{super().__str__()} - {self.kilometraje}"