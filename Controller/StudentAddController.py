from PyQt5 import QtCore
from PyQt5.QtCore import QObject

from Entities.Student import Student
from Models.StudentModel import StudentModel


class StudentAddController(QObject):

    def __init__(self, student_model):
        super().__init__()

        self.model: StudentModel = student_model

    def save_student(self, student: Student) -> bool:
        if self.model.create_student(student):
            return True
        return False
