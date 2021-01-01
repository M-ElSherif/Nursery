from PyQt5.QtWidgets import QWidget, QDataWidgetMapper

from Controller.EmployeeController import EmployeeController
from Entities.Employee import Employee
from Models.EmployeeModel import EmployeeModel
from Views.DialogAlertView import DialogAlertView
from Views.MainWindowView import MainWindowView
from gui.FormEditDeleteEmployee import Ui_FormEditDeleteEmployee

'''
EDIT / DELETE STUDENT FORM CLASS
'''


class EmployeeEditView(QWidget, Ui_FormEditDeleteEmployee):
    def __init__(self, employee_model, employee_controller, main_window):
        super().__init__()
        self.setupUi(self)
        self.employee_model: EmployeeModel = employee_model
        self.employee_controller: EmployeeController = employee_controller
        self.main_window: MainWindowView = main_window
        self.mapper = QDataWidgetMapper()
        self.set_employee_editor()

    def show_editor(self, s=None):
        # load role combobox
        self.load_employee_positions_combobox()

        # Set the selected employee to the editor
        i = self.is_selected()
        if i & i >= 0:
            self.mapper.setCurrentIndex(i)
        self.show()

    def clear_fields(self):
        self.lineEditEmployeeID.clear()
        self.dteEditEmployeeDate.clear()
        self.spinEditEmployeeSalary.clear()
        self.cmbEditEmployeeRole.clear()
        self.load_employee_positions_combobox()

    def load_employee_positions_combobox(self):
        positions = self.employee_model.get_employee_positions()
        self.cmbEditEmployeePosition.addItem("")
        self.cmbEditEmployeePosition.addItems(positions)

    def is_selected(self, s=None) -> int:
        # print(self.selection_model.hasSelection())
        # print(self.selection_model.isRowSelected(0))
        index = self.main_window.tblEmployees.selectionModel().currentIndex().row()

        return index

    def set_employee_editor(self, index=0):
        self.btnEditEmployeePrevious.clicked.connect(self.mapper.toPrevious)
        self.btnEditEmployeeNext.clicked.connect(self.mapper.toNext)
        self.btnEditEmployeeSave.clicked.connect(self.update_button_action)
        self.btnEditEmployeeDelete.clicked.connect(self.delete_button_action)
        self.mapper.setModel(self.main_window.employee_sql_query_model)
        self.mapper.addMapping(self.lineEditEmployeeID, 0)
        self.mapper.addMapping(self.lineEditEmployeeName, 1)
        self.mapper.addMapping(self.cmbEditEmployeePosition, 2)
        self.mapper.addMapping(self.spinEditEmployeeSalary, 3)
        self.mapper.addMapping(self.dteEditEmployeeDate, 4)

        # self.set_student_table(self.model)
        # if index > 0:
        #     self.mapper.setCurrentIndex(index)
        self.mapper.toFirst()

    def update_button_action(self, saved):
        employee_id: int = int(self.lineEditEmployeeID.text())
        employee_name: str = self.lineEditEmployeeName.text()
        employee_role: str = self.cmbEditEmployeePosition.currentText()
        employee_salary: float = float(self.spinEditEmployeeSalary.cleanText())
        employee_date: str = self.dteEditEmployeeDate.text()

        employee: Employee = Employee(employee_name, employee_role, employee_salary, employee_date)

        self.employee_controller.update_employee(employee, employee_id)

    def delete_button_action(self):
        dialog_alert_view: DialogAlertView = DialogAlertView()
        employee_id = int(self.lineEditEmployeeID.text())

        dialog_alert_view.show_dialog(True, 4)
        self.employee_controller.delete_employee(employee_id)
