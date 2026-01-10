from reloj import Reloj
import random

print('\n----- PROGRAME SU ALARMA -----\n')

alarmas = []
nu_alarm = 0

while True:
    print('1. Agregar nueva alarma')
    print('2. Ver alarmas activas')
    print('3. Alarma con tiempo aleatorio')
    print('4. Salir')
    opcion = int(input('Seleccione una opción: '))

    if opcion == 1:
        nomb = input('\nIngrese el nombre de la alarma: ')
        print('\nRecuerde ingresar las horas en formarto 24hrs.')
        print('Ejemplo si quiere programas su alarma a las 6 pm, seria a las 18hrs.')
        h = int(input('Ingrese la hora: '))
        print('\nRecuerde ingresar minutos de 0 a 59 únicamente')
        m = int(input('Ingrese minutos: '))
        print('\nRecuerde ingresar los segundo de 0 a 59 únicamente.')
        s = int(input('Ingresar segundo: '))

        alarm = Reloj(nomb, h, m, s)
        alarmas.append(alarm)

    elif opcion == 2:
        for num, x in enumerate(alarmas):
            print(f"{num + 1} - {x}")

        while True:
            print('\n1. Editar alarma existente\n2. Quitar alarma\n3. Salir') 
            op = int(input('Seleccione una opción: ')) 

            if op == 1:
                no_alarm = int(input('Ingrese el número de la alarma que desea editar: '))-1
                val = False
            
                for x, y in enumerate(alarmas):
                    if no_alarm == x:
                        val = True
                        break
                        
                if val == False:
                    input('LA ALARMA NO EXISTE') 
                else: 
                    while True:
                        print('Modificar alarma')
                        print('1. Modificar Hora\n2. Modificar Minutos\n3. Modificar segundos\n4. Salir')
                        op1 = ('Seleccione una opcion: ')
                   ##########################
                        if op1 == 1:
                            h = int(input('Ingrese hora: '))
                            Reloj.mod_hora(no_alarm, h)
                        
                        elif op1 == 2:
                            m = int(input('Ingrese minutos: '))
                            Reloj.mod_minuto(no_alarm, m)
                    
                        elif op1 == 3:
                            s = int(input('Ingrese segundos: '))
                            Reloj.mod_segundo(no_alarm, s)
                    
                        elif op1 == 4:
                            break
                        else:
                            input('NO EXISTE')
                            break
                    
            elif op == 2:    
                no_alarm = int(input('Ingrese el numero de la alarma que desea quitar: '))-1
                val = False
                
                for x, y in enumerate(alarmas):
                    if no_alarm == x:
                        val = True
                        break

                if val == False:
                   input('NO EXISTE')
                else:
                    pass

            elif op == 3:
                break
            else:
                input('NO EXISTE')


    elif opcion == 3:
        nombre = (f"Alarma aleatoria: {nu_alarm}")
        nu_alarm+=1
        h = random.randint(1, 24)
        m = random.randint(0, 59)
        s = random.randint(0, 59)
        alarma = Reloj(nombre, h, m, s)

    elif opcion == 4:
        break
    continue