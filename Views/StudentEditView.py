from PyQt5.QtWidgets import QWidget, QDataWidgetMapper

from Controller.StudentController import StudentController
from Entities.Student import Student
from Models.StudentModel import StudentModel
from Views.DialogAlertView import DialogAlertView
from Views.MainWindowView import MainWindowView
from gui.FormEditDeleteStudent import Ui_FormEditDeleteStudent

'''
EDIT / DELETE STUDENT FORM CLASS
'''


class StudentEditView(QWidget, Ui_FormEditDeleteStudent):
    def __init__(self, student_model, student_controller, main_window):
        super().__init__()
        self.setupUi(self)
        self.student_model: StudentModel = student_model
        self.student_controller: StudentController = student_controller
        self.main_window: MainWindowView = main_window
        self.mapper = QDataWidgetMapper()
        self.set_student_editor()

    def show_editor(self, s=None):
        i = self.is_selected()
        if i & i >= 0:
            self.mapper.setCurrentIndex(i)
        self.show()

    def clear_fields(self):
        self.lineEditStudentID.clear()
        self.lineEditStudentAge.clear()
        self.lineEditStudentName.clear()
        self.lineEditStudentGrade.clear()

    def is_selected(self, s=None) -> int:
        # print(self.selection_model.hasSelection())
        # print(self.selection_model.isRowSelected(0))
        index = self.main_window.tblStudents.selectionModel().currentIndex().row()

        return index

    def set_student_editor(self, index=0):
        self.btnEditStudentPrevious.clicked.connect(self.mapper.toPrevious)
        self.btnEditStudentNext.clicked.connect(self.mapper.toNext)
        self.btnEditStudentSave.clicked.connect(self.update_button_action)
        self.btnEditStudentDelete.clicked.connect(self.delete_button_action)
        self.mapper.setModel(self.main_window.student_sql_query_model)
        self.mapper.addMapping(self.lineEditStudentID, 0)
        self.mapper.addMapping(self.lineEditStudentName, 1)
        self.mapper.addMapping(self.lineEditStudentGrade, 2)
        self.mapper.addMapping(self.lineEditStudentAge, 3)

        # self.set_student_table(self.model)
        # if index > 0:
        #     self.mapper.setCurrentIndex(index)
        self.mapper.toFirst()

    def update_button_action(self, saved):
        student_id = int(self.lineEditStudentID.text())
        student_name = self.lineEditStudentName.text()
        student_grade = self.lineEditStudentGrade.text()
        student_age = self.lineEditStudentAge.text()

        student: Student = Student(student_name, student_age, student_grade)

        self.student_edit_controller.update_student(student, student_id)

    def delete_button_action(self):
        dialog_alert_view: DialogAlertView = DialogAlertView()
        student_id = int(self.lineEditStudentID.text())

        dialog_alert_view.show_dialog(True, 4)
        self.student_edit_controller.delete_student(student_id)
