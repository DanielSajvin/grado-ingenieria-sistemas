from cola import Cola
import os
import datetime

print('-----   PAGOS ACADÉMICOS   -----\n')
estudiantes = Cola()
atendidos = 0
tiemposs = []
t_monto = []

while True:
    os.system('cls')
    print('MENÚ\n')
    print('1. Ingresar estudiante')
    print('2. Atender estudiante')
    print('3. Ver a todos los estudiantes')
    print('4. Infomración de la cola')
    print('5. Definir el número máximo de estudiantes')
    print('6. Salir')
    opcion = int(input('Ingrese una opción: '))

    if opcion == 1:
        os.system('cls')
        nombre = input('Ingresar nombre: ')
        carne = input('Ingresar no. de carné: ')
        monto = float(input('Ingrese el monto a pagar: '))
        tiempo = datetime.datetime.now()
        try:
            estudiantes.insertar(nombre, carne, monto, tiempo)
        except Exception as error:
            print(f"Ocurrió un error:\n{error}")
        os.system('pause')
        
    elif opcion == 2:
        os.system('cls')
        en_cola = datetime.datetime.now() - estudiantes.frente.tiempo

        try:
            print(f"Atendiendo a: {estudiantes.frente.nombre}\nTiempo en cola: {en_cola}")
            tiemposs.append(estudiantes.frente.tiempo)
            t_monto.append(estudiantes.frente.monto)
            nodo = estudiantes.eliminar()
            atendidos += 1
        except Exception as error:
            print(f"Ocurrió un error:\n{error}\nNO hay estudiantes")
        
        os.system('pause')
    elif opcion == 3:
        os.system('cls')
        resultados = estudiantes.recorrer()
        print(f"Cola de estudiantes:\n{resultados}")
        #print(resultado)
        os.system('pause')
    elif opcion == 4:
        os.system('cls')
        t_medio = 0
        for x in tiemposs:
            t_medio += x
        t_medio = t_medio / 2

        montos = 0
        for x in t_monto:
            montos += x

        print(f"Estudantes atendidos: {atendidos}\nMonto total de todas las transacciones: {montos}\nTiempo medio en que se tarda en atender a un estudiante: {t_medio}\nEstudiantes en cola: {estudiantes.tamaño}")

        #nodo = estudiantes.eliminar()
        #print(f"Total de estudiantes atendidos: {nodo}")
        #print(estudiantes)
        os.system('pause')
    elif opcion == 5:
        os.system('cls')
        if estudiantes.tamaño > 0:
            print('Tienes que ingresar el limite antes de ingresar un estudiante  :/')
        
        else:

            print('A continuación ingrese el maximo de estudiantes que pueden hacer cola,')
            print('si desea que la cola no tenga límite ingrese -1, de lo contrario ingrese otro número.')
            limite = int(input('\nIngrese el límite: '))
            estudiantes = Cola(limite)
        os.system('pause')
        
    elif opcion == 6:
        break
    else:
        continue
