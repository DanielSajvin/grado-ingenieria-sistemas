from datetime import datetime
from movimiento import Movimiento 
class Cuenta:
    def __init__(self, titular, numero, saldo):
        self.titular = titular
        self.numero = numero
        self.movimientos = []
        self.saldo = 0.0
        self.depositar(saldo)
    
    # Metodo mutador
    def depositar(self, cantidad):
        # Crear nuevo movimiento
        fecha = datetime.now()
        saldo_final = self.saldo + cantidad
        nuevo_movimiento = Movimiento(fecha, cantidad, saldo_final)
        # nombre_lista.append(registro)
        self.movimientos.append(nuevo_movimiento)
        self.saldo = saldo_final

    # Metodo mutador
    def retirar(self, cantidad):
        fecha = datetime.now()
        saldo_final = self.saldo - cantidad
        nuevo_movimiento = Movimiento(fecha, cantidad, saldo_final)
        # nombre_lista.append(registro)
        self.movimientos.append(nuevo_movimiento)
        self.saldo = saldo_final 

    # Metodo accesor
    def mostrar_movimientos(self):
        for movimiento in self.movimientos:
            print(movimiento)

    # Metodo accesor
    def mostrar_saldo(self):
        pass

    def __str__(self):
        return f"{self.titular} - {self.numero} - (Q. {self.saldo})"