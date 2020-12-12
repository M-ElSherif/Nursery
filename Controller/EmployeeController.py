from PyQt5.QtCore import QObject

from Entities.Employee import Employee
from Models.EmployeeModel import EmployeeModel


class EmployeeController(QObject):

    def __int__(self, employee_model: EmployeeModel):
        super().__init__()
        self.model: EmployeeModel = employee_model

    def save_employee(self, employee: Employee) -> bool:
        return True if self.model.create_employee(employee) else False

    def update_employee(self, employee: Employee, employee_id: int) -> bool:
        return True if self.model.update_employee(employee, employee_id) else False

    def delete_employee(self, employee_id: int) -> bool:
        return True if self.model.delete_employee(employee_id) else False
