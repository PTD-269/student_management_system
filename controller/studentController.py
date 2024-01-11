from model.studentModel import StudentModel
class StudentController:
    def __init__(self, view):
        self.model = StudentModel()
        self.view = view
    
    def get_all_student(self, sort_needed):
        data = self.model.get_all(sort_needed)
        return data
    
    def get_student(self, id):
        id = int(id)
        data = self.model.get_student(id)
        return data

    def add_student(self, last_name, first_name, major, gpa):
        last_name = str(last_name).capitalize()
        first_name = str(first_name).capitalize()
        major = str(major).upper()
        gpa = float(gpa)
        major_condition = ["AI", "MKT", "SE", "MATH"]
        
        if (major in major_condition) and (0 <= gpa <= 4):
            self.model.insert(last_name, first_name, major, gpa)
    
    def delete_student(self, id):
        self.model.delete(id)

    def update_student_info(self, id, last_name, first_name, major, gpa):
        id = int(id)
        last_name = str(last_name).capitalize()
        first_name = str(first_name).capitalize()
        major = str(major).upper()
        gpa = float(gpa)

        major_condition = ["AI", "MKT", "SE", "MATH"]
        
        if (major in major_condition) and (0 <= gpa <= 4):
            self.model.edit(id, last_name, first_name, major, gpa)
    