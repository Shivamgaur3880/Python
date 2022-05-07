num=int(input("enter number to add natural no\t"))
factorial=1
for i in range(1,num+1):
    factorial= factorial*i

print(f"factorial of {num} is {factorial}")