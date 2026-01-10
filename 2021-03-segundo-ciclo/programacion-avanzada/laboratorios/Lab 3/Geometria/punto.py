from cmath import sqrt

class Punto:
    def __init__(self, x, y, x2, y2):
        self.__coordenada_x = x
        self.__coordenada_y = y
        self.__x2 = x2
        self.__y2 = y2
    
    # Método para imprimir en pantalla las coordenadas ingresadas por el usuario
    def obtener_coordenada(self):
        return f"{self.__coordenada_x}, {self.__coordenada_y})  ({self.__x2}, {self.__y2})"
    
    # Método para determinar en que cuadrante se encuentra la primera coordenada ingresada
    def obtener_cuadrante(self):
        a = self.__coordenada_x
        b = self.__coordenada_y

        if a > 0 and b > 0:
            # En el primer cuadrante (x, y)
            return 'Cuadrante I'
        elif a < 0 and b > 0:
            # En el segundo cuadrante (-x, y)
            return 'Cuadrante II'
        elif a < 0 and b < 0:
            # En el tercer cuadrante (-x, -y)
            return 'Cuadrante III'
        elif a > 0 and b < 0:
            # En el cuarto cuadrate (x, -y)
            return 'Cuadrante IV'
    
    # Método para calcular en que cuadrante se encuentra el resultante de las dos coordenadas ingresadas
    def vector_resultante(self):
        x = self.__coordenada_x
        y = self.__coordenada_y
        x2 = self.__x2
        y2 = self.__y2

        resulx = (x2 - x)
        resuly = (y2 - y)

        if resulx > 0 and resuly > 0:
            return 'Cuadrante I'
        elif resulx < 0 and resuly > 0:
            return 'Cuadrante II'
        elif resulx < 0 and resuly < 0:
            return 'Cuadrante III'
        elif resulx > 0 and resuly < 0:
            return 'Cuadrante IV'
    
    # Método para saber cual es la distancia entre las dos coordenadas ingresadas
    def disctancia_puntos(self):
        x = self.__coordenada_x
        y = self.__coordenada_y
        x2 = self.__x2
        y2 = self.__y2

        distancia = sqrt(pow(x2 - x, 2) + pow(y2 - y, 2))
        return distancia