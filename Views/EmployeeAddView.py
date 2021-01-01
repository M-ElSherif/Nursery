from datetime import datetime, date

from PyQt5.QtWidgets import QWidget

from Controller.EmployeeController import EmployeeController
from Entities.Employee import Employee
from Models.EmployeeModel import EmployeeModel
from gui.FormAddEmployee import Ui_FormAddEmployee


class EmployeeAddView(QWidget, Ui_FormAddEmployee):
    def __init__(self, employee_model, employee_controller):
        super().__init__()
        self.setupUi(self)
        self.model: EmployeeModel = employee_model
        self.employee_controller: EmployeeController = employee_controller
        self.assign_buttons()
        self.load_employee_positions_combobox()

    def assign_buttons(self):
        # Assign add employee form buttons
        self.btnSaveEmployee.clicked.connect(self.save_button_action)

    def save_button_action(self, saved):
        employee_name: str = self.lineEmployeeName.text()
        employee_role: str = self.cmbEmployeePosition.currentText()
        employee_join_date: str = self.dteEmployeeJoinDate.text()
        employee_salary = float(self.spinEmployeeSalary.cleanText())

        employee = Employee(employee_name, employee_role, employee_salary, employee_join_date)

        if self.employee_controller.save_employee(employee):
            self.clear_fields

    def clear_fields(self):
        self.lineEmployeeName.clear()
        self.cmbEmployeePosition.clear()
        self.dteEmployeeJoinDate.clear()
        self.spinEmployeeSalary.clear()
        self.load_employee_positions_combobox()

    def load_employee_positions_combobox(self):
        positions = self.model.get_employee_positions()
        self.cmbEmployeePosition.addItem("")
        self.cmbEmployeePosition.addItems(positions)
