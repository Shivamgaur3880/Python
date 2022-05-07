lst=[1,2,3,4,5]
print(lst)
print(lst[0])
print(lst[0:4:2])
lst[0]=6
print(lst)

var=len(lst)
print(var)

var1=lst.insert(0,7)
print(lst)

var2=lst.remove(2)  #remove number
print(lst)

var3=lst.pop()  #remove end
print(lst)

del lst[3]     #remove position
print(lst)


lst.clear()
print(lst)