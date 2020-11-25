import sys

from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel
from PyQt5.QtWidgets import QDataWidgetMapper
from PyQt5 import QtWidgets

from Controller.StudentAddController import StudentAddController
from Controller.StudentEditController import StudentEditController
from Views.StudentAddView import StudentAddView
from Views.StudentEditView import StudentEditView
from DAO.StudentDAO import StudentDAO
from gui.MainWindow import Ui_MainWindow

db = QSqlDatabase("QSQLITE")
db.setDatabaseName("./Database/Nursery.sqlite")
try:
    db.open()
except Exception as e:
    print(e)

''' 
MAINWINDOW CLASS
'''


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # TODO: Should be refactored up maybe into another class
        # Setting the SqlQuery model for the tables
        self.model = QSqlQueryModel()
        self.tblStudents.setModel(self.model)

        self.set_student_table()
        self.set_student_editor()
        self.assign_slots()

        # QModelIndex QItemSelectionModel::currentIndex() const
        self.selection_model = self.tbl_students.selectionModel()

    '''[1] MainWindow method'''

    def assign_slots(self):
        # Assign search filters on text change in search fields
        self.lineDisplayStudentName.textChanged.connect(self.set_student_table)
        self.lineDisplayStudentGrade.textChanged.connect(self.set_student_table)
        self.lineDisplayStudentAge.textChanged.connect(self.set_student_table)

        # Assign search filters clear button
        self.btnClearFilters.clicked.connect(self.clear_filters)

        # Assign add student form button
        self.btnAddStudent.clicked.connect(self.student_add_controller.show)

        # Assign edit student form button
        self.btnEditStudent.clicked.connect(self.show_form_editstudent)

        # Edit Student Form
        self.form_edit_student.btnEditStudentPrevious.clicked.connect(self.mapper.toPrevious)
        self.form_edit_student.btnEditStudentNext.clicked.connect(self.mapper.toNext)
        self.form_edit_student.btnEditStudentSave.clicked.connect(self.update_student)
        self.form_edit_student.btnEditStudentDelete.clicked.connect(self.delete_student)

    '''[2] MainWindow method'''

    def refresh_table(self):
        self.set_student_table()

    '''[4] MainWindow method'''

    def show_form_addstudent(self, checked):
        self.student_add_controller.show()

    '''[5] MainWindow method'''

    def show_form_editstudent(self, checked):
        self.student_edit_controller.show()

    '''[6] MainWindow method'''

    def set_student_table(self, s=None):
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

    '''[7] MainWindow method'''

    def get_filters(self, s=None):
        # Get the text values from the search entries
        student_name = self.lineDisplayStudentName.text()
        student_grade = self.lineDisplayStudentGrade.text()
        student_age = self.lineDisplayStudentAge.text()

        return student_name, student_grade, student_age

    '''[8] MainWindow method'''

    def clear_filters(self, s=None):
        self.lineDisplayStudentName.clear()
        self.lineDisplayStudentAge.clear()
        self.lineDisplayStudentGrade.clear()


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
