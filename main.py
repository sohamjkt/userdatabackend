from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app= FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins, change this for production!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/serve")
def serve():
    file_path=file_path = os.path.join(os.path.dirname(__file__), "userdata.json")
    with open(file_path, "r") as f:
        users = json.load(f)
    return JSONResponse(content=users)