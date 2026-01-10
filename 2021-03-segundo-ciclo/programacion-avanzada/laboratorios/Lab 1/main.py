import requests
import os
import random

clear = lambda: os.system('cls')

def buscar_pokemon(numero): #Funcion que muestra los datos del Pokémon
    pokemon = requests.get(f"https://pokeapi.co/api/v2/pokemon/{numero}/").json()
    #deb = requests.get(f"https://pokeapi.co/api/v2/type/{numero}/").json()
    especie = requests.get(pokemon['species']['url']).json()
    evoluciones = requests.get(especie['evolution_chain']['url']).json()
    clear()
    
    print("Datos del Pokémon:")
    print(f"{pokemon['name']}")
    print(f"No. {pokemon['id']}")
    print(" ")

    print("Evoluciones del Pokémon: ")
    print(evoluciones['chain']['species']['name'])
    if evoluciones['chain']['evolves_to'] != None:
      print(evoluciones['chain']['evolves_to'][0]['species']['name'])
      if evoluciones['chain']['evolves_to'][0]['evolves_to'] != None:
        print(evoluciones['chain']['evolves_to'][0]['evolves_to'][0]['species']['name'])
    print(" ")

    print("Descripción del Pokémon: ")
    for x, y in enumerate(especie['flavor_text_entries']):
      if especie['flavor_text_entries'][x]['language']['name'] == 'es':
         print(f"{especie['flavor_text_entries'][x]['flavor_text']}")
         break
    print(" ")

    print("Puntos de combate: ")
    for x, y in enumerate(pokemon['stats']): 
      print(f"{pokemon['stats'][x]['stat']['name']} = {pokemon['stats'][x]['base_stat']}")
    print(" ")

    print("Datos relevantes:")
    print(f"Altura: {pokemon['height'] / 10} m")
    print(f"Peso: {pokemon['weight'] / 10} kg")
    print(" ")
    
    print("Debilidades: ")
    for x, y in enumerate (pokemon['types']):
      debilidad = requests.get(pokemon['types'][x]['type']['url']).json()
    for a, b in enumerate (debilidad['damage_relations']['double_damage_from']):
      print(f" {debilidad['damage_relations']['double_damage_from'][a]['name']}")
    print(" ")

    print("Tipos:")
    for item in pokemon['types']:
      print(f"- {item['type']['name']}")
    input('Presiona una tecla para continuar... ')
 
def segun_tipo(tipo): #Funcion que muestra el listado de tipos de Pokémon
  tiposww = requests.get(f"https://pokeapi.co/api/v2/type/{tipo}/").json()
  print('¿Qué tipo de Pokémon desea ver? ')
  for x, y in enumerate(tiposww['pokemon']):
    print(f"{x+1}  {tiposww['pokemon'][x]['pokemon']['name']}")
  input('Presione una tecla para continuar...')     

def listar_pokemon(): #Funcion que basicamente seria un segundo menú, que permite avanzar de página y también la opción de buscar un Pokémon en especifico
  clear()
  pagina = 1
  while True:
     print("Listado de Pokémon:") 
     offset = (pagina - 1) * 20
     url = f"https://pokeapi.co/api/v2/pokemon?offset={offset}&limit=20"
     respuesta = requests.get(url).json()
     resultados = respuesta['results']
     for x, pokemon in enumerate(resultados):
       #url1 = respuesta['results'][x]['url']
       #admurl = requests.get(url1).json()
       print(f"{x + offset + 1} {pokemon['name']}")
     print('\nAcciones:')
     print('1- Página anterior.')
     print('2- Página siguiente.')
     print('3- Seleccionar Página.')
     print('4- Seleccionar Pokémon')
     print('5- Regresar.')
     opcion = int(input('Seleccione una acción: '))

     if opcion == 1:
       pagina = 1 if pagina == 1 else pagina -1
     elif opcion == 2:
      pagina = pagina+1
     elif opcion == 3:
       pagina = int(input('Ingrese Número de Página: '))
     elif opcion == 4:
       numero = int(input('Ingrese un Pokémon: '))
       if numero > offset & numero <= (offset + 20):
         buscar_pokemon(numero)
       else:
         print("Numero inválido")
         input('Presione una tecla para continuar... ')
      
     elif opcion == 5:
       print("Presione 5 para continuar...")
       break

def listar_tipos(): #Funcion que permite buscar Pokémon según su tipo
  clear()
  while True:
      print("Listado de tipos")
      respuesta = requests.get('https://pokeapi.co/api/v2/type').json()
      for j, i in enumerate (respuesta['results']):
        print(f"{j+1}- {respuesta['results'][j]['name']}")
       #------------------------------------------------------------
      print("1- ¿Qué tipo de Pokémon desea ver?")
    
      print("2- Presione para salir... ")
      opc = int(input("Seleccione lo que desea hacer: "))
      if opc == 1:
        tipo = int(input("Seleccione el tipo de Pokémon que desea ver: "))
        clear()
        segun_tipo(tipo)
      elif opc == 2:
        break

def pokemon_aleatorio(): #Funcion que muestra un Pokémon aleatorio al usuario 
  aleatorio = random.randint(1, 898)
  buscar_pokemon(aleatorio)
  input('Presione una tecla para continuar...')

pagina = 1
while True: #Esta parte es el menú principal, en el cual solo se hace el llamado a las funcines anteriormente mencionadas 
  clear()
  print('Bienvienido al Pokédex')
  print('Acciones:')
  print('1- Listado de Pokémon.')
  print('2- Ver Pokémon por tipo.')
  print('3- Buscar Pokémon.')
  print('4- ¡Sorpréndeme con uno aleatorio!')
  print('5- Salir.')
  opcion = int(input('Seleccione una acción: ')) 
  #--------------------------------------------------------------------------------------- *estas lineas son para no confundirme :c
  if opcion == 1:
    listar_pokemon()
  elif opcion == 2:
   clear()
   listar_tipos()
  elif opcion == 3:
    clear()
    n = int(input('Ingrese el número de Pokémon: '))
    buscar_pokemon(n)
  
  elif opcion == 4:
    pokemon_aleatorio()
  elif opcion == 5:
    break
  else:
    continue
