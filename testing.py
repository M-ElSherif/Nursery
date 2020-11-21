from Entities.Student import Student
from DAO.StudentDAO import StudentDAO

student_dao = StudentDAO()
student_dao.create(Student("test", 1, 1))


