from fastapi import FastAPI
from routes.carta import user

app = FastAPI()

app.include_router(user)

