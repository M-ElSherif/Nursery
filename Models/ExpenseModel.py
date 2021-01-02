from PyQt5.QtCore import QObject, pyqtSignal

from DAO.ExpenseDAO import ExpenseDAO
from Entities.Expense import Expense


class ExpenseModel(QObject):
    signal_expense_saved = pyqtSignal(bool, int)
    signal_expense_deleted = pyqtSignal(bool, int)

    def __init__(self):
        super().__init__()
        self.expenseDAO: ExpenseDAO = ExpenseDAO()

    def create_expense(self, expense: Expense) -> bool:
        if self.expenseDAO.create(expense):
            self.signal_expense_saved.emit(True, 1)

    def read_expense(self, expense_id: int) -> Expense:
        expense = self.expenseDAO.read(expense_id)
        if expense is not None:
            return expense

    def update_expense(self, expense: Expense, expense_id: int) -> bool:
        if self.expenseDAO.update(expense, expense_id):
            self.signal_expense_saved.emit(True, 2)

    def delete_expense(self, expense_id: int) -> bool:
        if self.expenseDAO.delete(expense_id):
            self.signal_expense_deleted.emit(True, 3)

    def get_expense_table_fields(self) -> list:
        table_fields = self.expenseDAO.get_table_fields()
        if (table_fields is not None) or len(table_fields) > 0:
            return table_fields
