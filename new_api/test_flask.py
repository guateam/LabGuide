def test_home_page(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert rv.data == '{ "code": 1, "data": [], "msg": "success" }'
