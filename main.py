
from view.studenView import StudentView
from PySide6.QtWidgets import QApplication, QMainWindow
import sys 

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        widget1 = StudentView()

        self.setCentralWidget(widget1)



app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
