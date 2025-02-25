#Integer Input
def is_even(num):
    if(num%2==0):
        return True
    return False

input_number=int(input("Enter A Number : "))
def odd_place_even_sum(number):
    first_sum=second_sum=0
    FLIP=0
    while(number):
        digit=number%10
        if is_even(digit):
            if(not FLIP):
                first_sum+=digit
            else:
                second_sum+=digit
        FLIP=1-FLIP
        digit//=10
    if(FLIP):
        return first_sum
    return second_sum
print(f"The Sum Of Even Numbers Present At Odd Position = {odd_place_even_sum(input_number)}")