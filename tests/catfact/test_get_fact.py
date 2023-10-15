def test_get_fact_length(catfact_request):
    response = catfact_request('GET', '/fact')
    resonse_data = response.json()

    assert response.status_code == 200
    assert len(resonse_data['fact']) == resonse_data['length']