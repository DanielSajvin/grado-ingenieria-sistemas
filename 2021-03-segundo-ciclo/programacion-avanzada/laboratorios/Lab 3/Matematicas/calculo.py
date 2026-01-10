from math import factorial
class Calculo:
    def __init__(self, numero):
        self.__numero = numero
    
    # Metodo para calcular el factorial de un numero
    def calcular_factorial(self):
        res = factorial(self.__numero)
        return res
    
    # Metodo para saber si el numero es primo o no 
    def es_primo(self):
        if self.__numero < 2:
            return False
        for i in range(2, self.__numero):
            if self.__numero % i == 0:
                return False
        return True 
    
    # Metodo para obetenr la tabla de multiplicar del numero ingresado 
    def obtener_tabla_multiplicar(self):
        x = self.__numero
        print(f"Tabla de {x}")
        for i in range(1, 11):
            print(f"{i}x{x} = {x * i}")

        # Intenté hacer esto pero solo me mostraba la direccion de memoria :(
        #for i in range(1, 11):
         #   res = f"{i}x{x} = {x*i}"
        #return res

    # Metodo para obtener todos lo numeros por los cuales es divisible el número ingresado
    def obtener_divisibles(self):
        x = self.__numero
        print(f"Factores de {x}: ")
        for i in range(1, x+1):
            if x % i == 0:
                print(i)
        # Aquí también intenté hacer esto pero igual solo me mostraba la dirección de memoria :(
        #cont = 0
        #for divisible in range(1, self.__numero+1):
         #   if self.__numero % divisible == 0:
          #      #return divisible
           #     cont += 1
            #    return divisible
        
            

