def cadena_invertida(cadena):
    if len(cadena) == 0:
        return cadena
    else:
        return cadena_invertida(cadena[1:]) + cadena[0]

cadena = input('Ingrese una palabra: ')
r = cadena_invertida(cadena)
print(f"Palabra al revés: {r}")