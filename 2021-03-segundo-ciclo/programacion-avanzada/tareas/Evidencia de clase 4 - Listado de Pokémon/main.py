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
print(pokemon['name'])