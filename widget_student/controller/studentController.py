
class StudentController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
    

    def add_student(self, last_name, first_name, major, gpa):
        self.model.insert(last_name, first_name, major, gpa)
        data = self.model.get_all()
        self.view.update_view(data)

    def delete_student(self, id):
        self.model.delete(id)
        

    def setup(self):
        data = self.model.get_all()
        self.view.setupTableView(data)