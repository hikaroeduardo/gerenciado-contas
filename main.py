from fastapi import FastAPI

from sqlalchemy import create_engine

app = FastAPI()

engine = create_engine("sqlite:///database.db")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", port=3333, reload=True)