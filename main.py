from fastapi import FastAPI
from config import APP_VERSION

app = FastAPI(title="student-api", version=APP_VERSION)

@app.get("/health")
def health ():
    return {"status": "healthy"}

@app.get("/students")
def list_students ():
    return [{"id":1, "name": "Jose"}, {"id":2, "name": "Rembe"}]