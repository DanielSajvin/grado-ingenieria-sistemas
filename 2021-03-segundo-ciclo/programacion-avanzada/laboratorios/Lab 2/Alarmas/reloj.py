class Reloj:
    def __init__(self, nombre, horas, minutos, segundos):
       self.nombre = nombre
       self.horas = horas
       self.minuto = minutos
       self.segundo = segundos
       self.alarm = []
    
    def mod_hora(self, horas):
        self.horas = horas
    
    def mod_minuto(self, minutos):
        self.minuto = minutos
    
    def mod_segundo(self, segundos):
        self.segundo = segundos

    def __str__(self):
        return(f"Alarma: {self.nombre} Hora: {self.horas} Minuto: {self.minuto} Segundos: {self.segundo}")
