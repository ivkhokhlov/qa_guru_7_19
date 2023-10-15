import requests

from config import BASE_URL


def test_delete_user():
    user_id = 1

    response = requests.delete(f'{BASE_URL}/api/users/{user_id}')

    assert response.status_code == 204
    assert response.text == ''
