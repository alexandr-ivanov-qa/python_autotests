import requests
url_1 = 'https://api.pokemonbattle.ru/v2'
token = 'dd2510f71749449394b9c5323e43add9'
header = {'Content-Type':'application/json','trainer_token':f'{token}'}

body_pokemon_creation = {
    "name": "generate",
    "photo_id": -1
                        }

body_pokemon_name_change = {
    "pokemon_id": "43020",
    "name": "Plumbumbum",
    "photo_id": 3
}

body_add_pokeball = {
    "pokemon_id": "43020"
}

'''response_pokemon_creation = requests.post(url = f'{url_1}/pokemons', headers = header, json = body_pokemon_creation)
print(response_pokemon_creation.text)

message = response_pokemon_creation.json()['message']
print(message)'''

response_pokemon_name_change = requests.put(url = f'{url_1}/pokemons', headers = header, json = body_pokemon_name_change)
print(response_pokemon_name_change.text)

response_add_pokeball = requests.post(url = f'{url_1}/trainers/add_pokeball', headers = header, json = body_add_pokeball)
print(response_add_pokeball.text)