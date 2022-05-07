num=int(input("which table you want\t"))
print("\nBy For loop")
for i in range(1,11):

    # print(str(num) +" X " +  str(i) +' = ' +str(num*i))
    print(f"{num} X {i} = {num*i}")      # f strings
   

a=1
print("By While loop")
while a<11:
    print(f"{num} X {a} = {num*a}")
    a=a+1