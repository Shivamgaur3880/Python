class Railway:
    formtype= "railway form"
    def printdata(self):
        print(f"Name of Applicant is {self.name}")
        print(f"Name of Train is {self.train}")


janakapplication= Railway()

print(janakapplication.formtype)
janakapplication.name="janak"
janakapplication.train="rajdhani express"
janakapplication.printdata()
