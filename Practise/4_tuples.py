a=("harsh",'rohan',"sonu","monu",24,24,24)
print(a)
print(type(a))      # a is the object of class tuple

# a=list(a)         # a is the object of class list
# print(type(a))

print(a[0:4:2])

# a[0]="harshit"     # not support change

print(len(a))

var=a.count(24)
print(var)

var1=a.index("sonu")
print(var1)