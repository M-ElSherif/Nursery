from PyQt5.QtSql import QSqlQuery, QSqlDatabase

from Controller.EmployeeController import EmployeeController
from Controller.StudentController import StudentController
from Models.EmployeeModel import EmployeeModel
from Models.StudentModel import StudentModel
from Views.DialogConfirmationView import DialogConfirmationView
from Views.EmployeeAddView import EmployeeAddView
from Views.MainWindowView import MainWindowView
from Views.StudentAddView import StudentAddView
from Views.StudentEditView import StudentEditView

db = QSqlDatabase("QSQLITE")
db.setDatabaseName("./Database/Nursery.sqlite")
try:
    db.open()
except Exception as e:
    print(e)


class MainController:

    def __init__(self):
        # Instantiate the models to be used for the data
        self.student_model: StudentModel = StudentModel()
        self.employee_model: EmployeeModel = EmployeeModel()

        # Instantiate the controllers
        self.student_controller: StudentController = StudentController(self.student_model)
        self.employee_controller: EmployeeController = EmployeeController(self.employee_model)

        # Instantiate the views to be utilized throughout the application
        self.mainwindow_view: MainWindowView = MainWindowView()
        self.student_add_view: StudentAddView = StudentAddView(self.student_model, self.student_controller)
        self.student_edit_view: StudentEditView = StudentEditView(self.student_model, self.student_controller,
                                                                  self.mainwindow_view)
        self.employee_add_view: EmployeeAddView = EmployeeAddView(self.employee_model, self.employee_controller)
        self.dialog_popup_view: DialogConfirmationView = DialogConfirmationView()
        self.student_add_view.show()
        self.student_add_view.hide()
        self.student_edit_view.show_editor()
        self.student_edit_view.hide()
        self.employee_add_view.show()
        self.employee_add_view.hide()

        # Instantiate the QSqlQuery objects to be used by the tables
        self.student_query = QSqlQuery(db=db)
        self.employee_query = QSqlQuery(db=db)

        # Prepare the students table, load the data and assign slots to the signals
        self.set_student_table()
        self.student_selection_model = self.mainwindow_view.tblStudents.selectionModel()
        self.assign_student_slots()

        # Set the employees table, load the data and assign slots to the signals
        self.set_employee_table()
        self.employee_selection_model = self.mainwindow_view.tblEmployees.selectionModel()
        self.assign_employee_slots()

    def show(self):
        self.mainwindow_view.show()

    def assign_student_slots(self):
        # Assign search filters on text change in search fields
        self.mainwindow_view.lineDisplayStudentName.textChanged.connect(self.set_student_table)
        self.mainwindow_view.lineDisplayStudentGrade.textChanged.connect(self.set_student_table)
        self.mainwindow_view.lineDisplayStudentAge.textChanged.connect(self.set_student_table)

        # Assign search filters clear button
        self.mainwindow_view.btnClearFilters.clicked.connect(self.clear_student_filters)

        # Assign add student form button
        self.mainwindow_view.btnAddStudent.clicked.connect(self.student_add_view.show)

        # Assign edit student form button
        self.mainwindow_view.btnEditStudent.clicked.connect(self.student_edit_view.show_editor)

        # When a student is saved, deleted or updated successfully, refresh the student table
        #TODO: missing update signal
        self.student_model.signal_student_saved.connect(self.refresh_table)
        self.student_model.signal_student_saved.connect(self.dialog_popup_view.show_dialog)
        self.student_model.signal_student_deleted.connect(self.refresh_table)
        self.student_model.signal_student_deleted.connect(self.dialog_popup_view.show_dialog)

        # Assign refresh student table button
        self.mainwindow_view.btnRefresh.clicked.connect(self.refresh_table)

        # Assign add employee form button
        self.mainwindow_view.btnAddEmployee.clicked.connect(self.employee_add_view.show)

    def assign_employee_slots(self):
        # Populate the employee positions combobox
        self.load_employee_positions_combobox()

        # Assign search filters on text change in search fields
        self.mainwindow_view.lineEmployeeName.textChanged.connect(self.set_employee_table)
        self.mainwindow_view.cmbEmployeePosition.currentTextChanged.connect(self.set_employee_table)

        # # Assign search filters clear button
        self.mainwindow_view.btnClearFiltersEmployee.clicked.connect(self.clear_employee_filters)

        # # Assign add student form button
        # self.mainwindow_view.btnAddStudent.clicked.connect(self.student_add_view.show)
        #
        # # Assign edit student form button
        # self.mainwindow_view.btnEditStudent.clicked.connect(self.student_edit_view.show_editor)
        #
        # self.student_model.signal_student_saved.connect(self.refresh_table)
        # self.student_model.signal_student_saved.connect(self.dialog_popup_view.show_dialog)
        # self.student_model.signal_student_deleted.connect(self.refresh_table)
        # self.student_model.signal_student_deleted.connect(self.dialog_popup_view.show_dialog)
        #
        # # Assign refresh student table button
        # self.mainwindow_view.btnRefresh.clicked.connect(self.refresh_table)

    def load_employee_positions_combobox(self):
        positions = self.employee_model.get_employee_positions()
        self.mainwindow_view.cmbEmployeePosition.addItem("")
        self.mainwindow_view.cmbEmployeePosition.addItems(positions)

    def refresh_table(self, s):
        if s:
            self.set_student_table()

    def set_student_table(self, s=None):
        self.student_query.prepare(
            "SELECT studentID,name,age,grade "
            "FROM students "
            "WHERE name LIKE '%' || :student_name || '%' AND "
            "age LIKE '%' || :student_age || '%' AND "
            "grade LIKE '%' || :student_grade || '%'"
        )

        student_name, student_grade, student_age = self.get_student_filters()
        self.student_query.bindValue(":student_name", student_name)
        self.student_query.bindValue(":student_grade", student_grade)
        self.student_query.bindValue(":student_age", student_age)

        self.student_query.exec_()
        self.mainwindow_view.student_sql_query_model.setQuery(self.student_query)

    def set_employee_table(self, s=None):
        self.employee_query.prepare(
            "SELECT employeeID, name, position, salary, joindate "
            "FROM employees "
            "WHERE name LIKE '%' || :employee_name || '%' AND "
            "position LIKE '%' || :employee_position || '%'"
        )

        employee_name, employee_position = self.get_employee_filters()
        self.employee_query.bindValue(":employee_name", employee_name)
        self.employee_query.bindValue(":employee_position", employee_position)

        self.employee_query.exec_()
        self.mainwindow_view.employee_sql_query_model.setQuery(self.employee_query)

    def get_student_filters(self, s=None):
        # Get the text values from the search entries
        student_name = self.mainwindow_view.lineDisplayStudentName.text()
        student_grade = self.mainwindow_view.lineDisplayStudentGrade.text()
        student_age = self.mainwindow_view.lineDisplayStudentAge.text()

        return student_name, student_grade, student_age

    def clear_student_filters(self, s=None):
        self.mainwindow_view.lineDisplayStudentName.clear()
        self.mainwindow_view.lineDisplayStudentAge.clear()
        self.mainwindow_view.lineDisplayStudentGrade.clear()

    def get_employee_filters(self, s=None):
        # Get the text values from the search entries
        employee_name = self.mainwindow_view.lineEmployeeName.text()
        employee_position = self.mainwindow_view.cmbEmployeePosition.currentText()

        return employee_name, employee_position

    def clear_employee_filters(self, s=None):
        self.mainwindow_view.lineEmployeeName.clear()
        self.mainwindow_view.cmbEmployeePosition.clear()
        self.load_employee_positions_combobox()
