from DAO.AbstractDAO import AbstractDAO
from Database.DBManager import DBManager
from Entities.Student import Student


class StudentDAO(AbstractDAO):

    def __init__(self):
        self.sql_connection = DBManager.createConnection()

    def create(self, student: Student) -> bool:
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

    def read(self, student_id) -> list:
        cur = self.sql_connection.cursor()

        try:
            cur.execute("SELECT studentID,name,grade,age "
                        "FROM students "
                        "WHERE studentID = ?", (student_id,))
            row = cur.fetchone()
            cur.close()
            return Student(row[1],row[2],row[3])
        except Exception as e:
            print(e)
            self.sql_connection.close()

    def update(self, student, student_id) -> bool:
        cur = self.sql_connection.cursor()

        try:
            cur.execute("UPDATE students "
                        "SET name= ?, grade = ?, age = ? "
                        "WHERE studentID = ?", (student.name, student.grade, student.age, student_id))
            self.sql_connection.commit()
            return True
        except Exception as e:
            print(e)
            self.sql_connection.rollback()

        cur.close()
        return False

    def delete(self, student_id) -> bool:
        cur = self.sql_connection.cursor()

        try:
            cur.execute("DELETE FROM students WHERE studentID = ?", (student_id,))
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
            cur = self.sql_connection.execute('SELECT name,age,grade FROM students')
            fields = [description[0] for description in cur.description]
            cur.close()
            return fields
        except Exception as e:
            print(e)

        cur.close()
