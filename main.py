import sys

from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel, QSqlTableModel
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableView, QWidget, QDataWidgetMapper
from PyQt5 import QtWidgets

from Student import Student
from StudentDAO import StudentDAO
from dbAccess import DBAccess
from gui.MainWindow import Ui_MainWindow
from gui.FormAddStudent import Ui_FormAddStudent
from gui.FormEditDeleteStudent import Ui_FormEditDeleteStudent

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
EDIT / DELETE STUDENT FORM CLASS
'''


class EditDeleteStudentForm(QWidget, Ui_FormEditDeleteStudent):
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
        self.form_add_student = AddStudentForm()
        self.form_add_student.hide()
        self.form_edit_student = EditDeleteStudentForm()
        self.form_edit_student.hide()
        self.student_dao = StudentDAO()
        self.mapper = QDataWidgetMapper()

        # TODO: Should be refactored up maybe into another class
        # Setting the SqlQuery model for the tables
        self.model = QSqlQueryModel()
        self.tblStudents.setModel(self.model)

        self.display_student_table()
        self.display_student_editor()
        self.assign_slots()

        # TODO: Currently disabled combobox
        # Setting the combobox for Students tab
        # self.cmbFieldFilter.addItems(studentDAO().getTableFields())

    def assign_slots(self):
        # Assign search filters on text change in search fields
        self.lineDisplayStudentName.textChanged.connect(self.display_student_table)
        self.lineDisplayStudentGrade.textChanged.connect(self.display_student_table)
        self.lineDisplayStudentAge.textChanged.connect(self.display_student_table)

        # Assign search filters clear button
        self.btnClearFilters.clicked.connect(self.clear_filters)

        # Assign add student form button
        self.btnAddStudent.clicked.connect(self.show_form_addstudent)

        # Add Student Form
        # Assign save student in add student form
        self.form_add_student.btnSaveStudent.clicked.connect(self.add_student)

        # Assign edit student form button
        self.btnEditStudent.clicked.connect(self.show_form_editstudent)

        # Edit Student Form
        self.form_edit_student.btnEditStudentPrevious.clicked.connect(self.mapper.toPrevious)
        self.form_edit_student.btnEditStudentNext.clicked.connect(self.mapper.toNext)
        self.form_edit_student.btnEditStudentSave.clicked.connect(self.mapper.submit)   # TODO: need to fix this use a separate QSqlTableModel instead to allow submit to work
        self.form_edit_student.btnEditStudentDelete.clicked.connect(self.delete_student)

    def add_student(self):
        student_name = self.form_add_student.lineAddStudentName.text()
        student_grade = int(self.form_add_student.lineAddStudentGrade.text())
        student_age = int(self.form_add_student.lineAddStudentAge.text())

        new_student = Student(student_name, student_age, student_grade)

        self.student_dao.create_student(new_student)
        self.display_student_table()

    def delete_student(self):
        student_id = int(self.form_edit_student.lineEditStudentID.text())

        self.student_dao.delete_student(student_id)
        self.display_student_editor()
        self.display_student_table()

    def show_form_addstudent(self, checked):
        self.form_add_student.show()

    def show_form_editstudent(self, checked):
        self.form_edit_student.show()

    def display_student_table(self, s=None):
        self.query = QSqlQuery(db=db)
        self.query.prepare(
            "SELECT studentID,name,age,grade FROM students "
            "WHERE name LIKE '%' || :student_name || '%' AND "
            "age LIKE '%' || :student_age || '%' AND "
            "grade LIKE '%' || :student_grade || '%'"
        )

        student_name, student_grade, student_age = self.get_filters()
        self.query.bindValue(":student_name", student_name)
        self.query.bindValue(":student_grade", student_grade)
        self.query.bindValue(":student_age", student_age)

        self.query.exec_()
        self.model.setQuery(self.query)


    def get_filters(self, s=None):
        # Get the text values from the search entries
        student_name = self.lineDisplayStudentName.text()
        student_grade = self.lineDisplayStudentGrade.text()
        student_age = self.lineDisplayStudentAge.text()

        return (student_name, student_grade, student_age)

    def clear_filters(self, s=None):
        self.lineDisplayStudentName.clear()
        self.lineDisplayStudentAge.clear()
        self.lineDisplayStudentGrade.clear()

    def display_student_editor(self):
        self.mapper = QDataWidgetMapper()
        self.mapper.setModel(self.model)
        self.mapper.addMapping(self.form_edit_student.lineEditStudentID, 0)
        self.mapper.addMapping(self.form_edit_student.lineEditStudentName, 1)
        self.mapper.addMapping(self.form_edit_student.lineEditStudentGrade, 2)
        self.mapper.addMapping(self.form_edit_student.lineEditStudentAge, 3)

        self.display_student_table(self.model)
        self.mapper.toFirst()



app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
