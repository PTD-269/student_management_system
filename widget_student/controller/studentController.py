from widget_student.model import StudentModel

class StudentController:
    def __init__(self, view):
        self.model = StudentModel()
        self.view = view
        self.headers = ("id","last_name", "first_name", "major", "gpa")

    def add_student(self, last_name, first_name, major, gpa):
        self.model.insert(last_name, first_name, major, gpa)
        data = self.model.get_all()
        
        self.update_view(data)
    
    def delete_student(self, id):
        self.model.delete(id)


    def update_view(self, data_in_objs):
        headers = self.headers
        if data_in_objs:
            data_in_lists =  [[obj.id, obj.last_name, obj.first_name, obj.major, obj.gpa] for obj in data_in_objs]
            self.view.update_view(headers, data_in_lists)
        else:
            data = []
            self.view.update_view(headers, data)
