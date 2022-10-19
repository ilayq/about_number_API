from fastapi import FastAPI
from number_analysis import Number
from api_key_generator import generate_api_key


app = FastAPI()


@app.get('/')
async def root():
    return {"message": 'This is about_number API, if you have API key send GET to /number/api_key=<your api '
                       'key>&number=<your number>, else send GET to /generate_api?user_name=<your user name>'}


@app.get('/number/')
def send_data(api_key: str, number: int):
    with open('apikeys.txt') as f:
        lines = [line.strip() for line in f]
        if api_key not in lines:
            return {'message': 'invalid API key'}
    num = Number(number)
    return num.to_json()


@app.get('/generate_api/{user_name}')
async def send_api_key(user_name: str):
    return {'api': generate_api_key(user_name)}
