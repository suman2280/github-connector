from fastapi import FastAPI
from app.routes.handler import router

app = FastAPI(title="GitHub Connector API")

app.include_router(router)


@app.get("/")
def root():
    return {"message": "GitHub Connector is running..."}