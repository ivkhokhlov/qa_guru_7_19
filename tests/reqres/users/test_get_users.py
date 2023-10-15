import pytest
from jsonschema import validate

from utils.utils import load_schema


def test_list_of_users_not_empty(reqres_request):
    response = reqres_request('GET', '/api/users')

    assert response.status_code == 200
    assert len(response.json()['data']) > 0


@pytest.mark.parametrize('per_page', list(range(1, 10)))
def test_pagination_per_page(per_page, reqres_request):
    response = reqres_request('GET', '/api/users', params={'per_page': per_page})

    assert response.status_code == 200
    assert len(response.json()['data']) == per_page
    assert response.json()['per_page'] == per_page


def test_pagination_per_page_default_value(reqres_request):
    response = reqres_request('GET', '/api/users', params={'per_page': 0})

    assert response.status_code == 200
    assert len(response.json()['data']) == 6
    assert response.json()['per_page'] == 6


@pytest.mark.parametrize('page', list(range(1, 10)))
def test_pagination_page_number(page, reqres_request):
    response = reqres_request('GET', '/api/users', params={'per_page': 1, 'page': page})

    assert response.status_code == 200
    assert response.json()['page'] == page
    assert response.json()['data'][0]['id'] == page


def test_get_single_user(reqres_request):
    user_id = 2

    response = reqres_request('GET', f'/api/users/{user_id}')

    assert response.status_code == 200
    assert response.json()['data']['id'] == user_id


def test_get_nonexisted_user(reqres_request):
    user_id = 1000

    response = reqres_request('GET', f'/api/users/{user_id}')

    assert response.status_code == 404


def test_get_validate_schema(reqres_request):
    schema = load_schema('get_users_response.json')

    response = reqres_request('GET', '/api/users')

    validate(response.json(), schema)
