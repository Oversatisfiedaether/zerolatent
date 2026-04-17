from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Scheme

router = APIRouter()

@router.get("/schemes")
def get_all_schemes(db: Session = Depends(get_db)):
    schemes = db.query(Scheme).all()
    return schemes

@router.get("/schemes/{id}")
def get_scheme(id: int, db: Session = Depends(get_db)):
    scheme = db.query(Scheme).filter(Scheme.id == id).first()
    return scheme