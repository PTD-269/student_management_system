from .controller import StudentController
from .model import StudentModel
from .view import StudentView



class WidgetStudent(StudentView):
    def __init__(self):
        super().__init__()
        
        model = StudentModel()
        controller = StudentController(model, self)
        self.set_controller(controller)
        self.controller.setup()
