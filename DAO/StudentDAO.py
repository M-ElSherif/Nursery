from DAO.AbstractDAO import AbstractDAO
from Database.DBManager import DBManager
from Entities.Student import Student


class StudentDAO(AbstractDAO):

    def __init__(self):
        self.sql_connection = None

    def create(self, student: Student) -> bool:
        cur = None

        name = student.name
        grade = student.grade
        age = student.age

        try:
            self.sql_connection = DBManager.create_connection()
            cur = self.sql_connection.cursor()
            cur.execute("INSERT INTO students (name, grade, age) VALUES (?,?,?)",
                        (name, grade, age))
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

    def read(self, student_id) -> Student:
        cur = None

        try:
            self.sql_connection = DBManager.create_connection()
            cur = self.sql_connection.cursor()
            cur.execute("SELECT studentID,name,grade,age "
                        "FROM students "
                        "WHERE studentID = ?", (student_id,))
            row = cur.fetchone()
            cur.close()
            self.sql_connection.close()
            return Student(row[1], row[2], row[3])
        except Exception as e:
            print(e)
            self.sql_connection.close()

    def update(self, student, student_id) -> bool:
        cur = None

        try:
            self.sql_connection = DBManager.create_connection()
            cur = self.sql_connection.cursor()
            cur.execute("UPDATE students "
                        "SET name= ?, grade = ?, age = ? "
                        "WHERE studentID = ?", (student.name, student.grade, student.age, student_id))
            self.sql_connection.commit()
            self.sql_connection.close()
            return True
        except Exception as e:
            print(e)
            self.sql_connection.rollback()

        cur.close()
        self.sql_connection.close()
        return False

    def delete(self, student_id) -> bool:
        cur = None

        try:
            self.sql_connection = DBManager.create_connection()
            cur = self.sql_connection.cursor()
            cur.execute("DELETE FROM students WHERE studentID = ?", (student_id,))
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
            cur = self.sql_connection.execute('SELECT name,age,grade FROM students')
            fields = [description[0] for description in cur.description]
            cur.close()
            self.sql_connection.close()
            return fields
        except Exception as e:
            print(e)

        cur.close()
        self.sql_connection.close()
