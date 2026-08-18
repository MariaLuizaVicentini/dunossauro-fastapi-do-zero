from http import HTTPStatus

from dunossauro_fastapi.schemas import UserPublic


def test_login_for_acess_token(client):

    # preparar

    # acao

    # verificao
    ...


def test_create_user_sucess(client):
    payload = {
        'username': 'malu',
        'email': 'test@malu.com',
        'password': 'vodoeprajacu',
    }

    response = client.post('/users/', json=payload)
    assert response.status_code == HTTPStatus.OK


def test_create_integrity_error(client, user):
    response = client.post(
        '/users',
        json={
            'username': 'Teste',
            'email': 'fausto@example.com',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.CONFLICT
    assert response.json() == {'detail': 'Username ou email ja existe'}


def test_read_users_sucess(client, token):
    response = client.get(
        '/users',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'id': 1,
                'username': 'Teste',
                'email': 'teste@test.com',
            },
        ],
    }


def test_read_users_with_users_sucess(client, user, token):
    user_schema = UserPublic.model_validate(user).model_dump()

    response = client.get('/users', headers={'Authorization': f'Bearer {token}'})

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': [user_schema]}


def test_update_user_success(client, user, token):
    payload = {
        'username': 'malu',
        'email': 'test@malu.com',
        'password': 'vodoeprajacu',
    }

    response = client.put(
        '/users/1', json=payload, headers={'Authorization': f'Bearer {token}'}
    )

    assert response.status_code == HTTPStatus.OK


def test_update_integrity_error(client, user, token):
    client.post(
        '/users',
        json={
            'username': 'fausto',
            'email': 'fausto@example.com',
            'password': 'secret',
        },
    )

    response = client.put(
        f'/users/{user.id}',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'username': 'fausto',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )

    assert response.status_code == HTTPStatus.CONFLICT
    assert response.json() == {'detail': 'Username ou email ja existe'}


def test_delete_user_success(client, user):
    message_success = {'message': 'Usuario deletado com sucesso'}

    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == message_success


def test_delete_user_error(client):
    message_success = {'detail': 'User nao encontrado'}

    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == message_success


def test_get_token(client, user):
    response = client.post(
        '/token',
        data={'username': user.email, 'password': user.clean_password},
    )
    token = response.json()

    assert response.status_code == HTTPStatus.OK
    assert token['token_type'] == 'Bearer'
    assert 'access_token' in token
