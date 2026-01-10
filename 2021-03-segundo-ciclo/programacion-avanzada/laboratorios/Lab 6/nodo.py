import datetime

class Nodo:
    def __init__(self, nombre, carne, monto, tiempo):
        self.nombre = nombre
        self.carne = carne
        self.monto = monto
        self.tiempo = tiempo
        self.siguiente = None
    
    def __str__(self):
        return f"Nombre: {self.nombre} - No. Carné: {self.carne} - Monto: {self.monto} - Tiempo en cola: {datetime.datetime.now() - self.tiempo}"