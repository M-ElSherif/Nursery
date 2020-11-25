from Entities.Student import Student
from Models.StudentModel import StudentModel
from Views.StudentAddView import StudentAddView


class StudentAddController:

    def __init__(self, main_window):
        self.model: StudentModel = StudentModel()
        self.view: StudentAddView = StudentAddView()
        from main import MainWindow
        self.main_window: MainWindow = main_window
        self.assign_buttons()

    def show(self, s=None):
        self.view.show()

    def hide(self, s=None):
        self.view.hide()

    def assign_buttons(self):
        # Assign add student form button
        self.view.btnSaveStudent.clicked.connect(self.save_button_action)

    def save_button_action(self, saved):
        student_name = self.view.lineAddStudentName.text()
        student_grade = int(self.view.lineAddStudentGrade.text())
        student_age = int(self.view.lineAddStudentAge.text())

        student = Student(student_name, student_age, student_grade)

        if self.model.create_student(student):
            self.main_window.set_student_table()


