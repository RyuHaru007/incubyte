from fastapi import FastAPI

app = FastAPI(title="Incubyte Salary API")

@app.get("/health")
def health_check():
    return {"status": "ok"}