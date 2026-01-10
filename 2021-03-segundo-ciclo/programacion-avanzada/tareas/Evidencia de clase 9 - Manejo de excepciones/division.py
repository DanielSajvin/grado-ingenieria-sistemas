resultado = 0
try: 
    numerador = int(input('Ingrese el numerador: '))
    denominador = int(input('Ingrese el denominador: '))
    resultado = numerador / denominador
except ValueError: 
    print('¡¡Ingrese números!!')
except ZeroDivisionError:
    print('¡¡Los ceros no pueden dividir!!')
except: 
    print('Lo siento, no sé que paso :(')
else:
    print(f"La division es: {resultado}")
    