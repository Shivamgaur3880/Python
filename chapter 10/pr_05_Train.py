

class Train:
    under='Indian Railway'
    
    def bookticket(self):
            name= input("Enter your Name/t")
            ticket=input("How many tickets\t")
            print(f"Congratulation.....{name} Booked {ticket} tickets")
            with open("reservation.txt",'w') as f:
                f.write(name)
            with open("reservation.txt",'a') as f:
                f.write(ticket)

    def status(self):
        n1=input("enter your name\t")
        with open('reservation.txt') as f:
            content=f.read()
            find=content.find(n1)
            if find==-1:
                print("not present")
            else:
                print("Under Process")


    def fair(self):
        print("Indian Railway--Rs 100 per Ticket")


reservation=Train()

print(reservation.under)
choice= int(input("Enter Your Choice \n1 for bookTicket\n\
2 for Status\n3 for fair\n"))

if choice==1:

    reservation.bookticket()

elif choice==2:
    reservation.status()

elif choice==3:
    reservation.fair()

else:
    print("You Entered Wrong Choice")
