from PySide6 import QtWidgets
from widget_student.view import MainWindow
import sys
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
        
    def main(self):
        app=QtWidgets.QApplication(sys.argv)
        data = self.model.get_all()
        window= MainWindow(data)
        window.set_controller(self)
        window.show()
        app.exec_()