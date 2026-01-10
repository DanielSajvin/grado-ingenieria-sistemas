import requests

respuesta = requests.get('https://pokeapi.co/api/v2/pokemon?limit=150')
diccionario = respuesta.json()
resultados = diccionario['results']
print("Listado de Pokémon")
print("------------------------")

for x, pokemon in enumerate(resultados):
    print(f"{x + 1} - {pokemon['name']}")

print("¿Qué Pokémon desea ver?")
opcion = int(input())

respuesta1 = requests.get(f"https://pokeapi.co/api/v2/pokemon/{opcion}/")
pokemon = respuesta1.json()

print(f"Nombre del Pokémon: {pokemon['name']}")
print(f"Pokémon Número: {pokemon['id']}")
print(f"Altura: {pokemon['height']} m")
print(f"Peso: {pokemon['weight']} kg")

i = 0

for x in pokemon['types']:
    print(f"Tipo: {pokemon['types'][i]['type']['name']}")
    i+= 1