from DAO.EmployeeDAO import EmployeeDAO
from Entities.Employee import Employee
from Entities.Student import Student
from DAO.StudentDAO import StudentDAO

student_dao = StudentDAO()
student_dao.create(Student("test", 1, 1))


employee_dao = EmployeeDAO()
employee_dao.create(Employee("test","Teacher",10000,"2020-01-10"))
employee_dao.delete(5)

