def check_perfect_cube(number):
    print(f"{number} Is A Perfect Cube." if (round(number**(1/3)))**3==number else f"{number} Is Not A Perfect Cube.")
input_number=int(input("Enter A Positive Integer To Check If It Is A Perfect Cube : "))
check_perfect_cube(input_number)
