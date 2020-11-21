import sys

from PyQt5.QtCore import QModelIndex
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel
from PyQt5.QtWidgets import QDataWidgetMapper
from PyQt5 import QtWidgets

from Forms.AddStudentForm import AddStudentForm
from Forms.EditStudentForm import EditDeleteStudentForm
from Models.Student import Student
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

        self.set_student_table()
        self.set_student_editor()
        self.assign_slots()

        # TODO: Figure out how to get id of selected row. Below method might help
        # QModelIndex QItemSelectionModel::currentIndex() const
        self.selection_model = self.tblStudents.selectionModel()
        self.isselected.clicked.connect(self.is_selected)

    def is_selected(self, s= None):
        print(self.selection_model.hasSelection())
        print(self.selection_model.isRowSelected(0))
        index = self.selection_model.currentIndex().row()
        # i = index.sibling(index.row(), 0).data()

        return index

    '''[1] MainWindow method'''

    def assign_slots(self):
        # Assign search filters on text change in search fields
        self.lineDisplayStudentName.textChanged.connect(self.set_student_table)
        self.lineDisplayStudentGrade.textChanged.connect(self.set_student_table)
        self.lineDisplayStudentAge.textChanged.connect(self.set_student_table)

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
        self.form_edit_student.btnEditStudentSave.clicked.connect(self.update_student)
        self.form_edit_student.btnEditStudentDelete.clicked.connect(self.delete_student)

    '''[2] MainWindow method'''

    def add_student(self):
        student_name = self.form_add_student.lineAddStudentName.text()
        student_grade = int(self.form_add_student.lineAddStudentGrade.text())
        student_age = int(self.form_add_student.lineAddStudentAge.text())

        student = Student(student_name, student_age, student_grade)

        self.student_dao.create_student(student)
        self.set_student_table()

    '''[3] MainWindow method'''

    def update_student(self):
        student_id = int(self.form_edit_student.lineEditStudentID.text())
        student_name = self.form_edit_student.lineEditStudentName.text()
        student_grade = self.form_edit_student.lineEditStudentGrade.text()
        student_age = self.form_edit_student.lineEditStudentAge.text()

        student = Student(student_name, student_age, student_grade)

        self.student_dao.update_student(student, student_id)
        self.set_student_table()

    '''[3] MainWindow method'''

    def delete_student(self):
        student_id = int(self.form_edit_student.lineEditStudentID.text())

        self.student_dao.delete_student(student_id)
        self.set_student_editor()
        self.set_student_table()

    '''[4] MainWindow method'''

    def show_form_addstudent(self, checked):
        self.form_add_student.show()

    '''[5] MainWindow method'''

    def show_form_editstudent(self, checked):
        i = self.is_selected()
        if i & i >= 0:
            self.mapper.setCurrentIndex(i)
        self.form_edit_student.show()

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

    '''[9] MainWindow method'''

    def set_student_editor(self, index=0):
        self.mapper = QDataWidgetMapper()
        self.mapper.setModel(self.model)
        self.mapper.addMapping(self.form_edit_student.lineEditStudentID, 0)
        self.mapper.addMapping(self.form_edit_student.lineEditStudentName, 1)
        self.mapper.addMapping(self.form_edit_student.lineEditStudentGrade, 2)
        self.mapper.addMapping(self.form_edit_student.lineEditStudentAge, 3)

        # self.set_student_table(self.model)
        # if index > 0:
        #     self.mapper.setCurrentIndex(index)
        self.mapper.toFirst()


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
