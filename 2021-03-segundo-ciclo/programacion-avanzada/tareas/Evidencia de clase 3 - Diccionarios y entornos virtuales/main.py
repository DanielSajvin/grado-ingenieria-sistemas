import requests

respuesta = requests.get('https://pokeapi.co/api/v2/pokemon/25')

pokemon = respuesta.json()

print(pokemon['name'])