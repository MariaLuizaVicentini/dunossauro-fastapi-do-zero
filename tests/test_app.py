from fastapi.testclient import TestClient

from dunossauro_fastapi.app import app


def test_root_deve_retornar_pla_mundo():
    client = TestClient(app)

    response = client.get('/')

    # assert é tipo "garanta"
    assert response.json() == {'message': 'Hello world!'}
