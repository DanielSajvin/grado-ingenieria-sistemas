class Triangulo:
    def __init__(self, altura, base):
        self.altura = altura
        self.base = base
        self.calcular_area()
    
    def calcular_area(self):
        area = (self. altura * self.base)
        total = area / 2
        print(f"\nEl area del triangulo es: {total}\n")
        
    def __str__(self):
        return(f"{self.calcular_area}")