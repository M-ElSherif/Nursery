from PyQt5.QtCore import QObject, pyqtSignal

from DAO.StudentDAO import StudentDAO
from Entities.Student import Student


class StudentModel(QObject):
    signal_student_saved = pyqtSignal(bool, int)
    signal_student_deleted = pyqtSignal(bool, int)

    def __init__(self):
        super().__init__()
        self.studentDAO = StudentDAO()

    def create_student(self, student: Student) -> bool:
        if self.studentDAO.create(student):
            self.signal_student_saved.emit(True, 1)

    def read_student(self, student_id: int) -> Student:
        student = self.studentDAO.read(student_id)
        if student is not None:
            return student

    def update_student(self, student: Student, student_id: int) -> bool:
        if self.studentDAO.update(student, student_id):
            self.signal_student_saved.emit(True, 2)

    def delete_student(self, student_id: int) -> bool:
        if self.studentDAO.delete(student_id):
            self.signal_student_deleted.emit(True, 3)

    def get_student_table_fields(self) -> list:
        table_fields = self.studentDAO.get_table_fields()
        if (table_fields is not None) or len(table_fields) > 0:
            return table_fields
