# Primer paso:
# Definir una clase.
class Estudiante:
    def __init__(self, n, c, e):
        # Funciones del metodo constructor
        # 1. Agrega valores iniciales o valores por defecto
        #2 Asignar valores de los objetos 
        self.nombre = n
        self.carnet = c
        self.edad = e
        self.notas = []

    def saludar(self):
        print(f"¡Hola soy {self.nombre}!")
        print(f"Mi carnet es {self.carnet}")

    def agregar_nota(self, nota):
        self.notas.append(nota)   
        
    def es_aprobado(self):
        promedio = 0 
        for nota in self.notas:
            promedio = promedio + nota
        promedio = promedio / len(self.notas)
        return promedio >= 65  

    def mensaje_aprobado(self): 
        if self.es_aprobado():
            print("El estudiante ha aprobado")
        else:
            print("El estudiante perdio :(")