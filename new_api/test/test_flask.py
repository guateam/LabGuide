import json

import pytest

from new_api.main import app


@pytest.fixture()
def client():
    app.config['TESTING'] = True
    return app.test_client()


def test_flask(client):
    rv = client.get('/')
    data = json.loads(rv.data)
    assert data['code'] == 1
