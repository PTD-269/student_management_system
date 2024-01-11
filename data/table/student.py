from sqlalchemy import Column, Integer, String, Float

from .base import Base
from sqlalchemy import desc

class Student(Base):
    __tablename__ = 'Student'
    
    id = Column(Integer, primary_key=True)
    last_name = Column(String)
    first_name = Column(String)
    major = Column(String)
    gpa = Column(Float)
    
    def __init__(self, id, last_name, first_name, major, gpa):
        self.id = id
        self.last_name = last_name
        self.first_name = first_name
        self.major = major
        self.gpa = gpa


