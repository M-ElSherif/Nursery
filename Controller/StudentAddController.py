from PyQt5 import QtCore
from PyQt5.QtCore import QObject

from Entities.Student import Student
from Models.StudentModel import StudentModel


class StudentAddController(QObject):
    signal_refresh_table = QtCore.pyqtSignal(bool)

    def __init__(self, student_model):
        super().__init__()

        self.model: StudentModel = student_model

    def save_student(self, student: Student) -> bool:
        if self.model.create_student(student):
            self.signal_refresh_table.emit(True)
            return True
        return False
