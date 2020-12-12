from PyQt5 import QtCore
from PyQt5.QtCore import QObject

from Entities.Student import Student
from Models.StudentModel import StudentModel


class StudentController(QObject):

    def __init__(self, student_model):
        super().__init__()
        self.model: StudentModel = student_model

    def save_student(self, student: Student) -> bool:
        if self.model.create_student(student):
            return True
        return False

    def delete_student(self, student_id: int) -> bool:
        return True if self.model.delete_student(student_id) else False

    def update_student(self, student: Student, student_id: int) -> bool:
        return True if self.model.update_student(student, student_id) else False
