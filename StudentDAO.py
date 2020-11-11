import sqlite3

from dbAccess import DBAccess
from Student import Student


class StudentDAO:

    def __init__(self):
        self.sql_connection = DBAccess.createConnection()

    # TODO: Finish add student feature with QT Designer
    def create_student(self, student):
        cur = self.sql_connection.cursor()

        name = student.name
        grade = student.grade
        age = student.age

        try:
            cur.execute("INSERT INTO students (name, grade, age) VALUES (?,?,?)",
                        (name, grade, age))
            self.sql_connection.commit()
            cur.close()
            return True
        except Exception as e:
            print(e)
            self.sql_connection.rollback()
            cur.close()
            return False

    def delete_student(self, id):
        cur = self.sql_connection.cursor()

        try:
            cur.execute("DELETE FROM students WHERE studentID = ?", (id,))
            self.sql_connection.commit()
        except Exception as e:
            print(e)
            self.sql_connection.rollback()

        cur.close()

    def get_table_fields(self):
        # TODO: make a case statement which has a query for each table in the database
        try:
            cur = self.sql_connection.cursor()
            cur = self.sql_connection.execute('SELECT name,age,grade FROM students')
            fields = [description[0] for description in cur.description]
            cur.close()
            return fields
        except Exception as e:
            print(e)

        cur.close()
