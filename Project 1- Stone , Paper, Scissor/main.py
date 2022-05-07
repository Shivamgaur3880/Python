import random
    

def game(you,comp):
    if you==comp:
        return None
    elif you=='r':
        if comp=='p':
            return False
        elif comp=='s':
            return True
    elif you=='p':
        if comp=='s':
            return False
        elif comp=='r':
            return True     
    elif you=='s':
        if comp=='r':
            return False
        elif comp=='p':
            return True



you=input("Enter your Choice  r-rock  p-paper  s-scissor\t")

comp=1

random_No= random.randint(1,3)

if random_No==1:
    comp='r'
elif random_No==2:
    comp='p'
else:
    comp='s'


a=game(you,comp)


if a==None:
    
    print(f"Compuer Choose {comp}   You Choose {you} \n GAME TIE")   

if a==False:
    
    print(f"Compuer Choose {comp}   You Choose {you} \n YOU LOOSE")

if a==True:
    
    print(f"Compuer Choose {comp}   You Choose {you} \n Congratulation YOU WIN")