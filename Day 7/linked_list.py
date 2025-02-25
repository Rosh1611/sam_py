from sys import exit
class Node:
    def __init__(self,data):
        self.data=data
        self.link=None
class List:
    def __init__(self):
        self.first=None
    def getnode(self,input_data):
        new_node=Node(input_data)
        return new_node
    def insert_at_position(self,element,position):
        new_node=self.getnode(element)
        if(not self.first and position==1):
            self.first=new_node
            return new_node
        if(not self.first):
            print("Invalid Position")
            return self.first
        temp=self.first
        while(position>2 and temp):
            temp=temp.link
            position-=1
        if(position>2):
            print("Invalid Position")
            return self.first
        new_node.link=temp.link
        temp.link=new_node
        return self.first
    def print_list(self):
        print("Linked List : ",end="")
        temp=self.first
        while(temp):
            print(temp.data,end=" ")
            temp=temp.link
class Menu:
    def invalid_choice(self):
        print('Invalid choice entered')
    def end_of_program(self):
        exit('End of Program')
    def match_user_choice(self, choice, linked_list):
        match choice:
            case 1 :
                input_element=int(input("Enter The Element You Wish To Insert : "))
                input_position=int(input("Enter The Position At Which You Wish To Insert : "))
                linked_list.insert_at_position(input_element,input_position)
            case 3 :
                linked_list.print_list()
            case 7 :
                self.end_of_program()
            case _ :
                self.invalid_choice()

    def run_menu(self):
        linked_list =List()
        while True:
            choice = int(input('\n1:Ins_pos 2:Delete 3:InOrder 4:PreOrder 5:PostOrder 6:Search 7:Exit.  Your choice: '))
            self.match_user_choice(choice, linked_list)
trial=List()
#trial.run_menu()
trial.first=trial.insert_at_position(10,1)
trial.print_list()
trial.first=trial.insert_at_position(20,3)
trial.first=trial.insert_at_position(20,2)
#trial.first=trial.insert_at_position(15,2)
#trial.first=trial.print_list()

