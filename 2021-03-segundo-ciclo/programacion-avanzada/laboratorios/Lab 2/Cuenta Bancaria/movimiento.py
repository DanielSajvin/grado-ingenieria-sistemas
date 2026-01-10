class Movimiento:
    def __init__(self, f, m, s):
        self.fecha = f
        self.monto = m
        self. saldo = s
    
    def __str__(self):
        return f"FECHA: {self.fecha} - MONTO: {self.monto} - SALDO FINAL: (Q. {self.saldo})"