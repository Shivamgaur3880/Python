num=int(input("enter a number"))

def sum(num):
    if num==1:
        return 1
    else:
        return num+sum(num-1)

a=sum(num)

print(a)