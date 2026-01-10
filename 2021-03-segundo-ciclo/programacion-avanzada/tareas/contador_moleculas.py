print("--- Contador de moléculas ---\n")
print("Instrucciones: ")
print("Debe ingresar una cadena de ADN, solo debe ingresar la letra con que se identifica cada nucleótido: ")
print("Adenina (A), Citosina (C), Guanina (G) y Timina (T).\n")
# Se le pide al usuario que ingrese una cadena de 15 caracteres 
print("Ingrese la cadena de ADN (compuesta por 15 caracteres): ")
adn = (input())
# Acá se el llamado a esta función que sirve para contar, en este caso para contar las letras de la cadena que ingrese el usuario
# las va a contar y luego me va a mostrar cuantas veces aparece determinada letra en la cadena que ingresó el usuario 
from typing import Counter
cont = Counter(adn)
print("\nResultado: ")
# Acá ya solo se muestran los resultados que la función nos de, y se le imprime en pantalla al usuario 
print("Adenina (A): ", cont['A'],  "\nCitosina (C): ", cont['C'], "\nGuanina (G): ", cont['G'], "\nTimina (T): ", cont['T'], "\n")