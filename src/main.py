from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def get_main():
    return {"message": "Hello mazafaka"}
