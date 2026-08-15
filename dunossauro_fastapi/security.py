from pwdlib import PasswordHash

pwd_context = PasswordHash.recommended()


def get_password_hash(password: str):
    """
        Recebe uma senha em texto puro e retorna o hash gerado para ela.
    """
    return pwd_context.hash(password)


# valida se a senha pura bate com o hash do banco de dados
def verify_password(plain_password: str, hashed_password):
    """
        Verifica se a senha em texto puro corresponde ao hash informado
        True = Corresponde
        False = Nao corresponde
    """
    return pwd_context.verify(plain_password, hashed_password)
