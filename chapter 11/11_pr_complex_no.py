class Complex:
    def __init__(self,r,i):
        self.real=r
        self.imagenary=i
                                            #pending
    def __add__(self,c2):
        return Complex(self.real+c2.real,self.imagenary+c2.imagenary)

    def __mul__(self,c3):
        self.mul1=(self.real*c3.real)-(self.imagenary*c3.imagenary)
        self.mul2=(self.real*c3.imagenary)+(self.imagenary*c3.real)
        return complex(self.mul1,self.mul2)

    def __str__(self):
        return f"{self.real}+{self.imagenary}j"
c=complex(3,2)
c1=complex(1,7)
print(c+c1)
print(c*c1)
