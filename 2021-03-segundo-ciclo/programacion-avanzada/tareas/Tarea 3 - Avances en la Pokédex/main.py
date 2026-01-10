import requests
import os
import random

clear = lambda: os.system('cls')

# TODO:
#   1- Hacer uso de procedimientos y funciones.
#   2- Evitar repetir código.
#   3- No usuar variables globales.
pagina = 1
while True:
  clear()
  print('Bienvienido al Pokédex')
  print('Acciones:')
  print('1- Listado de Pokémon.')
  print('2- Ver Pokémon por tipo.')
  print('3- Buscar Pokémon.')
  print('4- ¡Sorpréndeme con uno aleatorio!')
  print('5- Salir.')
  opcion = int(input('Seleccione una acción: ')) 
  if opcion == 1:
    clear()
    pagina = 1
    while True:
     print("Listado de Pokémon:") 
     #pagina 1
    
     offset = (pagina - 1) * 20
     url = f"https://pokeapi.co/api/v2/pokemon?offset={offset}&limit=20"
     respuesta = requests.get(url).json()
     resultados = respuesta['results']
     for x, pokemon in enumerate(resultados):
       url1 = respuesta['results'][x]['url']
       admurl = requests.get(url1).json()
       print(f"{admurl['id']} {pokemon['name']}")
    # TODO:
    #   1- Visualizar los Pokémon en bloques de 20.
    #   2- Poder navegar hacia las páginas anteriores.
    #   3- Poder navegar hacia las páginas siguientes.
    #   4- Seleccionar un Pokémon por su número en la Pokédex.
    #   5- Regresar al menú principal.
     print('\nAcciones:')
     print('1- Página anterior.')
     print('2- Página siguiente.')
     print('3- Seleccionar Página.')
     print('4- Seleccionar Pokémon')
     print('5- Regresar.')
    #arreglar los indies,seleccionar un pokemon por su numero
    #listar todos los tipos nombre y name
     opcion = int(input('Seleccione una acción: '))
     if opcion == 1:
       pagina = 1 if pagina == 1 else pagina -1
     elif opcion == 2:
      pagina = pagina+1
     elif opcion == 3:
       pagina = int(input('Seleccione una accion'))
     elif opcion == 4:
       busqueda = int(input('Ingrese un Pokémon: '))-1
       cont = 0
       for x in respuesta['results']:
         if cont == busqueda:
            url1 = respuesta['results'][cont]['url']
            admurl = requests.get(url1).json()
            clear()
            print(f"Nombre Pokémon: {admurl['name']}\nNúmero Pokémon: {admurl['id']}\nAltura: {admurl['height']/10}m\nPeso: {admurl['weight']/10}kg")
            break 
         cont +=1
     elif opcion == 5:  
       break
  elif opcion == 2:
    clear()
    while True:
      print("Listado de tipos")
      respuesta = requests.get('https://pokeapi.co/api/v2/type').json()
      for j, i in enumerate (respuesta['results']):
        print(f"{respuesta['results'][j]['name']}")
        op = int(input("Menú\n1. Salir"))
      if op == 1:
        break
      # TODO:
      #    1- Listar todos los tipos disponibles.
      #   2- Preguntar al usuario seleccionar un tipo.
      #   3- Mostrar un listado de pokémon en base al tipo. 
  elif opcion == 3:
    clear()
    opcion = int(input('Ingrese el número del Pokémon:'))
    pokemon = requests.get(f"https://pokeapi.co/api/v2/pokemon/{opcion}/").json()
    clear()
    print("Datos del Pokémon:")
    print(f"{pokemon['name']}")
    print(f"No. {pokemon['id']}")
    print("Datos relevantes:")
    print(f"Altura: {pokemon['height'] / 10} m")
    print(f"Peso: {pokemon['weight'] / 10} kg")
    # TODO:
    #   1- Mostrar las habilidades en español.
    print("Habilidades:")
    for item in pokemon['abilities']:
      print(f"- {item['ability']['name']}")
    # TODO:
    #   1- Mostrar los tipos en español.
    print("Tipos:")
    for item in pokemon['types']:
      print(f"- {item['type']['name']}")
    # TODO:
    #   1- Agregar las debilidades por tipo.
    input('Presione una tecla para continuar...')
  elif opcion == 4:
    pokedex = random.randint(1, 898)
    pokemon = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokedex}/").json()
    clear()
    print("Datos del Pokémon:")
    print(f"{pokemon['name']}")
    print(f"No. {pokemon['id']}")
    print("Datos relevantes:")
    print(f"Altura: {pokemon['height'] / 10} m")
    print(f"Peso: {pokemon['weight'] / 10} kg")
    print("Habilidades:")

    for item in pokemon['abilities']:
      print(f"- {item['ability']['name']}")
    print("Tipos:")
    for item in pokemon['types']:
      print(f"- {item['type']['name']}")
    input('Presione una tecla para continuar...')
  elif opcion == 5:
    break
  else:
    continue
