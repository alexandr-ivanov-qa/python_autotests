import requests
import pytest

url_1 = 'https://api.pokemonbattle.ru/v2'
token = 'dd2510f71749449394b9c5323e43add9'
TRAINER_ID1 = '4520'
header = {'Content-Type':'application/json','trainer_token':f'{token}'}

def test_status_code200():
    response = requests.get(url = f'{url_1}/trainers', params = {'trainer_id':TRAINER_ID1})
    assert response. status_code == 200

def response_content():
    response_get = requests.get(url = f'{url_1}/trainers', params = {'trainer_id':TRAINER_ID1})
    assert response_get.json()["data"][0]["trainer_name"] == 'Elerium'

@pytest.mark.parametrize('key, value', [('name','paras'), ('trainer_id', TRAINER_ID1),('id', '43022')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{url_1}/pokemons', params = {'trainer_id': TRAINER_ID1})
    assert response_parametrize.json()["data"][0][key] == value