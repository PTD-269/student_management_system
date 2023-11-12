import sys
from .MainWindow import Ui_MainWindow
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt


class DictionaryTableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(DictionaryTableModel, self).__init__()
        self._data = data
        self._headers = list(self._data.keys())

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # Look up the key by header index.
            column = index.column()
            column_key = self._headers[column]
            return str(self._data[column_key][index.row()])

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data[self._headers[0]])

    def columnCount(self, index):
        # The length of our headers.
        return len(self._headers)

    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._headers[section])

            if orientation == Qt.Vertical:
                return str(section)
    

class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self, data):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.controller = None

        # Button custom
        self.findButton.clicked.connect(self.find)
        self.addButton.clicked.connect(self.add)
        self.updateButton.clicked.connect(self.update)
        self.deleteButton.clicked.connect(self.delete)

        # ComboBox custom
        self.comboBox.addItem("gpa")
        self.comboBox.addItem("LName")
        self.comboBox.setCurrentIndex(-1)
        self.comboBox.currentTextChanged.connect(self.text_changed)

        # TableView custom
        self.tableModel = DictionaryTableModel(data)
        self.tableView.setModel(self.tableModel)
        # For resize automaticly depends on data shape
        self.tableView.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableView.clicked.connect(self.table_clicked)

    def set_controller(self, controller):
        """Set controller to communicate for getting specific data"""
        self.controller = controller
    
    def load(self, data):
        """Load new data for TableModel """
        self.tableModel._data = data

    def add(self):
        """Add object to database"""
        last_name = self.lineEditLastName.text()
        first_name = self.lineEditFirstName.text()
        major = self.lineEditMajor.text()
        gpa = float(self.lineEditGPA.text())
        
        if last_name and first_name and major and gpa:
            self.controller.add_student(last_name, first_name, major, gpa)
            data = self.controller.get_all_students()
            self.load(data)
            self.tableModel.layoutChanged.emit()

            self.lineEditLastName.setText("")
            self.lineEditFirstName.setText("")
            self.lineEditMajor.setText("")
            self.lineEditGPA.setText("")

    def text_changed(self, text):  # text is a str
        print(text)

    def find(self):
        print("found")

    def update(self):
        print("updated")

    def delete(self):
        # indexes = self.tableView.selectedIndexes()
        pass
        # row = indexes[0].row()

    def sort_gpa(self):
        print("sorted gpa")

    def table_clicked(self):
        indexes = self.tableView.selectedIndexes()
        row = indexes[0].row()
        
        print("row", row)


class StudentView:
    def __init__(self):
        self.controller = None

    def set_controller(self, controller):
        self.controller = controller

    def show(self):
        app=QtWidgets.QApplication(sys.argv)
        data = self.controller.get_all_students()
        self.window=MainWindow(data)
        self.window.set_controller(self.controller)
        self.window.show()
        app.exec_()

