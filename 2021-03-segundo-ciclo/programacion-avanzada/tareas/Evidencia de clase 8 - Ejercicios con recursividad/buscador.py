def buscador(numero, elemento):
    if lista[elemento] == numero:
        return numero
    else:
        return f"{lista[elemento]} -> {buscador(numero, elemento + 1)}"

# Bloque principal
lista = [150, 90, 80, 15, 6]
print('Se tiene la lista [150, 90, 80, 15, 6]')
numero = int(input('Ingrese el número a buscar: '))
r = buscador(numero, 0)
print(r)