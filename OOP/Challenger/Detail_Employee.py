
class Employee:

    employee_count = 101

    def __init__(self, name, desig, sal) -> None:
        self.name = name
        self.salary = sal
        self.designation = desig
        self.eid = 'e' + str(Employee.employee_count)
        Employee.employee_count += 1

    def show_detail(self):
        print('Name: ',self.name)
        print('Id: ',self.eid)
        print('Designation: ',self.designation)
        print('Salary: ',self.salary)

    @classmethod # 
    def total_emp(cls):
        return cls.employee_count - 101


trung = Employee('Trung','Team Leader',1000000)
print('')
vui = Employee('Vui','memeber',5000000)

trung.show_detail()
vui.show_detail()

print('Total Employee: ',vui.total_emp())
 