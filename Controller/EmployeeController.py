from PyQt5.QtCore import QObject

from Entities.Employee import Employee
from Entities.Student import Student
from Models.EmployeeModel import EmployeeModel
from Models.StudentModel import StudentModel


class EmployeeController(QObject):

    def __init__(self, employee_model):
        super().__init__()
        self.model: EmployeeModel = employee_model

    def save_employee(self, employee: Employee) -> bool:
        if self.model.create_employee(employee):
            return True
        return False

    def delete_employee(self, employee_id: int) -> bool:
        if self.model.delete_employee(employee_id):
            return True
        return False

    def update_employee(self, employee: Employee, employee_id: int) -> bool:
        if self.model.update_employee(employee, employee_id):
            return True
        return False
