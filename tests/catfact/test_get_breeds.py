def test_get_breeds_not_empty(catfact_request):
    response = catfact_request('GET', '/breeds')

    assert response.status_code == 200
    assert len(response.json()) > 0
