from pwdlib import PasswordHash

pwd_context = PasswordHash.recommended()


# le a senha e gera o hash da senha
def get_password_hash(password: str):
    return pwd_context.hash(password)


# valida se a senha pura bate com o hash do banco de dados
def verify_password(plain_password: str, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
