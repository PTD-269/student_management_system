from data.table import Student

class StudentModel:
    def __init__(self):
        super().__init__()

    def get_all(self, sort_needed):
        session = Student.get_session()
        students = session.query(Student).order_by(sort_needed).all()
        session.close()
        return students
    
    def get_student(self, id):
        session = Student.get_session()
        found_student = session.query(Student).filter_by(id=id).first()
        session.close()
        return found_student
    
    # Insert student to Student table in Database
    def insert(self, last_name, first_name, major, gpa):
        id = self.generate_id()
        student = Student(id, last_name, first_name, major, gpa)
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
        session.query(Student).filter(Student.id==id).update({
        'last_name': last_name, 
        'first_name': first_name,
        'major': major,
        'gpa': gpa 
        })
        session.commit()
        session.close()
    # Generate id depends on student amount and start year
    def generate_id(self):
        from datetime import datetime
        current_year = datetime.now().year
        try:
            session = Student.get_session()
            last_student_id = str(session.query(Student.id).order_by(Student.id.desc()).first()[0])[-4:]
            last_student_id = int(last_student_id)
            session.close()
        except Exception:
            last_student_id = -1
        return int(str(current_year)[-2:] + str(last_student_id + 1).zfill(4))
    
