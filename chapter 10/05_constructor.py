class Employee:
    company='Google'

    def __init__(self,name,subunit):
        print("Employee class is created")
        self.name=name                          # as constructor initialise first
        self.subunit=subunit                    # so ====> statement transfer to 
                                                # another function
    def getdetail(self):
        print(f"name of Employee is {self.name}")
        print(f"subunit is {self.subunit}")


    def getsalary(self,signature):
        print("salary is 1000",signature)

    @staticmethod
    def greet():
        print("Have a nice day")


janak= Employee("janak","printers")

janak.getdetail()

janak.getsalary("THANKS....",)

janak.greet()