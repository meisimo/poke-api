from fastapi import FastAPI

from api.berries.routes import route as berries_route

app = FastAPI()


berries_route(app)
