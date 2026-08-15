from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from jwt import encode
from pwdlib import PasswordHash

pwd_context = PasswordHash.recommended()

SECRET_KEY = 'your-secret-key'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def get_password_hash(password: str):
    """
    Recebe uma senha em texto puro e retorna o hash gerado para ela.
    """
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password):
    """
    Verifica se a senha em texto puro corresponde ao hash informado
    True = Corresponde
    False = Nao corresponde
    """
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict):
    """
    Cria um token jwt de acesso (bearer) a partir dos dados fornecidos,
    e adiciona o tempo de expiracao
    """
    to_encode = data.copy()

    expire = datetime.now(tz=ZoneInfo('UTC')) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )
    to_encode.update({'exp': expire})

    encode_jwt = encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt
