from fastapi import APIRouter
from pydantic import BaseModel
from groq import Groq
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(__file__).parent.parent / ".env")

router = APIRouter()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SCHEMES = """
1. PM Kisan - Farmers get Rs 6000/year. Eligibility: small/marginal farmers.
2. Mudra Loan - Business loan up to Rs 10 lakh. Eligibility: small business owners.
3. PM Scholarship - Rs 36000/year for students. Eligibility: children of ex-servicemen.
4. Ayushman Bharat - Free health insurance Rs 5 lakh. Eligibility: below poverty line families.
5. PM Awas Yojana - Housing assistance. Eligibility: families without pucca house.
"""

class UserQuery(BaseModel):
    message: str
    language: str = "english"

@router.post("/match-schemes")
def match_schemes(query: UserQuery):
    prompt = f"""
    You are a helpful assistant that matches Indian citizens to government schemes.
    
    Available schemes:
    {SCHEMES}
    
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