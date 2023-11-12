from sqlalchemy import Column, Integer, String, Float
from datetime import datetime
from .base import Base


class Student(Base):
    __tablename__ = 'Student'
    
    id = Column(Integer, primary_key=True)
    last_name = Column(String)
    first_name = Column(String)
    major = Column(String)
    gpa = Column(Float)
    
    def __init__(self, last_name, first_name, major, gpa):
        self.id = self.generate_id()
        self.last_name = last_name
        self.first_name = first_name
        self.major = major
        self.gpa = gpa

    # Generate id depends on student amount and start year
    def generate_id(self):
        current_year = datetime.now().year
        session = self.get_session()
        current_student_count = session.query(Student).count()
        return int(str(current_year)[-2:] + str(current_student_count + 1).zfill(4))

    @classmethod
    def get_columns_name(cls):
        names = ["id", "last_name", "first_name", "major", "gpa"]
        return names