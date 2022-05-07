class Calculator:
    
    @staticmethod
    def greet():
        print("hello Welcome to Calculator")

    def __init__(self,num,choice):
        self.num=num
        self.choice=choice
        

    def square(self):
        print(f"Square of {self.num} is {self.num**2} ")

    def cube(self):
        print(f"Cube of {self.num} is {self.num**3} ")
            
    def squareroot(self):
         print(f"Square Root of {self.num} is {self.num**0.5} ")

obj=Calculator(None,None)
obj.greet()


num=int(input('enter number\t'))
choice= int(input(f"enter your choice \n 1.Square of {num} \
            2.Cube of {num}\n3.SquareRoot of {num}\t"))

result=Calculator(num,choice)

if choice == 1:
    result.square()

elif choice == 2:
    result.cube()

elif choice==3:
    result.squareroot()

else:
    print("You entered wrong Choice")