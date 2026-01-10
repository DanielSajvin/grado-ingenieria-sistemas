class Nodo:
    def __init__(self, letra):
        self.letra = letra
        self.siguiente = None

    def __str__(self):
        return self.letra
