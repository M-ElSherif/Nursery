from Database.DBManager import DBManager


class StudentDAO:

    def __init__(self):
        self.sql_connection = DBManager.createConnection()

    def create_student(self, student) -> bool:
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

    def update_student(self, student, studentID) -> bool:
        cur = self.sql_connection.cursor()

        try:
            cur.execute("UPDATE students "
                        "SET name= ?, grade = ?, age = ? "
                        "WHERE studentID = ?", (student.name, student.grade, student.age, studentID))
            self.sql_connection.commit()
            return True
        except Exception as e:
            print(e)
            self.sql_connection.rollback()

        cur.close()
        return False

    def delete_student(self, student_id) -> bool:
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
