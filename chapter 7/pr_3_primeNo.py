num=int(input("Enter number to check prime\t"))
prime=True
for i in range(2,num):
    if num%i==0:
        prime=False
        break

if prime is True:
    print("This is prime number")
else:
    print("That is not prime")
