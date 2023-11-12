from widget_student.model import StudentModel
from widget_student.view import StudentView
from widget_student.controller import StudentController

def main():
    model = StudentModel()
    view = StudentView()
    controller = StudentController(model, view)
    view.set_controller(controller)
    controller.main()

# if __name__ == "__main__":
main()

