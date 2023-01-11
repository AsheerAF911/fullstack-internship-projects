import requests

choice = input("Enter Pokemon name: ")
choice = choice.lower()

url =  f"https://pokeapi.co/api/v2/pokemon/{choice}"

req = requests.get(url)

data =req.json()

print(f"Name of Pokemon: {data['name']}")
print(f"Height: {data['height']}")
print("Abilities:")
for ability in data['abilities']:
    print(ability['ability']['name'])

