from PyQt5.QtCore import QObject, pyqtSignal

from DAO.StudentDAO import StudentDAO
from Entities.Student import Student


class StudentModel(QObject):
    signal_student_saved = pyqtSignal(bool)
    signal_student_deleted = pyqtSignal(bool)

    def __init__(self):
        super().__init__()
        self.studentDAO = StudentDAO()

    def create_student(self, student) -> bool:
        if self.studentDAO.create(student):
            self.signal_student_saved.emit(True)

    def read_student(self, student_id) -> Student:
        student_row = self.studentDAO.read(student_id)
        if student_row is not None:
            student_name = student_row[1]
            student_grade = student_row[3]
            student_age = student_row[2]
            return Student(student_name, student_age,student_grade)

    def update_student(self, student, student_id) -> bool:
        if self.studentDAO.update(student, student_id):
            self.signal_student_saved.emit(True)

    def delete_student(self, student_id) -> bool:
        if self.studentDAO.delete(student_id):
            self.signal_student_deleted.emit(True)

    def get_student_table_fields(self) -> list:
        table_fields = self.studentDAO.get_table_fields()
        if (table_fields is not None) or len(table_fields) > 0:
            return table_fields
