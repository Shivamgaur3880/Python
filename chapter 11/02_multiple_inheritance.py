class Employee:
    company="visa"
    ecode=120

class Freelancer:
    company="fiverr"
    level=0

    def upgradelevel(self):
        self.level=self.level+1
        return self.level
        

class Programmer(Employee,Freelancer):
    name="janak"

p=Programmer()
print(p.upgradelevel())
print(p.level)
print(p.company)