from PyQt5.QtSql import QSqlQuery, QSqlDatabase

from Controller.StudentAddController import StudentAddController
from Controller.StudentEditController import StudentEditController
from Views.MainWindow import MainWindow

db = QSqlDatabase("QSQLITE")
db.setDatabaseName("./Database/Nursery.sqlite")
try:
    db.open()
except Exception as e:
    print(e)


class MainController:

    def __init__(self):
        self.view: MainWindow = MainWindow()
        self.student_add_controller: StudentAddController = StudentAddController(self.view)
        self.student_edit_controller: StudentEditController = StudentEditController(self.view)
        self.student_add_controller.show()
        self.student_add_controller.hide()
        self.student_edit_controller.show()
        self.student_edit_controller.hide()
        self.query = QSqlQuery(db=db)
        self.assign_slots()
        self.set_student_table()
        self.student_edit_controller.set_student_editor()
        self.selection_model = self.view.tblStudents.selectionModel()

    def show(self):
        self.view.show()

    def assign_slots(self):
        # Assign search filters on text change in search fields
        self.view.lineDisplayStudentName.textChanged.connect(self.set_student_table)
        self.view.lineDisplayStudentGrade.textChanged.connect(self.set_student_table)
        self.view.lineDisplayStudentAge.textChanged.connect(self.set_student_table)

        # Assign search filters clear button
        self.view.btnClearFilters.clicked.connect(self.clear_filters)

        # Assign add student form button
        self.view.btnAddStudent.clicked.connect(self.student_add_controller.show)

        # Assign edit student form button
        self.view.btnEditStudent.clicked.connect(self.student_edit_controller.show)

        self.student_add_controller.signalPassDataToMainForm.connect(self.refresh_table)
        self.student_edit_controller.signalPassDataToMainForm.connect(self.refresh_table)

        # Assign refresh student table button
        self.view.btnRefresh.clicked.connect(self.refresh_table)

    def refresh_table(self, s):
        if s:
            self.set_student_table()

    '''[4] MainWindow method'''

    def show_form_addstudent(self, checked):
        self.student_add_controller.show()

    '''[5] MainWindow method'''

    def show_form_editstudent(self, checked):
        self.student_edit_controller.show()

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
        self.view.sql_query_model.setQuery(self.query)

    def get_filters(self, s=None):
        # Get the text values from the search entries
        student_name = self.view.lineDisplayStudentName.text()
        student_grade = self.view.lineDisplayStudentGrade.text()
        student_age = self.view.lineDisplayStudentAge.text()

        return student_name, student_grade, student_age

    '''[8] MainWindow method'''

    def clear_filters(self, s=None):
        self.view.lineDisplayStudentName.clear()
        self.view.lineDisplayStudentAge.clear()
        self.view.lineDisplayStudentGrade.clear()
