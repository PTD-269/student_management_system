# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTableView, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(640, 480)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_1 = QWidget(Form)
        self.widget_1.setObjectName(u"widget_1")
        self.horizontalLayout = QHBoxLayout(self.widget_1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.widget_1)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(67, 25))

        self.horizontalLayout.addWidget(self.label, 0, Qt.AlignLeft)

        self.lineEditID = QLineEdit(self.widget_1)
        self.lineEditID.setObjectName(u"lineEditID")

        self.horizontalLayout.addWidget(self.lineEditID)

        self.findButton = QPushButton(self.widget_1)
        self.findButton.setObjectName(u"findButton")

        self.horizontalLayout.addWidget(self.findButton, 0, Qt.AlignRight)

        self.label_2 = QLabel(self.widget_1)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.comboBox = QComboBox(self.widget_1)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout.addWidget(self.comboBox)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_7)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_11)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_9)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_8)


        self.verticalLayout.addWidget(self.widget_1)

        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_6 = QLabel(self.widget_2)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_2.addWidget(self.label_6)

        self.lineEditLastName = QLineEdit(self.widget_2)
        self.lineEditLastName.setObjectName(u"lineEditLastName")

        self.horizontalLayout_2.addWidget(self.lineEditLastName)

        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.lineEditFirstName = QLineEdit(self.widget_2)
        self.lineEditFirstName.setObjectName(u"lineEditFirstName")

        self.horizontalLayout_2.addWidget(self.lineEditFirstName)

        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.lineEditMajor = QLineEdit(self.widget_2)
        self.lineEditMajor.setObjectName(u"lineEditMajor")

        self.horizontalLayout_2.addWidget(self.lineEditMajor)

        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.lineEditGPA = QLineEdit(self.widget_2)
        self.lineEditGPA.setObjectName(u"lineEditGPA")

        self.horizontalLayout_2.addWidget(self.lineEditGPA)


        self.verticalLayout.addWidget(self.widget_2)

        self.widget_3 = QWidget(Form)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_10)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.addButton = QPushButton(self.widget_3)
        self.addButton.setObjectName(u"addButton")

        self.horizontalLayout_3.addWidget(self.addButton)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.updateButton = QPushButton(self.widget_3)
        self.updateButton.setObjectName(u"updateButton")

        self.horizontalLayout_3.addWidget(self.updateButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.deleteButton = QPushButton(self.widget_3)
        self.deleteButton.setObjectName(u"deleteButton")

        self.horizontalLayout_3.addWidget(self.deleteButton)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_14)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_13)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_12)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addWidget(self.widget_3)

        self.tableView = QTableView(Form)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout.addWidget(self.tableView)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Student ID:", None))
        self.findButton.setText(QCoreApplication.translate("Form", u"Find", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Sort By:", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Last Name:", None))
        self.lineEditLastName.setText("")
        self.label_5.setText(QCoreApplication.translate("Form", u"First Name:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Major:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"GPA:", None))
        self.addButton.setText(QCoreApplication.translate("Form", u"Add", None))
        self.updateButton.setText(QCoreApplication.translate("Form", u"Update", None))
        self.deleteButton.setText(QCoreApplication.translate("Form", u"Delete", None))
    # retranslateUi

