from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title = "Inkwell", description = "A simple web application built with FastAPI and React", version = "0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "Inkwell is running"}