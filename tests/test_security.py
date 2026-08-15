from jwt import decode

from dunossauro_fastapi.security import ALGORITHM, SECRET_KEY, create_access_token


def test_jwt():
    data = {'test': 'test'}
    token = create_access_token(data)

    decoded = decode(token, SECRET_KEY, algorithms=ALGORITHM)
    assert decoded['test'] == data['test']
    assert 'exp' in decoded  # testa se o valor de exp foi add ao tokenj
