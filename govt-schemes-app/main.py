from dotenv import load_dotenv
import os

# Load .env FIRST before anything else
from fastapi import FastAPI
from models import Base
from database import engine
from routes import schemes, user, ai

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(schemes.router)
app.include_router(user.router)
app.include_router(ai.router)

@app.get("/")
def home():
    return {"message": "Government Schemes API is running!"}