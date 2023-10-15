import requests
from jsonschema import validate

from config import BASE_URL
from utils.utils import load_schema


def test_update_user(reqres_request):
    user_id = 1
    data = {
        "name": "morpheus",
        "job": "leader"
    }

    response = reqres_request('PATCH', f'/api/users/{user_id}', json=data)

    assert response.status_code == 200
    assert response.json()['name'] == data['name']
    assert response.json()['job'] == data['job']


def test_update_user_validate_schema(reqres_request):
    user_id = 1
    schema = load_schema('patch_users_response.json')
    data = {
        "name": "morpheus",
        "job": "leader"
    }

    response = reqres_request('PATCH',f'/api/users/{user_id}', json=data)

    validate(response.json(), schema)
