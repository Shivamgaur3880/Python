import random
random_number=random.randint(1,100)
print(random_number)

guesses=0
guess_no=None
while random_number!=guess_no:
    guesses+=1
    guess_no=int(input("Enter Number\t"))

    if random_number==guess_no:
        print("Congratulation......You Have Correct Guess")
        print(f"guesses are {guesses}")

    elif random_number<guess_no:
         print("Sorry....Enter a Larger Number")

    elif random_number>guess_no:
            print("Sorry....Enter a Smaller Number")

with open("hiscore.txt") as f:
    file=f.read()

if guesses<int(file):
    print(f"Congratulation You Have Highscore of..{guesses}.. Guesses")
    with open("hiscore.txt",'w') as f:
        f.write(str(guesses))
