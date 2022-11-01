import os
os.system("cls")
import requests
url="https://pokeapi.co/api/v2/pokemon/"
r=requests.get(url)
data=r.json()

