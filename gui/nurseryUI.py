# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nurseryUI_2.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

#Current UI
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(935, 752)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.pgeStudents = QtWidgets.QWidget()
        self.pgeStudents.setObjectName("pgeStudents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.pgeStudents)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabsStudents = QtWidgets.QTabWidget(self.pgeStudents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabsStudents.sizePolicy().hasHeightForWidth())
        self.tabsStudents.setSizePolicy(sizePolicy)
        self.tabsStudents.setObjectName("tabsStudents")
        self.tabDisplayStudents = QtWidgets.QWidget()
        self.tabDisplayStudents.setObjectName("tabDisplayStudents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tabDisplayStudents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.lblStudentName = QtWidgets.QLabel(self.tabDisplayStudents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblStudentName.sizePolicy().hasHeightForWidth())
        self.lblStudentName.setSizePolicy(sizePolicy)
        self.lblStudentName.setMinimumSize(QtCore.QSize(0, 0))
        self.lblStudentName.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lblStudentName.setObjectName("lblStudentName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblStudentName)
        self.lineStudentName = QtWidgets.QLineEdit(self.tabDisplayStudents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineStudentName.sizePolicy().hasHeightForWidth())
        self.lineStudentName.setSizePolicy(sizePolicy)
        self.lineStudentName.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineStudentName.setFrame(True)
        self.lineStudentName.setObjectName("lineStudentName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineStudentName)
        self.label_2 = QtWidgets.QLabel(self.tabDisplayStudents)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineStudentGrade = QtWidgets.QLineEdit(self.tabDisplayStudents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineStudentGrade.sizePolicy().hasHeightForWidth())
        self.lineStudentGrade.setSizePolicy(sizePolicy)
        self.lineStudentGrade.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineStudentGrade.setObjectName("lineStudentGrade")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineStudentGrade)
        self.label_3 = QtWidgets.QLabel(self.tabDisplayStudents)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineStudentAge = QtWidgets.QLineEdit(self.tabDisplayStudents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineStudentAge.sizePolicy().hasHeightForWidth())
        self.lineStudentAge.setSizePolicy(sizePolicy)
        self.lineStudentAge.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineStudentAge.setObjectName("lineStudentAge")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineStudentAge)
        self.verticalLayout.addLayout(self.formLayout)
        self.tblStudents = QtWidgets.QTableView(self.tabDisplayStudents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tblStudents.sizePolicy().hasHeightForWidth())
        self.tblStudents.setSizePolicy(sizePolicy)
        self.tblStudents.setObjectName("tblStudents")
        self.verticalLayout.addWidget(self.tblStudents)
        self.tabsStudents.addTab(self.tabDisplayStudents, "")
        self.gridLayout_3.addWidget(self.tabsStudents, 0, 0, 1, 1)
        self.tabWidget.addTab(self.pgeStudents, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabsStudents.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblStudentName.setText(_translate("MainWindow", "Name:"))
        self.lineStudentName.setPlaceholderText(_translate("MainWindow", "Input search text..."))
        self.label_2.setText(_translate("MainWindow", "Grade:"))
        self.lineStudentGrade.setPlaceholderText(_translate("MainWindow", "Input search text..."))
        self.label_3.setText(_translate("MainWindow", "Age:"))
        self.lineStudentAge.setPlaceholderText(_translate("MainWindow", "Input search text..."))
        self.tabsStudents.setTabText(self.tabsStudents.indexOf(self.tabDisplayStudents), _translate("MainWindow", "Display"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pgeStudents), _translate("MainWindow", "Students"))