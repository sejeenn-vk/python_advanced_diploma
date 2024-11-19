from typing import Annotated

import uvicorn
from fastapi import FastAPI, Header
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles


app = FastAPI()
app.mount("/static", StaticFiles(directory="static/"), name="static")


@app.get("/")
async def get_main(api_key: Annotated[str | None, Header()] = 'test'):
    return {"api_key": api_key}


@app.get("/api/users/me")
async def login():
    return {
        "result": "true",
        "user": {
            "id": 1,
            "name": "test",
            "followers": [{"id": 2, "name": "Nikolay"}],
            "following": [{"id": 3, "name": "Tatyana"}],
        },
    }


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
