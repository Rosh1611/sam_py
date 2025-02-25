#Integer Stack

class Front_Stack:
    #Front Operations
    def __init__(self,size=5):
        self.__stack=[]
        self.__size=size
    def stack_underflow(self):
        return True if not len(self.__stack) else False
    def stack_overflow(self):
        return True if len(self.__stack)==self.__size else False
    def push(self,item):
        #Insert At Front
        return "Sorry, Stack Is Empty" if self.stack_overflow() else self.__stack.insert(0,item)
    def pop(self):
        #Delete From Front
        return "Sorry, Stack Is Empty" if self.stack_underflow() else self.__stack.remove(0)
    def print_stack(self):
        print("Stack")
        for ele in self.__stack:
            print(ele)
class Rear_Stack:
    #Rear Operations
    def __init__(self,size=5):
        self.__stack=[]
        self.__size=size
    def stack_underflow(self):
        return True if not len(self.__stack) else False
    def stack_overflow(self):
        return True if len(self.__stack)==self.__size else False
    def push(self,item):
        #Insert At Rear
        return "Sorry, Stack Is Full" if self.stack_overflow() else self.__stack.append(item)
    def pop(self):
        #Delete From Rear
        return "Sorry, Stack Is Empty" if self.stack_underflow() else self.__stack.pop()
    def print_stack(self):
        print("Stack")
        for ele in self.__stack[::-1]:
            print(ele)
def menu():
    print("Stack Menu".center(50))
    stacks={1:(Front_Stack,"Front"),2:(Rear_Stack,"Rear")}
    while True:
        stack_choice=int(input("Where Do You Wish The Top To Be Pointed At?\n1. Front\n2. Rear\n[Press 0 If You Wish To Exit]\nYour Choice : "))
        if(not stack_choice):
            print("Thank You")
            return
        if stack_choice in stacks:
            stack_size=5
            yes_or_no=input("Do You To Want Designate The Size Of The Stack [Yes/No] : ")
            if(yes_or_no.upper() in ["YES","Y"]):
                stack_size=input("Enter The Size Of Stack : ")
            stack_object=stacks[stack_choice][0](stack_size)
        else:
            print("Invalid Choice\nPlease Try Again")
            continue
        print(f"\nThe Operations Will Be Performed From {stacks[stack_choice][1]}")
        while True:
            operation_choice=int(input("\nOperations\n1. Push\n2. Pop\n3. Print Stack\n[Press 0 If You Wish To Terminate The Current Stack]\nEnter Your Choice : "))
            if(not operation_choice):
                print(f"\n{stacks[stack_choice][1]} Stack Terminated!!")
                break
            if(operation_choice==1):
                input_element=int(input("Enter The Element You Wish To Push : "))
                print(stack_object.push(input_element))

stack1=Front_Stack()
print(stack1.pop())
stack1.push('A')
stack1.print_stack()
stack1.push('B')
stack1.print_stack()
stack1.push('C')

