def test_delete_user(reqres_request):
    user_id = 1

    response = reqres_request('DELETE', f'/api/users/{user_id}')

    assert response.status_code == 204
    assert response.text == ''
