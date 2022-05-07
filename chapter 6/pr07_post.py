post= input("enter post\t")
a="harry"
b="HARRY"
c=post.find(a)
d=post.find(b)
if(c!=-1):
    print("YES POST IS TALKING ABOUT HARRY")
elif(d!=-1):
    print("YES POST IS TALKING ABOUT HARRY")
else:
    print("POST IS TALKING ABOUT SOMEONE ELSE")