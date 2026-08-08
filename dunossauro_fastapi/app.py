from http import HTTPStatus

from fastapi import FastAPI, HTTPException

from dunossauro_fastapi.schemas import (
    Message,
    UserDB,
    UserList,
    UserPublic,
    UserSchema,
)

app = FastAPI()

database = []


@app.get('/', response_model=Message, tags=["Hello World"])
def read_root():
    return {'message': 'Hello world!'}


@app.post('/users/', response_model=UserPublic, tags=["Users"])
def create_user(user: UserSchema):
    user_with_id = UserDB(id=len(database) + 1, **user.model_dump())
    database.append(user_with_id)

    return user_with_id


@app.get('/users/', response_model=UserList, tags=["Users"])
def read_users():
    return {'users': database}


@app.put('/users/{user_id}', response_model=UserPublic, tags=["Users"])
def update_user(user_id: int, user: UserSchema):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Usuario nao encontrado'
        )

    user_with_id = UserDB(id=len(database), **user.model_dump())
    print(user_with_id)

    database[user_id - 1] = user_with_id

    return user_with_id


@app.delete('/users/{user_id}', response_model=Message, tags=["Users"])
def delete_user(user_id: int):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Usuario nao encontrado'
        )

    del database[user_id - 1]

    return {'message': 'Usuario deletado com sucesso'}
