class Comprador:
    def __init__(self, nombre, edad, memebresia):
        self.__nombre = nombre
        self.__edad = edad
        self.__membresia = memebresia
    
    def verificar_acceso(self):
        resultado = True
        if self.__edad >= 18 and self.__membresia == "Si":
            resultado = True
        else:
            resultado = False
        return resultado
    
    def verificar_precio(self):
        if self.__edad >= 60:
            precio = 25.00
        else:
            precio = 45.00
        return precio
    
    def dar_poporopos(self):
        resultado = True
        if self.__membresia == "Si":
            pop = True
        else:
            pop = False
        return pop
    
    def __str__(self):
        if self.__membresia == "Si":
            membresia = 'Miembro del club'
        else:
            membresia = 'No hay membresia'
        return f"Nombre: ({self.__nombre}) - Edad: ({self.__edad}) - {membresia}"