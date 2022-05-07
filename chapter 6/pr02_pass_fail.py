mark1= int(input("enter marks of physics\t"))
mark2= int(input("enter marks of chemistry\t"))
mark3= int(input("enter marks of mathmatics\t"))
totalmarks=mark1+mark2+mark3
totalpercentage=(totalmarks)*(100/300)
if(totalpercentage<40):
    print("\tyou are fail")
elif(mark1<33 or mark2<33 or mark3<33):
    print("you are fail")
else:
    print("\tcongratulation you are pass")