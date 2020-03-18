import json

import pytest

from new_api.main import app


@pytest.fixture()
def client():
    app.config['TESTING'] = True
    return app.test_client()


def test_server_state(client):
    rv = client.get('/')
    data = json.loads(rv.data)
    assert data['code'] == 1
    assert data['msg'] == 'success'
    assert not data['data']


def test_require_login(client):
    rv = client.get('/require_login')
    data = json.loads(rv.data)
    assert data['code'] == 0
    assert data['msg'] == 'you must login'
    assert not data['data']


def test_doc_definitions(client):
    rv = client.get('/')
    data = json.loads(rv.data)
    assert data['code'] == 1
    assert data['msg'] == 'success'
    assert not data['data']
