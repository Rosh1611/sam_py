#Integer Input Using List
#Converting Number To List
def num_to_list(num):
    num_list=[]
    while(num>0):
        num_list.append(num%10)
        num//=10
    return num_list[::-1]
#Calculates Sum Of Even Numbers
def even_sum(num_list):
    even=0
    for dig in num_list:
        if(not dig%2):
            even+=dig
    return even
#Accepting An Integer Which Is Converted To A List Of Its Digits
input_number_list=num_to_list(int(input("Enter A Number : ")))
#Printng The Result
print(f"The Sum Of Even Numbers Present At Odd Position = {even_sum(input_number_list[::2])}") #Sliced List Is Sent Only With Odd Positions
