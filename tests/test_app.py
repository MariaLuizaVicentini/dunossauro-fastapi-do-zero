from http import HTTPStatus


def test_root_deve_retornar_pla_mundo(client):

    response = client.get('/')

    assert response.json() == {'message': 'Hello world!'}
    assert response.status_code == HTTPStatus.OK


def test_create_user_sucess(client):

    payload = {
        'username': 'malu',
        'email': 'test@malu.com',
        'password': 'vodoeprajacu',
    }

    response = client.post('/users/', json=payload)
    print(vars(response))
    assert response.status_code == HTTPStatus.CREATED


def test_read_users_sucess(client):
    mockUsers = {
        'users': [{'id': 1, 'username': 'malu', 'email': 'test@malu.com'}]
    }

    response = client.get('users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == mockUsers
