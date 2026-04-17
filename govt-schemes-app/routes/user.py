from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import User
from pydantic import BaseModel

router = APIRouter()

class UserProfile(BaseModel):
    age: int
    income_level: str
    category: str
    state: str
    occupation: str
    preferred_language: str

@router.post("/user/profile")
def save_profile(profile: UserProfile, db: Session = Depends(get_db)):
    user = User(**profile.model_dump())
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"message": "Profile saved!", "user_id": user.id}