from fastapi import FastAPI
from models import Base
from database import engine
from routes import schemes, user

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(schemes.router)
app.include_router(user.router)

@app.get("/")
def home():
    return {"message": "Government Schemes API is running!"}