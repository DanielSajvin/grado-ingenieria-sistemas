from nodo import Nodo

class Pila:
    def __init__(self, max = -1):
        self.tope = None
        self.tamaño = 0
        self.max = max

    def insertar(self, cadena):
        if self.max == -1 or self.tamaño < self.max:
            nueva_cadena = Nodo(cadena)
            nueva_cadena.siguiente = self.tope
            self.tope = nueva_cadena
            self.tamaño += 1 
        else:
            raise Exception('Desbordamiento de pila')

    def recorrer(self):
        def cambiar(exp):
            if len(exp) == 0:
                return exp
            else:
                return cambiar(exp[1:]) + exp[0]
        aux = self.tope
        resul = ''
        for x in range(self.tamaño):
            if aux == None:
                break
            else:
                resul = resul + str(aux)
                aux = aux.siguiente
        print(end=''+cambiar(resul))