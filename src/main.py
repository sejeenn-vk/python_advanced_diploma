from fastapi import FastAPI
from src.api.users_me import users_me
from src.core.models.db_helper import db_helper

app = FastAPI()
app.include_router(users_me)
