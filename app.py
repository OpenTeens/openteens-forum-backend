import schemas.user

from fastapi import FastAPI
from sqlalchemy import create_engine

...

app = FastAPI()
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)


@app.get("/")
def index():
    return "Hello World! "


@app.post("/v1/user/register")
async def register(data: schemas.user.RegisterModel):
    return data


@app.post("/v1/user/login")
def login(data: schemas.user.LoginModel):
    pass


if __name__ == '__main__':
    # Run the application of debug mode
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=41268)
