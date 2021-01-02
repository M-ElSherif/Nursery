from DAO.AbstractDAO import AbstractDAO
from Database.DBManager import DBManager
from Entities.Expense import Expense


class ExpenseDAO(AbstractDAO):

    def __init__(self):
        self.sql_connection = None

    def create(self, expense: Expense) -> bool:
        cur = None

        category = expense.category
        description = expense.description
        exp_type = expense.exp_type
        cost = expense.cost
        date = expense.date

        try:
            self.sql_connection = DBManager.create_connection()
            cur = self.sql_connection.cursor()
            cur.execute("INSERT INTO expenses (category, description, type, cost, date) VALUES (?,?,?,?,?)",
                        (category, description, exp_type, cost, date))
            self.sql_connection.commit()
            cur.close()
            self.sql_connection.close()
            return True
        except Exception as e:
            print(e)
            self.sql_connection.rollback()
            cur.close()
            self.sql_connection.close()
            return False

    def read(self, expense_id: int) -> Expense:
        cur = None

        try:
            self.sql_connection = DBManager.create_connection()
            cur = self.sql_connection.cursor()
            cur.execute("SELECT expenseID, category, description, type, cost, date "
                        "FROM expenses "
                        "WHERE expenseID = ?", (expense_id,))
            row = cur.fetchone()
            cur.close()
            self.sql_connection.close()
            return Expense(row[1], row[3], row[4], row[5], row[2])
        except Exception as e:
            print(e)
            self.sql_connection.close()

    def update(self, expense: Expense, expense_id: int) -> bool:
        cur = None

        try:
            self.sql_connection = DBManager.create_connection()
            cur = self.sql_connection.cursor()
            cur.execute("UPDATE expenses "
                        "SET category = ?, description = ?, type = ?, cost = ?, date = ? "
                        "WHERE expenseID = ?", (
                            expense.category, expense.description, expense.exp_type, expense.cost, expense.date,
                            expense_id))
            self.sql_connection.commit()
            self.sql_connection.close()
            return True
        except Exception as e:
            print(e)
            self.sql_connection.rollback()

        cur.close()
        self.sql_connection.close()
        return False

    def delete(self, expense_id: int) -> bool:
        cur = None

        try:
            self.sql_connection = DBManager.create_connection()
            cur = self.sql_connection.cursor()
            cur.execute("DELETE FROM expenses WHERE expenseID = ?", (expense_id,))
            self.sql_connection.commit()
            self.sql_connection.close()
            return True
        except Exception as e:
            print(e)
            self.sql_connection.rollback()

        cur.close()
        self.sql_connection.close()
        return False

    def get_table_fields(self) -> list:
        cur = None

        try:
            self.sql_connection = DBManager.create_connection()
            cur = self.sql_connection.cursor()
            cur = self.sql_connection.execute('SELECT category, description, type, cost, date FROM expenses')
            fields = [description[0] for description in cur.description]
            cur.close()
            self.sql_connection.close()
            return fields
        except Exception as e:
            print(e)

        cur.close()
        self.sql_connection.close()
