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
    assert response.status_code == HTTPStatus.OK


def test_read_users_sucess(client):
    mockUsers = {'users': [{'id': 1, 'username': 'malu', 'email': 'test@malu.com'}]}

    response = client.get('users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == mockUsers


def test_update_user_success(client):

    payload = {
        'username': 'malu',
        'email': 'test@malu.com',
        'password': 'vodoeprajacu',
    }

    response = client.put('/users/1', json=payload)

    assert response.status_code == HTTPStatus.OK


def test_update_user_error(client):

    payload = {
        'username': 'malu',
        'email': 'test@malu.com',
        'password': 'vodoeprajacu',
    }

    response = client.put('/users/3', json=payload)

    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_user_success(client):
    message_success = {'message': 'Usuario deletado com sucesso'}

    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == message_success


def test_delete_user_error(client):
    message_success = {'detail': 'Usuario nao encontrado'}

    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == message_success
