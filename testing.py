from Student import Student
from StudentDAO import StudentDAO

student_dao = StudentDAO()
student_dao.create_student(Student("test",1,1))


