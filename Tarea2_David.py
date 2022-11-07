import requests
url = "https://pokeapi.co/api/v2/pokemon-shape/"
r = requests.get(url)
data = r.json()

print("Escriba la forma del pokemon que desea: ")
for i in data["results"]:
    print(i["name"])
forma = input("Elección 2: ")

for i in data["results"]:
    if forma == i["name"]:
        print("\t"+i["name"])
        link = i['url']
        data_nombres = requests.get(link).json()
        for poke_nombres in data_nombres["pokemon_species"]:
            print("\t\t"+ poke_nombres["name"])

