from http import HTTPStatus

from fastapi import FastAPI

from dunossauro_fastapi.schemas import Message, UserSchema, UserPublic

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK ,response_model=Message)
def read_root():
    return {'message': 'Hello world!'}


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    return user 