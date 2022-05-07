class Number:
    def __init__(self,num):
        self.num=num

    def __add__(self,num2):
        print("addition is")
        return self.num + num2.num

    def __mul__(self,num2):
        print("addition is")
        return self.num * num2.num

    def __str__(self):
        print("Number is")
        return f" {self.num}"

    def __len__(self):
        print("length is")
        return 1

    def __truediv__(self,num2):
        print("division is")
        return self.num / num2.num

n1= Number(2)
n2=Number(3)

sum=n1+n2
print(sum)

mul=n1*n2
print(mul)

print(n1)

print(len(n1))


div=n1/n2
print(div)