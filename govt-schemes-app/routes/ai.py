from fastapi import APIRouter, Depends
from pydantic import BaseModel
from groq import Groq
from sqlalchemy.orm import Session
from database import get_db
from models import Scheme
from dotenv import load_dotenv
import os

router = APIRouter()

def get_groq_client():
    load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))
    return Groq(api_key=os.getenv("GROQ_API_KEY"))

class UserQuery(BaseModel):
    message: str
    language: str = "english"

@router.post("/match-schemes")
def match_schemes(query: UserQuery, db: Session = Depends(get_db)):
    client = get_groq_client()

    schemes = db.query(Scheme).all()

    schemes_text = ""
    for scheme in schemes:
        schemes_text += f"""
        - {scheme.name}: {scheme.description}
          Benefits: {scheme.benefits}
          Eligibility: {scheme.eligibility}
          Apply at: {scheme.apply_link}
        """

    prompt = f"""
    You are a helpful assistant that matches Indian citizens to government schemes.

    Available schemes:
    {schemes_text}

    User's situation: {query.message}

    Tell them:
    1. Which schemes they qualify for
    2. Why they qualify
    3. How to apply

    Keep response simple and clear.
    Respond in {query.language} language.
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    return {
        "response": response.choices[0].message.content,
        "language": query.language
    }