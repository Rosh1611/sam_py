def check_perfect_square(number):
    print(f"{number} Is A Perfect Square." if ((number**0.5)%1==0) else f"{number} Is Not A Perfect Square.")
input_number=int(input("Enter A Positive Integer To Check If It Is A Perfect Square : "))
check_perfect_square(input_number)