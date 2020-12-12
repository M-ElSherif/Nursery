import sys

from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel
from PyQt5 import QtWidgets, QtCore

from gui.Ui_MainWindow import Ui_MainWindow


class MainWindowView(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Setting the SqlQuery model for the tables
        self.student_sql_query_model: QSqlQueryModel = QSqlQueryModel()
        self.employee_sql_query_model: QSqlQueryModel = QSqlQueryModel()
        self.tblStudents.setModel(self.student_sql_query_model)
        self.tblEmployees.setModel(self.employee_sql_query_model)


