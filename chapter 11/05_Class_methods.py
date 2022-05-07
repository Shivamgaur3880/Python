class Employee:
    company="Bharat gas"
    salary=5600
    salaryBonus=500
    totalsalary=salary+salaryBonus


    @classmethod
    def changesalary(cls,sal):      #jo bhi isme change hoga class me hoga
        cls.salary=sal
    
    
    # def changesalary(self,sal):
    #     # self.salary=sal
    #     self.__class__.salary=sal
    #     print(self.salary)

e=Employee()
print(e.salary)
e.changesalary(700)
print(Employee.salary)