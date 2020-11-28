import sys

from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel
from PyQt5 import QtWidgets, QtCore

from gui.Ui_MainWindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Setting the SqlQuery model for the tables
        self.sql_query_model: QSqlQueryModel = QSqlQueryModel()
        self.tblStudents.setModel(self.sql_query_model)


        # self.set_student_table()
        # self.student_add_controller: StudentAddController = StudentAddController(self)
        # self.student_edit_controller: StudentEditController = StudentEditController(self)
        # self.student_add_controller.show()
        # self.student_add_controller.hide()
        # self.student_edit_controller.show()
        # self.student_edit_controller.hide()

        # self.assign_slots()
        # self.student_edit_controller.set_student_editor()

        # QModelIndex QItemSelectionModel::currentIndex() const
        # self.selection_model = self.tbl_students.selectionModel()

    '''[1] MainWindow method'''

    # def assign_slots(self):
    #     # Assign search filters on text change in search fields
    #     self.lineDisplayStudentName.textChanged.connect(self.set_student_table)
    #     self.lineDisplayStudentGrade.textChanged.connect(self.set_student_table)
    #     self.lineDisplayStudentAge.textChanged.connect(self.set_student_table)
    #
    #     # Assign search filters clear button
    #     self.btnClearFilters.clicked.connect(self.clear_filters)
    #
    #     # Assign add student form button
    #     self.btnAddStudent.clicked.connect(self.student_add_controller.show)
    #
    #     # Assign edit student form button
    #     self.btnEditStudent.clicked.connect(self.student_edit_controller.show)

    '''[2] MainWindow method'''

    # def refresh_table(self):
    #     self.set_student_table()
    #
    # '''[4] MainWindow method'''
    #
    # def show_form_addstudent(self, checked):
    #     self.student_add_controller.show()
    #
    # '''[5] MainWindow method'''
    #
    # def show_form_editstudent(self, checked):
    #     self.student_edit_controller.show()

    '''[6] MainWindow method'''

    # def set_student_table(self, s=None):
    #     self.query = QSqlQuery(db=db)
    #     self.query.prepare(
    #         "SELECT studentID,name,age,grade FROM students "
    #         "WHERE name LIKE '%' || :student_name || '%' AND "
    #         "age LIKE '%' || :student_age || '%' AND "
    #         "grade LIKE '%' || :student_grade || '%'"
    #     )
    #
    #     student_name, student_grade, student_age = self.get_filters()
    #     self.query.bindValue(":student_name", student_name)
    #     self.query.bindValue(":student_grade", student_grade)
    #     self.query.bindValue(":student_age", student_age)
    #
    #     self.query.exec_()
    #     self.sql_query_model.setQuery(self.query)

    '''[7] MainWindow method'''

    # def get_filters(self, s=None):
    #     # Get the text values from the search entries
    #     student_name = self.lineDisplayStudentName.text()
    #     student_grade = self.lineDisplayStudentGrade.text()
    #     student_age = self.lineDisplayStudentAge.text()
    #
    #     return student_name, student_grade, student_age
    #
    # '''[8] MainWindow method'''
    #
    # def clear_filters(self, s=None):
    #     self.lineDisplayStudentName.clear()
    #     self.lineDisplayStudentAge.clear()
    #     self.lineDisplayStudentGrade.clear()
