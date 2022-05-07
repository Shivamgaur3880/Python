class Employee:
    salary=1500
    increment=1.5

    @property
    def salaryAfterIncrement(self):
        return self.salary*self.increment

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,sal):
        self.increment=sal/self.increment


e=Employee()
print(e.salaryAfterIncrement)

e.salaryAfterIncrement=10000
print(e.increment)