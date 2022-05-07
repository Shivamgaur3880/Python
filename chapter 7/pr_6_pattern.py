print("new pattern\n")
for j in range(4):    
    for i in range(4):
        print("#",end="")
    print()

print("new pattern\n")

for j in range(4):    
    for i in range(j+1):
        print("#",end="")
    print()

print("new pattern\n")

for j in range(4):    
    for i in range(4-j):
        print("#",end="")
    print()


print("new pattern\n")

for j in range(5):    
    for k in range(4-j):
        print(" ",end="")
    for i in range(j):
        print("#",end="")
    print()

print("new pattern\n")

for j in range(5):    
    for k in range(j):
        print(" ",end="")
    for i in range(5-j):
        print("#",end="")
    print()

print("new pattern\n")

for j in range(5):    
    for k in range(4-j):
        print(" ",end="")
    for i in range((2*j)+1):
        print("#",end="")
    for l in range(4-j):
        print(" ",end="")
    print()

print("new pattern\n")

for j in range(5):    
    for k in range(j):
        print(" ",end="")
    for i in range((5-j)+(4-j)):
        print("#",end="")
    for l in range(j):
        print(" ",end="")
    print()

print("new pattern\n")

for j in range(1,10):    
    for i in range(1,j):
        print(i,end="")
    print()

print("new pattern\n")


for row in range(3):
    for col in range(3):
        if (row==1 and col==1):
            print(" ",end="")
        else:
            print("*",end="")
    print()
       