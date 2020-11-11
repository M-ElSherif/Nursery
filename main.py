import sys

from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel, QSqlTableModel
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableView, QWidget
from PyQt5 import QtWidgets

from Student import Student
from StudentDAO import StudentDAO
from dbAccess import DBAccess
from gui.MainWindow import Ui_MainWindow
from gui.FormAddStudent import Ui_FormAddStudent

db = QSqlDatabase("QSQLITE")
db.setDatabaseName("Nursery.sqlite")
try:
    db.open()
except Exception as e:
    print(e)

''' 
ADD STUDENT FORM CLASS
'''


class AddStudentForm(QWidget, Ui_FormAddStudent):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

''' 
MAINWINDOW CLASS
'''


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.form_add_student = AddStudentForm()  # Initially set to None
        self.form_add_student.hide()
        self.student_dao = StudentDAO()

        # TODO: Should be refactored up maybe into another class
        # Setting the SqlQuery model for the tables
        self.model = QSqlQueryModel()
        self.tblStudents.setModel(self.model)

        self.assign_slots()
        self.display_table(self.model)

        # TODO: Currently disabled combobox
        # Setting the combobox for Students tab
        # self.cmbFieldFilter.addItems(studentDAO().getTableFields())

    def assign_slots(self):
        # Assign search filters on text change in search fields
        self.lineDisplayStudentName.textChanged.connect(self.apply_filters)
        self.lineDisplayStudentGrade.textChanged.connect(self.apply_filters)
        self.lineDisplayStudentAge.textChanged.connect(self.apply_filters)

        # Assign add student form button
        self.btnAddStudent.clicked.connect(self.show_form_addstudent)

        # Assign save student in add student form
        self.form_add_student.btnSaveStudent.clicked.connect(self.add_student)

    def add_student(self):
        student_name = self.form_add_student.lineAddStudentName.text()
        student_grade = int(self.form_add_student.lineAddStudentGrade.text())
        student_age = int(self.form_add_student.lineAddStudentAge.text())

        new_student = Student(student_name, student_age, student_grade)

        self.student_dao.create_student(new_student)
        self.apply_filters()

    def show_form_addstudent(self, checked):
        # if self.form_add_student is None:
        #     self.form_add_student = AddStudentForm()
        self.form_add_student.show()

        # else:
        #     self.form_add_student.close()
        #     self.form_add_student = None

    def display_table(self, model, s=None):
        self.query = QSqlQuery(db=db)
        self.query.prepare(
            "SELECT name,age,grade FROM students "
            "WHERE name LIKE '%' || :student_name || '%' AND "
            "age LIKE '%' || :student_age || '%' AND "
            "grade LIKE '%' || :student_grade || '%'"
        )

        self.apply_filters()

    def apply_filters(self, s=None):
        # Get the text values from the search entries
        student_name = self.lineDisplayStudentName.text()
        student_grade = self.lineDisplayStudentGrade.text()
        student_age = self.lineDisplayStudentAge.text()

        self.query.bindValue(":student_name", student_name)
        self.query.bindValue(":student_grade", student_grade)
        self.query.bindValue(":student_age", student_age)

        self.query.exec_()
        self.model.setQuery(self.query)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
