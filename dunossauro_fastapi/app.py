from http import HTTPStatus

from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from dunossauro_fastapi.database import get_session
from dunossauro_fastapi.models import User
from dunossauro_fastapi.schemas import (
    Message,
    Token,
    UserList,
    UserPublic,
    UserSchema,
)
from dunossauro_fastapi.security import (
    create_access_token,
    get_current_user,
    get_password_hash,
    verify_password,
)

app = FastAPI()


@app.post('/token', response_model=Token, tags=['Users'])
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(get_session),
):
    user = session.scalar(select(User).where(User.email == form_data.username))

    if not user:
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED,
            detail='Email ou senha nao cadastrados no banco',
        )

    if not verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED, detail='Email ou senha incorretos'
        )

    access_token = create_access_token(data={'sub': user.email})

    return {'access_token': access_token, 'token_type': 'Bearer'}


@app.post('/users/', response_model=UserPublic, tags=['Users'])
def create_user(user: UserSchema, session: Session = Depends(get_session)):

    user_db = session.scalar(
        select(User).where((User.email == user.email) | (User.username == user.username))
    )

    user_db = User(
        username=user.username,
        email=user.email,
        password=get_password_hash(user.password),
    )

    try:
        session.add(user_db)
        session.commit()
        session.refresh(user_db)

        return user_db
    except IntegrityError:
        raise HTTPException(
            status_code=HTTPStatus.CONFLICT, detail='Username ou email ja existe'
        )


@app.get('/users/', response_model=UserList, tags=['Users'])
def read_users(
    limit: int = 10,
    offset: int = 0,
    session: Session = Depends(get_session),
    current_user=Depends(get_current_user),
):
    users = session.scalars(select(User).limit(limit).offset(offset))
    return {'users': users}


@app.put('/users/{user_id}', response_model=UserPublic, tags=['Users'])
def update_user(user_id: int, user: UserSchema, session: Session = Depends(get_session)):
    user_db = session.scalar(select(User).where(User.id == user_id))

    if not user_db:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User nao encontrado'
        )

    user_db.username = user.username
    user_db.email = user.email
    user_db.password = get_password_hash(user.password)

    try:
        session.add(user_db)
        session.commit()
        session.refresh(user_db)

        return user_db
    except IntegrityError:
        raise HTTPException(
            detail='Username ou email ja existe',
            status_code=HTTPStatus.CONFLICT,
        )


@app.delete('/users/{user_id}', response_model=Message, tags=['Users'])
def delete_user(user_id: int, session: Session = Depends(get_session)):
    user_db = session.scalar(select(User).where(User.id == user_id))

    if not user_db:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User nao encontrado'
        )

    session.delete(user_db)
    session.commit()

    return {'message': 'Usuario deletado com sucesso'}
