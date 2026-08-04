from http import HTTPStatus

from fastapi.testclient import TestClient

from dunossauro_fastapi.app import app


def test_root_deve_retornar_pla_mundo():
    """
        Esse teste tem 3 etapas AAA:
            A - Arranjo: organiza dados necessários para teste
            A - Agir/Acao: que executa o teste
            A - Afirmacao: garante que A é A
    """
    # arranjo: inicializando cliente HTTP passando como parm minha app
    client = TestClient(app)

    # acao: o client inicializado faz request pra read_root
    response = client.get('/')

    # afirmarcao: assert é tipo "garanta"
    assert response.json() == {'message': 'Hello world!'}
    assert response.status_code == HTTPStatus.OK
