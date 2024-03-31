import requests
import pytest

Url = 'https://api.pokemonbattle.me/v2'
Token = '0a1d5c53f988ba9e71b96c3922c3270d'
Headers = {'Content-Type' : "application/json"}

# Проверяем что приходит код 200 на тренеров
def test_trainers_get_is_200():
    assert requests.get(url = f'{Url}/trainers', headers = Headers).status_code == 200

# Проверяем что приходит имя тренера
def test_get_my_trainer_info():
    assert 'cypresslol' in requests.get(url = f'{Url}/trainers', headers = Headers, params = {'trainer_id' : 2227}).text

# Проверяем что приходит имя тренера по другому
def test_get_my_trainer_info_json():
    assert requests.get(url = f'{Url}/trainers', headers = Headers, params = {'trainer_id' : 2227}).json()['data'][0]['trainer_name'] == 'cypresslol'


