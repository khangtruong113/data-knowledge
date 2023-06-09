from .db import Base
from sqlalchemy import String, Column, Integer, Date
from datetime import date
from sqlalchemy.dialects.postgresql import ENUM

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    age = Column(Integer)
    date_joined = Column(Date)
    level = Column(Integer)
    gmail = Column(String(50))

    def __init__(self, first_name: str, last_name: str, age: int, date_joined: date, level: int, gmail: str):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.date_joined = date_joined
        self.level = level
        self.gmail = gmail

