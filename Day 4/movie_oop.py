
chosen_movie={}
#movies={1:ABC,2:BBB,3:CCC}
class movie:
    __seats={}
    def __init__(self):
        print("Welcome To Movie Ticket Booking System")
        for no in range(5):
            row=chr(no+65)
            self.__seats[row]=[7]
            self.__seats[row][1::]=[str(i) for i in range(1,7)]
    def printdict(self,dic):
        for i in range(5):
            i=chr(i+65)
            print(i,end="  ")
            for j in range(1,7):
                print("%02s"%dic[i][j],end=" ")
            print("(Available = %d)"%dic[i][0])
    def update(self,dic):
        no_of_seats=int(input("How Many Seats Do You Wish To Book?\n"))
        print("Please Enter The Seats One After The Other [Example-A5/a5]")
        while(no_of_seats>0):
            row,seat_no=list(input().upper())
            seat_no=int(seat_no)
            cur_seat=self.__seats[row][seat_no]
            if cur_seat=='X':
                print("Sorry, The Entered Seat Has Been Booked\nPlease Enter A Different Seat\n")
                continue
            self.__seats[row][seat_no]='X'
            self.__seats[row][0]-=1
            no_of_seats-=1
    def getseats(self):
        return self.__seats

M1=movie()
print("Before")
seats=M1.getseats()
M1.printdict(seats)

M1.update(seats)
print("\nAfter")
M1.printdict(seats)
#ch=int(input("Enter Your Choice : "))
#chosen_movie=movies[ch]
