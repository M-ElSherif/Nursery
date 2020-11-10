import sqlite3

from dbAccess import DBAccess
from Student import Student

class StudentDAO:

    def __init__(self):
        self.sql_connection = DBAccess.createConnection()

    # TODO: Finish add student feature with QT Designer
    def createStudent(self, student):
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
