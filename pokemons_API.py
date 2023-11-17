import requests

# https://pokeapi.co/

url = "https://pokeapi.co/api/v2/pokemon/ditto"

response = requests.get(url)
output = response.json()["abilities"]

for ability in output:
	print(ability["ability"]["name"])


