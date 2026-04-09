from fastapi import FastAPI

from app import models
from app.database import engine
from app.routers import employees

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Incubyte Salary API")

app.include_router(employees.router)

@app.get("/health")
def health_check():
    return {"status": "ok"}