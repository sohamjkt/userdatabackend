from fastapi import FastAPI
from fastapi.responses import JSONResponse
import json
import os

app= FastAPI()

@app.get("/serve")
def serve():
    file_path=file_path = os.path.join(os.path.dirname(__file__), "userdata.json")
    with open(file_path, "r") as f:
        users = json.load(f)
    return JSONResponse(content=users)