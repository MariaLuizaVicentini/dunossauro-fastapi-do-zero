from http import HTTPStatus

from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from dunossauro_fastapi.models import User
from dunossauro_fastapi.schemas import (
    Message,
    UserDB,
    UserList,
    UserPublic,
    UserSchema,
)
from dunossauro_fastapi.settings import Settings

app = FastAPI()

database = []


@app.get('/', response_model=Message, tags=['Hello World'])
def read_root():
    return {'message': 'Hello world!'}


@app.post('/users/', response_model=UserPublic, tags=['Users'])
def create_user(user: UserSchema):
    engine = create_engine(Settings().DATABASE_URL)
    session = Session(engine)

    db_user = session.scalar(
        select(User).where((User.email == user.email) | (User.username == user.username))
    )

    if db_user:
        if db_user.username == user.username:
            raise HTTPException(
                status_code=HTTPStatus.CONFLICT,
                detail=f'Username já existe: {db_user.username}',
            )
        elif db_user.email == user.email:
            raise HTTPException(
                status_code=HTTPStatus.CONFLICT,
                detail=f'Email já existe: {db_user.email}',
            )

    db_user = User(username=user.username, email=user.email, password=user.password)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user


@app.get('/users/', response_model=UserList, tags=['Users'])
def read_users():
    return {'users': database}


@app.put('/users/{user_id}', response_model=UserPublic, tags=['Users'])
def update_user(user_id: int, user: UserSchema):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Usuario nao encontrado'
        )

    user_with_id = UserDB(id=len(database), **user.model_dump())

    database[user_id - 1] = user_with_id

    return user_with_id


@app.delete('/users/{user_id}', response_model=Message, tags=['Users'])
def delete_user(user_id: int):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Usuario nao encontrado'
        )

    del database[user_id - 1]

    return {'message': 'Usuario deletado com sucesso'}
