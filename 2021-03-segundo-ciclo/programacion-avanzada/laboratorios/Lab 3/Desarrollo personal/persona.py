#
class Persona:
    def __init__(self, nombre, edad, capital, peso, altura):
        self.__nombre = nombre
        self.__edad = edad
        self.__capital = capital
        self.__peso = peso
        self.__altura = altura
    
    def es_mayor_edad(self):
        resultado = True
        if self.__edad >= 18:
            resultado = True
        else:
            resultado = False
        return resultado
    
    def calcular_IMC(self):
        m = self.__altura / 100
        lb = self.__peso / 2.205
        IMC = lb / (m * m) 

        return IMC
    
    def obtener_composicion_corporal(self):
        imc = self.calcular_IMC()
        if imc < 18.5:
            return "Delgado"
        elif imc >= 18.5 and imc < 24.9:
            return "Normal"
        elif imc >= 24.9 and imc < 29.9:
            return "Sobrepeso"
        elif imc >= 29.9:
            return "Obeso"
    
    def calcular_capital_final(self, tasa_interes, años):
        capital_final = self.__capital * pow(1 + tasa_interes, años) 
        return capital_final