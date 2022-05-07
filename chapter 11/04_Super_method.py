class Person:
    
    country="India"
    def takeBreath(self):
        
        print("I am Breathing")

class Employee(Person):
    
    company="Honda"

    def getsalary(self):
        print(f"salary is {self.salary}")

    def takeBreath(self):
        super().takeBreath()
        print("I am Employee...Breathing")

class Programmer(Employee):
    company="fiverr"

    def getsalary(self):
        print("No Salary to programmer")
         
    def takeBreath(self):
        print("I am Programmer....Breathing")
        super().takeBreath()


p=Person()
p.takeBreath()

e=Employee()
e.takeBreath()
print(e.company)

pr=Programmer()
pr.takeBreath()
print(pr.country)