class Circulo: 
    def __init__(self, radio):
        self.radio = radio
        self.calcular_area3()

    def calcular_area3(self):
        area = (self.radio * self.radio) * 3.1416
        print(f"\nEl area del circulo es: {area}\n")
    
    def __str__(self):
        return(f"{self.calcular_area3}")
