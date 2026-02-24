class Employee:
    company_name = "TCS"

    def __init__(self, employee_name):
        self.employee_name = employee_name

e1 = Employee("Anu")
print(e1.employee_name, Employee.company_name)