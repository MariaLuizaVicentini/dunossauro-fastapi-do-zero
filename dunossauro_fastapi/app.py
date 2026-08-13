from http import HTTPStatus

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from dunossauro_fastapi.database import get_session
from dunossauro_fastapi.models import User
from dunossauro_fastapi.schemas import (
    Message,
    UserList,
    UserPublic,
    UserSchema,
)

app = FastAPI()


@app.get('/', response_model=Message, tags=['Hello World'])
def read_root():
    return {'message': 'Hello world!'}


@app.post('/users/', response_model=UserPublic, tags=['Users'])
def create_user(user: UserSchema, session: Session = Depends(get_session)):

    user_db = session.scalar(
        select(User).where((User.email == user.email) | (User.username == user.username))
    )

    if user_db:
        if user_db.username == user.username:
            raise HTTPException(
                status_code=HTTPStatus.CONFLICT,
                detail=f'Username já existe: {user_db.username}',
            )
        elif user_db.email == user.email:
            raise HTTPException(
                status_code=HTTPStatus.CONFLICT,
                detail=f'Email já existe: {user_db.email}',
            )

    user_db = User(username=user.username, email=user.email, password=user.password)
    session.add(user_db)
    session.commit()
    session.refresh(user_db)

    return user_db


@app.get('/users/', response_model=UserList, tags=['Users'])
def read_users(
    limit: int = 10, offset: int = 0, session: Session = Depends(get_session)
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
    user_db.password = user.password
    session.add(user_db)
    session.commit()
    session.refresh(user_db)

    return user_db


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
