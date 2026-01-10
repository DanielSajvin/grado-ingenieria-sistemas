class Pelicula:
    def __init__(self, pelicula, duracion, nombre, pais):
        self.__pelicula = pelicula
        self.__duracion = duracion
        self.__snombre = nombre
        self.__spais = pais
        self.__favorita = False

    def favorita(self):
        self.__favorita = True
    
    def nombre_pelicula(self):
        return self.__pelicula
    
    def estudio(self):
        return self.__snombre
    
    def __str__(self):
        if self.__favorita == False:
            favorita = 'No es Favorita'
        else:
            favorita = 'Película Favorita'
        return f"Nombre película: ({self.__pelicula}) - Duración: ({self.__duracion} s) - Estudio cinematográfico: ({self.__snombre}) País: {self.__spais} - {favorita}"
