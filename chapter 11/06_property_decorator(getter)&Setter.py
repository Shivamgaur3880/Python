
class Employee:
    company="Bharat Gas"
    salary=600
    salaryBonus=500
    

    @property                       #also called ========>>>Getter
    def totalsalary(self):
        return self.salary+self.salaryBonus

    @totalsalary.setter
    def totalsalary(self,val):
        self.salaryBonus=val - self.totalsalary
e=Employee()

print(e.totalsalary)
e.totalsalary=5800
print(e.salary)
print(e.salaryBonus)