
class StudentController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
    
    def get_all_students(self):
        data = self.model.get_all()
        return data
    def add_student(self, last_name, first_name, major, gpa):
        self.model.insert(last_name, first_name, major, gpa)
        data = self.controller.get_all_students()
        self.view.update_view(data)

    def delete_student(self, id):
        self.model.delete(id)
        
    def main(self):
        self.view.show()