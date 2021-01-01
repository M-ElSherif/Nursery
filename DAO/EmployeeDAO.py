from turtle import pos

from DAO.AbstractDAO import AbstractDAO
from Database.DBManager import DBManager
from Entities.Employee import Employee

#TODO: Open a DB connection and close it at the end of each method

class EmployeeDAO(AbstractDAO):

    def __init__(self):
        self.sql_connection = DBManager.createConnection()

    def create(self, employee: Employee) -> bool:
        cur = self.sql_connection.cursor()

        name = employee.name
        position = employee.position
        salary = employee.salary
        join_date = employee.join_date

        try:
            cur.execute("INSERT INTO employees (name, position, salary, joindate) VALUES (?,?,?,?)",
                        (name, position, salary, join_date))
            self.sql_connection.commit()
            cur.close()
            return True
        except Exception as e:
            print(e)
            self.sql_connection.rollback()
            cur.close()
            return False

    def read(self, employee_id: int) -> list:
        cur = self.sql_connection.cursor()

        try:
            cur.execute("SELECT employeeID,name,position,salary,joindate "
                        "FROM employees "
                        "WHERE employeeID = ?", (employee_id,))
            row = cur.fetchone()
            cur.close()
            return Employee(row[1],row[2],row[3],row[4])
        except Exception as e:
            print(e)
            self.sql_connection.close()

    def update(self, employee: Employee, employee_id: int) -> bool:
        cur = self.sql_connection.cursor()

        try:
            cur.execute("UPDATE employees "
                        "SET name= ?, position = ?, salary =? , joindate = ? "
                        "WHERE employeeID = ?", (employee.name, employee.position, employee.salary, employee.join_date, employee_id))
            self.sql_connection.commit()
            return True
        except Exception as e:
            print(e)
            self.sql_connection.rollback()

        cur.close()
        return False

    def delete(self, employee_id: int) -> bool:
        cur = self.sql_connection.cursor()

        try:
            cur.execute("DELETE FROM employees WHERE employeeID = ?", (employee_id,))
            self.sql_connection.commit()
            return True
        except Exception as e:
            print(e)
            self.sql_connection.rollback()

        cur.close()
        return False

    def get_table_fields(self) -> list:
        try:
            cur = self.sql_connection.cursor()
            cur = self.sql_connection.execute('SELECT name, position, salary, joindate FROM employees')
            fields = [description[0] for description in cur.description]
            cur.close()
            return fields
        except Exception as e:
            print(e)

        cur.close()

    def get_employee_positions(self) -> list:
        try:
            cur = self.sql_connection.cursor()
            cur = self.sql_connection.execute('SELECT DISTINCT position FROM employees')
            positions = [position[0] for position in cur.fetchall()]
            cur.close()
            return positions
        except Exception as e:
            print(e)

        cur.close()
