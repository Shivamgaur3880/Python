class Employee:
    company='Google'
    def getsalary(self):
        print("salary is 1000")

janak=Employee()

janak.getsalary()         # is same as Employee.getsalary(janak)
Employee.getsalary(janak)