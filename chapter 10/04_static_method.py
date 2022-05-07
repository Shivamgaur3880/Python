class Employee:
    company='Google'
    def getsalary(self,signature):
        print("salary is 1000",signature)

    @staticmethod
    def greet():
        print("Have a nice day")


janak= Employee()

janak.getsalary("thanks")
janak.greet()