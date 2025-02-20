def check_perfect_cube(input_number):
    print(f"{input_number} Is A Perfect Cube." if (round(input_number**(1/3)))**3==input_number else f"{input_number} Is Not A Perfect Cube.")
input_number=int(input("Enter Number : "))
check_perfect_cube(input_number)
