import uvicorn
from fastapi import FastAPI


app = FastAPI()


@app.get('/')
async def home():
    return {'message': 'hello, world'}


if __name__ == '__main__':
    uvicorn.run(app)
