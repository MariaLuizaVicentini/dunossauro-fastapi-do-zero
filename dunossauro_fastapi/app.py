from http import HTTPStatus

from fastapi import FastAPI

from dunossauro_fastapi.routers import auth, users
from dunossauro_fastapi.schemas import Message

app = FastAPI(title='Peeey!')

app.include_router(auth.router)
app.include_router(users.router)


@app.get('/', status_code=HTTPStatus.OK, response_model=Message, tags=['hello'])
def read_root():
    return {'message': 'Olá mundo'}
