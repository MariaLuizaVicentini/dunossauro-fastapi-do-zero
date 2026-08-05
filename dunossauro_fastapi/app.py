from http import HTTPStatus

from fastapi import FastAPI

from dunossauro_fastapi.schemas import Message, UserDB, UserPublic, UserSchema

app = FastAPI()

database = []


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Hello world!'}


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema): # "user" é uma instancia da classe UserSchema, portanto é um obj pydantic
    user_with_id = UserDB(
        id=len(database) + 1, 
        **user.model_dump() # aqui pegamos o obj pydantic e transformamos ele em um dict python nativo, pra manipular com colchetes
    )
    print(type(user_with_id))
    return user_with_id
