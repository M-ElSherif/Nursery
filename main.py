import sys

from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel, QSqlTableModel
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableView
from PyQt5 import QtWidgets

from dbAccess import DBAccess
from gui.nurseryUI import Ui_MainWindow

db = QSqlDatabase("QSQLITE")
db.setDatabaseName("Nursery.sqlite")
try:
    db.open()
except Exception as e:
    print(e)


class DAL:
    def __init__(self):
        self.sql_connection = DBAccess.createConnection()

    def getTableFields(self):
        # TODO: make a case statement which has a query for each table in the database
        try:
            cur = self.sql_connection.cursor()
            cur = self.sql_connection.execute('SELECT name,age,grade FROM students')
            fields = [description[0] for description in cur.description]
            return fields
        except Exception as e:
            print(e)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Data Access Layer class object
        dal = DAL()

        # TODO: Should be refactored up maybe into another class
        # Setting the SqlQuery model for the tables
        self.model = QSqlQueryModel()
        self.tblStudents.setModel(self.model)

        self.assignSlots()
        self.displayTable(self.model)

        # TODO: Currently disabled combobox
        # Setting the combobox for Students tab
        # self.cmbFieldFilter.addItems(dal.getTableFields())

    def assignSlots(self):
        # Assign search filters on text change in search fields
        self.lineStudentName.textChanged.connect(self.applyFilters)
        self.lineStudentGrade.textChanged.connect(self.applyFilters)
        self.lineStudentAge.textChanged.connect(self.applyFilters)

    def displayTable(self, model, s=None):
        self.query = QSqlQuery(db=db)
        self.query.prepare(
            "SELECT name,age,grade FROM students "
            "WHERE name LIKE '%' || :student_name || '%' AND "
            "age LIKE '%' || :student_age || '%' AND "
            "grade LIKE '%' || :student_grade || '%'"
        )

        self.applyFilters()

    def applyFilters(self, s=None):
        # Get the text values from the search entries
        student_name = self.lineStudentName.text()
        student_grade = self.lineStudentGrade.text()
        student_age = self.lineStudentAge.text()

        self.query.bindValue(":student_name", student_name)
        self.query.bindValue(":student_grade", student_grade)
        self.query.bindValue(":student_age", student_age)

        self.query.exec_()
        self.model.setQuery(self.query)

    def tempMethod(self):
        pass

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
