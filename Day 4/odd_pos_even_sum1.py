#String Input
even_sum=0
input_number_string=input("Enter A Number : ")
for digit in input_number_string[::2]:
    digit=int(digit)
    if(not digit%2):
        even_sum+=digit
print(f"The Sum Of Even Numbers Present At Odd Position = {even_sum}")