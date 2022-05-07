class Animal:
    def __init__(self):
        
        print("i am animal")

class Pets(Animal): 
    def __init__(self):
        super().__init__()
        print("i am pet")

class Dogs(Pets):
    
    def bark(self):
        super().__init__
        print("dog here")


d=Dogs()
d.bark()