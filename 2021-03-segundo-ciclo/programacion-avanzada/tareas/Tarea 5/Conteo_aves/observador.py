import datetime
aves = []
class Observador:
    def __init__(self, aves):
        self.__aves = aves
    
    def dia():
        hoy = datetime.datetime.today()
        if hoy.weekday() == 0:
            return f"Lunes: ({aves[0]})"
        elif hoy.weekday() == 1:
            return f"Martes: ({aves[1]})"        
        elif hoy.weekday() == 2:
            return f"Miercoles: ({aves[2]})"
        elif hoy.weekday() == 3:
            return f"Jueves: ({aves[3]})"
        elif hoy.weekday() == 4:
            return f"Viernes: ({aves[4]})"
        elif hoy.weekday() == 5:
            return f"Sabado: ({aves[5]})"
        elif hoy.weekday() == 6:
            return f"Domingo: ({aves[6]})"
     
    def agregar(self):
        aves.append(self.__aves)
    
    def ultima_semana():
        sum = 0
        for x in aves:
            sum = sum + x
        return(f"Total aves vistas: {sum}")
    
    def contar_aves():
        return (f"Lunes: ({aves[0]}) Martes: ({aves[1]}) Miércoles: ({aves[2]}) Jueves: ({aves[3]}) Viernes: ({aves[4]}) Sabado: ({aves[5]}) Domingo: ({aves[6]})")
    
    def dia_ocupado():
        for x, y in enumerate(aves):
            if y >= 5:
                if  x == 0:
                        print (f"Lunes: ({aves[x]})")
                elif x == 1:
                        print (f"Martes: ({aves[x]})")        
                elif x == 2:
                        print (f"Miercoles: ({aves[x]})")
                elif x == 3:
                        print (f"Jueves: ({aves[x]})")
                elif x == 4:
                        print (f"Viernes: ({aves[x]})")
                elif x == 5:
                        print (f"Sabado: ({aves[x]})")
                elif x == 6:
                        print (f"Domingo: ({aves[x]})")

    def __str__(self):
        return f"{self.__aves}"