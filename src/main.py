import uvicorn
from fastapi import FastAPI
from src.api.users_me import users_me


app = FastAPI()
app.include_router(users_me)


# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0", port=8000)
