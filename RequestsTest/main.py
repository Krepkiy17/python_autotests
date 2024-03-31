import requests

Url = 'https://api.pokemonbattle.me/v2'
Token = '0a1d5c53f988ba9e71b96c3922c3270d'
Headers = {'Content-Type' : "application/json", 'trainer_token': Token}
PokemonID = '15391'

# Создание покемона
pokemonsBody = {
    "name": "MisterTwister",
    "photo": "https://dolnikov.ru/pokemons/albums/069.png"
}
print(requests.post(url = f'{Url}/pokemons', headers = Headers, json = pokemonsBody).text)

# Смена имени покемона
pokemonsBody = {
    "pokemon_id": PokemonID,
    "name": "OldMister",
    "photo": "https://dolnikov.ru/pokemons/albums/018.png"
}
print(requests.put(url = f'{Url}/pokemons', headers = Headers, json = pokemonsBody).text)

# Ловим в покебол
pokemonsBody = {
    "pokemon_id": PokemonID
}
print(requests.post(url = f'{Url}/trainers/add_pokeball', headers = Headers, json = pokemonsBody).text)