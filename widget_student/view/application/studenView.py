from widget_student.view.application.widget import Ui_Form
from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Qt
from widget_student.controller import StudentController

class TableModel(QtCore.QAbstractTableModel):

    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]
            return str(value)

    def rowCount(self, index):
        return self._data.shape[0]

    def columnCount(self, index):
        return self._data.shape[1]

    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return str(self._data.columns[section])

            if orientation == Qt.Orientation.Vertical:
                return str(self._data.index[section])
    

class StudentView(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(StudentView, self).__init__()
        self.setupUi(self)

        self.controller = StudentController(self)

        self.tableModel = TableModel()
        self.tableView.setModel(self.tableModel)
        # For resize automaticly depends on data shape
        self.tableView.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        # Button custom
        self.addButton.clicked.connect(self.add)

    def update_view(self, data):
        """Load new data for TableModel """
        self.tableModel._data = data
        self.tableModel.layoutChanged.emit()

    def add(self):
        """Add object to database"""
        last_name = self.lineEditLastName.text()
        first_name = self.lineEditFirstName.text()
        major = self.lineEditMajor.text()
        gpa = float(self.lineEditGPA.text())
        
        if last_name and first_name and major and gpa:
            self.controller.add_student(last_name, first_name, major, gpa)

            self.lineEditLastName.setText("")
            self.lineEditFirstName.setText("")
            self.lineEditMajor.setText("")
            self.lineEditGPA.setText("")



