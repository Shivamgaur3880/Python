mark1=int(input("enter your marks 1\t"))
mark2=int(input("enter your marks 2\t"))
mark3=int(input("enter your marks 3\t"))
mark4=int(input("enter your marks 4\t"))
mark5=int(input("enter your marks 5\t"))

total= (mark1 + mark2 + mark3 + mark4 + mark5)/5
if total>=90:
    GRADE="EXCILLENT"
elif total>=80:
    GRADE="A"
elif total>=70:
    GRADE="B"
if total>=60:
    GRADE="C"
elif total>=50:
    GRADE="D"
else:
    GRADE="F"

print("your GRADE is\t" + GRADE)