import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles


app = FastAPI()
app.mount("/static", StaticFiles(directory="static/"), name="static")


@app.get("/", response_class=HTMLResponse)
async def get_main():
    with open("static/index.html", "r", encoding="utf-8") as file:
        html_data = file.read()
    return HTMLResponse(content=html_data)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
