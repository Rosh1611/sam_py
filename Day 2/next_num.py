#Convert List To Number
def list_to_num(num_list):
    num=0
    for dig in num_list:
        num=num*10+dig
    return num
#Converting Number To List
def num_to_list(num):
    num_list=[]
    while(num>0):
        num_list.append(num%10)
        num//=10
    return num_list[::-1]
#Accepting Input
input_number=int(input("Enter A Positive Integer :"))
#To Find The Next Smallest Number Formed Using Input Number's Digits
def next_num(num):
    num_list=num_to_list(num)
    #The Greatest Combination Of Digits Has Been Achieved, Further Is Not Possible
    if list_to_num(sorted(num_list,reverse=True))==num:
        return "Not Possible"
    index_counter=-2
    while(True):
        num_list[index_counter:]=sorted(num_list[index_counter:],reverse=True)
        if(list_to_num(num_list)>num):
            num_list[index_counter:]=sorted(num_list[index_counter:])
            break
        else:
            index_counter-=1   
    while True:
        if(list_to_num(num_list)<=num):
            new=num_list[index_counter]
            del num_list[index_counter]
            num_list.append(new)
        else:
            num_list[index_counter+1:]=sorted(num_list[index_counter+1:])
            break
    return list_to_num(num_list)
print(f"The Next Smallest Number Formed Using Digits Of {input_number} Is",next_num(input_number))

