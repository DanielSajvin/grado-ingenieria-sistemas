import requests
import os
import random

clear = lambda: os.system('cls')

def buscar_pokemon(numero):
    pokemon = requests.get(f"https://pokeapi.co/api/v2/pokemon/{numero}/").json()
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
    input('Presiona una tecla para continuar... ')
      

def listar_pokemon():
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

def listar_tipos():
  clear()
  while True:
      print("Listado de tipos")
      respuesta = requests.get('https://pokeapi.co/api/v2/type').json()
      for j, i in enumerate (respuesta['results']):
        print(f"{j+1}- {respuesta['results'][j]['name']}")
      op = int(input("Presione 1 para regresar... "))
      if op == 1:
        break

def pokemon_aleatorio():
  aleatorio = random.randint(1, 898)
  buscar_pokemon(aleatorio)
  input('Presione una tecla para continuar...')

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
  #---------------------------------------------------------------------------------------
  if opcion == 1:
    listar_pokemon()
  elif opcion == 2:
   clear()
   listar_tipos()
  elif opcion == 3:
    clear()
    n = int(input('Ingrese el número de Pokémon: '))
    buscar_pokemon(n)
    input('Presione una tecla para continuar...')
  elif opcion == 4:
    pokemon_aleatorio()
  elif opcion == 5:
    break
  else:
    continue
