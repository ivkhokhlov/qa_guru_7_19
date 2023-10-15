def test_get_facts_list_not_empty(catfact_request):
    response = catfact_request('GET', '/facts')
    resonse_data = response.json()

    assert response.status_code == 200
    assert len(resonse_data['data']) > 0


def test_get_facts_per_page_count(catfact_request):
    response = catfact_request('GET', '/facts')
    resonse_data = response.json()

    assert response.status_code == 200
    assert len(resonse_data['data']) == resonse_data['per_page']