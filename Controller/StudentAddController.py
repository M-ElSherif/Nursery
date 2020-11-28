from PyQt5 import QtCore
from PyQt5.QtCore import QObject

from Entities.Student import Student
from Models.StudentModel import StudentModel
from Views.MainWindow import MainWindow
from Views.StudentAddView import StudentAddView


class StudentAddController(QObject):
    signalPassDataToMainForm = QtCore.pyqtSignal(bool)

    def __init__(self, main_window):
        super().__init__()
        self.model: StudentModel = StudentModel()
        self.view: StudentAddView = StudentAddView()
        self.main_window: MainWindow = main_window
        self.assign_buttons()

    def show(self, s=None):
        self.view.show()

    def hide(self, s=None):
        self.view.hide()

    def assign_buttons(self):
        # Assign add student form button
        self.view.btnSaveStudent.clicked.connect(self.save_button_action)

    def clear_fields(self):
        self.view.lineAddStudentAge.clear()
        self.view.lineAddStudentName.clear()
        self.view.lineAddStudentGrade.clear()

    def save_button_action(self, saved):
        student_name = self.view.lineAddStudentName.text()
        student_grade = int(self.view.lineAddStudentGrade.text())
        student_age = int(self.view.lineAddStudentAge.text())

        student = Student(student_name, student_age, student_grade)

        # self.model.create_student(student)
        if self.model.create_student(student):
            self.signalPassDataToMainForm.emit(True)
            self.clear_fields()
