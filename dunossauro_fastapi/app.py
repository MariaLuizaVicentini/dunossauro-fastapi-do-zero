from fastapi import FastAPI

from dunossauro_fastapi.schemas import Message

app = FastAPI()


@app.get('/', response_model=Message)
def read_root():
    return {'message': 'Hello world!'}
