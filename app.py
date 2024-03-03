import schemas.user

from sqlalchemy.orm import Session

from fastapi import FastAPI, Response

from sqlalchemy import select, create_engine

from models import Base, User

app = FastAPI()
engine = create_engine("sqlite+pysqlite:///db.sqlite", echo=True)

Base.metadata.create_all(engine)


@app.get("/")
def index():
    return "Hello World! "


@app.post("/v1/user/register")
async def register(data: schemas.user.RegisterModel):
    with Session(engine) as session:
        if session.scalar(select(1).where(User.username == data.username).limit(1)):
            return {
                "errcode": "USER_EXISTS",
                "uid": None
            }

        user = User(username=data.username, password=data.password)

        session.add(user)
        session.commit()
        session.refresh(user)

    return {
        "errcode": "OK",
        "uid": user.id
    }


@app.post("/v1/user/login")
def login(data: schemas.user.LoginModel, response: Response):
    with Session(engine) as session:
        selected = session.scalar(select(User).where(User.username == data.username))

        if selected is None:
            return {
                "errcode": "INVALID_LOGIN",
                "uid": None
            }

        if selected.password != data.password:
            return {
                "errcode": "INVALID_LOGIN",
                "uid": None
            }

        # The token/session feature has not been implemented yet.
        # So we just temporarily put username in cookies.

        # WARNING: User may edit their cookies to log in OTHERS accounts.

        response.set_cookie("user_token", f"token_of_user@{selected.username}")

        return {
            "errcode": "OK",
            "uid": selected.id
        }


if __name__ == '__main__':
    # Run the application of debug mode
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=41271)
