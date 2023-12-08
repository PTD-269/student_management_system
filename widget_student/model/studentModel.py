from data.table import Student

class StudentModel:
    def __init__(self):
        super().__init__()

    def get_all(self):
        session = Student.get_session()
        students = session.query(Student).all()
        session.close()
        return students
    
    # Insert student to Student table in Database
    def insert(self, last_name, first_name, major, gpa):
        student = Student(last_name, first_name, major, gpa)
        session = Student.get_session()
        session.add(student)
        session.commit()
        session.close()

    # Delete student depends on id to Student table in Database
    def delete(self, id):
        session = Student.get_session()
        session.query(Student).filter(Student.id==id).delete()
        session.commit()
        session.close()
    
    def edit(self, id, last_name, first_name, major, gpa):
        session = Student.get_session()

        session.close()

    def sort_name(self):
        session = Student.get_session()

        session.close()
    
 
    def sort_average_point(self):
        session = Student.get_session()

        session.close()
    
    def find_highest_scrore(self):
        session = Student.get_session()

        session.close()

