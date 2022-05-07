with open("z_this.txt") as f:
    content= f.read()



with open("z_copied.txt") as f:
    content1= f.read()
    
if content==content1:
    print("same")
else:
    print("not same")