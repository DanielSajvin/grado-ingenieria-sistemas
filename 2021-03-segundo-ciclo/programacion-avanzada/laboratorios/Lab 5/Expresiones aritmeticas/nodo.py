class Nodo:
    def __init__(self, expresion):
        self.expresion = expresion
        self.siguiente = None
    
    def __str__(self):
        return self.expresion