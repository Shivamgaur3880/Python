def great(a,b,c):
    if a>b:
        a1=a
    else:                                     #concept 1
        a1=b
    if a1>c:
        return a1
    else:
        return c

num1=great(44,66,23)
print(num1)

def max(n1,n2,n3):
    if n1>n2:
        if n1>n3:
            return n1
        else:
            return n3
                                         #concept 2
    else:
        if n2>n3:
            return n2
        else:
            return n3

num=max(6,5,33)
print(num)
