import uvicorn
from fastapi import FastAPI


app = FastAPI()


@app.get("/api/users/me")
async def get_users_me():
    return {
        "result": "true",
        "user": {
            "id": 1,
            "name": "Евгений Воронцов",
            "followers": [{"id": 2, "name": "Николай Воронцов"}],
            "following": [{"id": 3, "name": "Татьяна Воронцова"}],
        },
    }


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
