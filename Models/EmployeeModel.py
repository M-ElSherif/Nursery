from PyQt5.QtCore import QObject, pyqtSignal

from DAO.EmployeeDAO import EmployeeDAO
from Entities.Employee import Employee


class EmployeeModel(QObject):
    signal_employee_saved = pyqtSignal(bool, int)
    signal_employee_deleted = pyqtSignal(bool, int)

    def __init__(self):
        super().__init__()
        self.employeeDAO = EmployeeDAO()

    def create_employee(self, employee: Employee) -> bool:
        if self.employeeDAO.create(employee):
            self.signal_employee_saved.emit(True, 1)

    def read_employee(self, employee_id: int) -> Employee:
        employee = self.employeeDAO.read(employee_id)
        if employee is not None:
            return employee

    def update_employee(self, employee: Employee, employee_id: int) -> bool:
        if self.employeeDAO.update(employee, employee_id):
            self.signal_employee_saved.emit(True, 2)

    def delete_employee(self, employee_id) -> bool:
        if self.employeeDAO.delete(employee_id):
            self.signal_employee_deleted.emit(True, 3)

    def get_employee_table_fields(self) -> list:
        table_fields = self.employeeDAO.get_table_fields()
        if (table_fields is not None) or len(table_fields) > 0:
            return table_fields

    def get_employee_positions(self) -> list:
        positions = self.employeeDAO.get_employee_positions()
        print(positions)
        if (positions is not None) or len(positions) > 0:
            return positions
