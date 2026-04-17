from sqlalchemy import Column, Integer, String, JSON
from database import Base

class Scheme(Base):
    _tablename_ = "schemes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    eligibility = Column(JSON)
    benefits = Column(String)
    apply_link = Column(String)

class User(Base):
    _tablename_ = "users"

    id = Column(Integer, primary_key=True, index=True)
    age = Column(Integer)
    income_level = Column(String)
    category = Column(String)
    state = Column(String)
    occupation = Column(String)
    preferred_language = Column(String)