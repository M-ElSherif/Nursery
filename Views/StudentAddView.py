from PyQt5.QtWidgets import QWidget

from Controller.StudentController import StudentController
from Entities.Student import Student
from Models.StudentModel import StudentModel
from gui.FormAddStudent import Ui_FormAddStudent

''' 
ADD STUDENT FORM CLASS
'''


class StudentAddView(QWidget, Ui_FormAddStudent):
    def __init__(self, student_model, student_controller):
        super().__init__()
        self.setupUi(self)
        self.model: StudentModel = student_model
        self.student_controller: StudentController = student_controller
        self.assign_buttons()

    def assign_buttons(self):
        # Assign add student form buttons
        self.btnSaveStudent.clicked.connect(self.save_button_action)
        self.btnClearStudent.clicked.connect(self.clear_fields)

    def clear_fields(self):
        self.lineAddStudentAge.clear()
        self.lineAddStudentName.clear()
        self.lineAddStudentGrade.clear()

    def save_button_action(self, saved):
        student_name = self.lineAddStudentName.text()
        student_grade = int(self.lineAddStudentGrade.text())
        student_age = int(self.lineAddStudentAge.text())

        student = Student(student_name, student_age, student_grade)

        if self.student_controller.save_student(student):
            self.clear_fields()
