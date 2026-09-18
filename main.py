from fastapi import FastApi
from config import APP_VERSION

app = FastApi(title="student-api", version=APP_VERSION)

@app.get("/health")
def health ():
    return {"status": "ok"}