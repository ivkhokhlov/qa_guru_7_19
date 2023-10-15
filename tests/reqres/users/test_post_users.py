from jsonschema import validate

from utils.utils import load_schema


def test_create_user(reqres_request):
    data = {
        "name": "morpheus",
        "job": "leader"
    }

    response = reqres_request('POST', '/api/users/', json=data)

    assert response.status_code == 201
    assert response.json()['name'] == data['name']
    assert response.json()['job'] == data['job']


def test_create_user_validate_schema(reqres_request):
    schema = load_schema('post_users_response.json')
    data = {
        "name": "morpheus",
        "job": "leader"
    }

    response = reqres_request('POST', '/api/users/', json=data)

    validate(response.json(), schema)
