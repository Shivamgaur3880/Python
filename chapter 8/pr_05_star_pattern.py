lines=int(input("enter no.of lines"))

def star(lines):
    for j in range(lines):
        for i in range(lines-j):
            print("*",end="")
        print()


a=star(lines)
print(a)
