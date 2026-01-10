class Cancion:
    def __init__(self, cancion, nombre, fecha):
        self.__cancion = cancion
        self.__nombre = nombre
        self.__fecha = fecha
        self.__favorita = False
    
    def favorita(self):
        self.__favorita = True
    
    def nombre_cancion(self):
        return self.__cancion
    
    def artista(self):
        return self.__nombre
    
    def __str__(self):
        if self.__favorita == False:
            favorita = 'No es favorita'
        else:
            favorita = 'Canción favorita'
        return f"Nombre canción: ({self.__cancion}) - Nombre artista: ({self.__nombre}) - Fecha lanzamiento: ({self.__fecha}) - {favorita}"