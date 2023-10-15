import requests
from jsonschema import validate
from config import BASE_URL
from utils.utils import load_schema


def test_create_user():
    data = {
        "name": "morpheus",
        "job": "leader"
    }

    response = requests.post(f'{BASE_URL}/api/users/', json=data)

    assert response.status_code == 201
    assert response.json()['name'] == data['name']
    assert response.json()['job'] == data['job']

def test_create_user_validate_schema():
    schema = load_schema('post_users_response.json')
    data = {
        "name": "morpheus",
        "job": "leader"
    }

    response = requests.post(f'{BASE_URL}/api/users/', json=data)

    validate(response.json(), schema)
