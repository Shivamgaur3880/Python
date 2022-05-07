class C2dVec:
    def __init__(self,i,j):             # self is refering to object(v2d calling it)
        self.icap=i
        self.jcap=j
    
    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"
        
class C3dVec(C2dVec):
    def __init__(self,i,j,k):
        super().__init__(i,j)           # not using self===> use for any object
        self.kcap=k

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"


v2d=C2dVec(1,2)
v3d=C3dVec(4,6,8)
print(v2d)
print(v3d)