from pila import Pila

print('-----   CADENA AL REVÉS   -----\n')
cadena = Pila()
print('Para ingresar una frase tiene que hacerlo letra por letra, cuando')
print('ya no desee ingresar letras, escriba: "-"\n')

while True:

    letra = input('Ingrese una letra: ')
    cadena.insertar(letra)

    if letra == '-':
        # Cuando el usuario ingrese "-" se dejarán de pedir letras, por naturaleza de la pila el ultimo en entrar es el ultimo en salir, de por sí va a mostrar la palabra en orden inverso
        cadena.recorrer()
        break
    else:
        continue
