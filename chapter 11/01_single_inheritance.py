class Employee:
    company="Google"

    def showDetail(self):
        print("This is Employee")

class Programmer(Employee):
    language="python"
    
    def getLanguage(self):
        print(f"The Language is {self.language}")

e=Employee()
print(e.company)
pr=Programmer()
pr.company="Youtube"
print(pr.company)
pr.showDetail()
pr.getLanguage()
