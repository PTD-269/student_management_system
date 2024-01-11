from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Qt

from view.widget import Ui_Form

from controller.studentController import StudentController


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self):
        super(TableModel, self).__init__()
        self._headers = []
        self._data = []

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._headers)
    
    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal and section < len(self._headers):
                return str(self._headers[section])

            if orientation == Qt.Vertical:
                return str(section + 1)  # Default row numbers if no vertical headers

class StudentView(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(StudentView, self).__init__()
        self.setupUi(self)
        self.feature_sorted = "id"
        self.controller = StudentController(self)
        self.init_ui()
        # Button custom
        self.addButton.clicked.connect(self.add)
        self.deleteButton.clicked.connect(self.delete)
        self.findButton.clicked.connect(self.find)
        self.updateButton.clicked.connect(self.update)
        self.comboBox.currentTextChanged.connect(self.sort_by_feature)
        
    def init_ui(self):
        self.tableModel = TableModel()
        self.tableView.setModel(self.tableModel)
        # For resize automaticly depends on data shape
        self.tableView.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.update_view()

        self.comboBox.addItems(["id", "last_name", "first_name", "major", "gpa"])
    def add(self):
        """Add object to database"""
        last_name = self.lineEditLastName.text()
        first_name = self.lineEditFirstName.text()
        major = self.lineEditMajor.text()
        gpa = self.lineEditGPA.text()
        
        if last_name and first_name and major and gpa :

            self.controller.add_student(last_name, first_name, major, gpa)
            self.update_view()

            self.clear()

    def delete(self):
        id_deleted = self.lineEditID.text()
        if id_deleted:
            self.controller.delete_student(id_deleted)
            self.update_view()

            self.clear()

    def update(self):
        id = self.lineEditID.text()
        last_name = self.lineEditLastName.text()
        first_name = self.lineEditFirstName.text()
        major = self.lineEditMajor.text()
        gpa = self.lineEditGPA.text()
        
        if id and last_name and first_name and major and gpa:

            self.controller.update_student_info(id, last_name, first_name, major, gpa)
            self.update_view()
            
            self.clear()

    def find(self):
        id = self.lineEditID.text()
        if id:
            student = self.controller.get_student(id)
            last_name, first_name, major, gpa = student.last_name, student.first_name, student.major, str(student.gpa)

            self.lineEditLastName.setText(last_name)
            self.lineEditFirstName.setText(first_name)
            self.lineEditMajor.setText(major)
            self.lineEditGPA.setText(gpa)
    
    def sort_by_feature(self, feature_sorted):
        self.feature_sorted = feature_sorted
        self.update_view()

        self.clear()
    def update_view(self):
        """Load new data for TableModel """
        sort_needed = self.feature_sorted
        data_in_objs = self.controller.get_all_student(sort_needed)

        headers = ("id","last_name", "first_name", "major", "gpa")
        data_in_lists = [[obj.id, obj.last_name, obj.first_name, obj.major, obj.gpa] for obj in data_in_objs]
    
        self.tableModel._headers = headers 
        self.tableModel._data = data_in_lists

        self.tableModel.layoutChanged.emit()

    def clear(self):
        """clear all input when user clicked"""
        self.lineEditID.setText("")
        self.lineEditLastName.setText("")
        self.lineEditFirstName.setText("")
        self.lineEditMajor.setText("")
        self.lineEditGPA.setText("")