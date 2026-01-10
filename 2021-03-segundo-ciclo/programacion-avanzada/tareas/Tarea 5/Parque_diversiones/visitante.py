import random

class Visitante:
    def __init__(self, nombre, altura):
        self.__nombre = nombre
        self.__altura = altura
        self.__pase = 0
       
    def comprar(self):
        self.__pase = random.randint(100, 1000)
        id = f"El ID de su pase es: {self.__pase}"
        return id
    
    def revocar(self):
        self.__pase = None
        return 'Su pase fue revocado'
        
    def verificar(self, altura):
        if self.__altura >= altura and self.__pase != None:
            permiso = '!Disfrute de la atracción!'
        else:
            permiso = '!No cumples con la altura o No tienes un pase de atracciones :( ! '
        return permiso
        
    def __str__(self):
        m = self.__altura / 100
        
        if self.__pase == None:
            pase = 'No hay pase de atracciones'
        else:
            pase = f"ID del pase: ({self.__pase})"

        return f"Nombre: ({self.__nombre}) - Altura: ({m}) m - {pase}"