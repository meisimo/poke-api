from fastapi import FastAPI

from api.berries.routes import route as berries_route

app = FastAPI()


# TODO: Pending to remove
@app.get("/")
async def read_main():
    return {"msg": "Hello World"}

berries_route(app)
