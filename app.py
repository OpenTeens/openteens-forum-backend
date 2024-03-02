from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return "Hello World! "


if __name__ == '__main__':
    # Run the application of debug mode
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
