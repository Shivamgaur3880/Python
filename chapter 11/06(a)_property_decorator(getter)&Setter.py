class Test:
    def __init__(self):
        self.var=10
        self._var1=12
        self.__var2=22
        
    @property
    def get_var2(self):                     #getting private variable value
        return self.__var2

    def setter_var2(self,num):              #setting private variable value
        self.__var2=num
        

    def func(self):
        print(self.var)
        print(self._var1)
        print(self.__var2)
    
    def __func(self):                       #private function
        print(self.var)
        print(self._var1)
        print(self.__var2)
        

t=Test()

print(t.var)
print(t._var1)
# print(t.__var2)                   # cant print private variable

t.func()
# t.__func()                           # cannot print private function


print(t.get_var2)

t.setter_var2(134)

print(t.get_var2)
