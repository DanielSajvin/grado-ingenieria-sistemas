class Cuadrado:
    def __init__(self, lado):
        self.lado = lado
        self.calcular_area2()

    def calcular_area2(self):
        area = self.lado * self.lado
        
        print(f"\nEl area del cuadrado es: {area}\n")
    
    def __str__(self):
        return(f"{self.calcular_area2}")