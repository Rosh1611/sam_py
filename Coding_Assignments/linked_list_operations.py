class Node:
    def __init__(self,data):
        self.data=data
        self.link=None

class Linked_List:
    def getnode(self,element):
        return Node(element)
    def insert_at_position(self,first,element,position):
        new_node=self.getnode(element)
        if(position==1):
            new_node.link=first
            return new_node
        temp=first
        while(position>2 and temp):
            temp=temp.link
            position-=1
        if(not temp):
            print("Invalid Position")
            return first
        new_node.link=temp.link
        temp.link=new_node
        return first
    def delete_from_position(self,first,position):
        if(not first):
            print("Sorry, List Is Empty.\nNo Elements To Delete")
        elif(position==1):
            first=first.link
        else:
            current_node=first
            previous_node=None
            while(position>1 and current_node):
                previous_node=current_node
                current_node=current_node.link
                position-=1
            if(not current_node):
                print("Invalid Position")
                return first
            previous_node.link=current_node.link
            current_node=None
        return first
    def recur_print_list(self,first):
        print(first.data,end=' ')
        if(first.link):
            self.recur_print_list(first.link)
    def print_reversed_list(self,first):
        if(first.link):
            self.print_reversed_list(first.link)
        print(first.data,end=' ')

first=None
list_object=Linked_List()
"""
first=list_object.insert_at_position(first,10,1)
first=list_object.insert_at_position(first,24,1)
first=list_object.insert_at_position(first,84,1)
first=list_object.insert_at_position(first,54,2)
#84 54 24 10
list_object.recur_print_list(first)
print()
first=list_object.delete_from_position(first,4)
list_object.recur_print_list(first)
print()
first=list_object.delete_from_position(first,4)
list_object.recur_print_list(first)
print()
first=list_object.delete_from_position(first,1)
list_object.recur_print_list(first)
print()
first=list_object.delete_from_position(first,10)
list_object.recur_print_list(first)
print()
first=list_object.delete_from_position(first,2)
list_object.recur_print_list(first)
print()
first=list_object.delete_from_position(first,1)
print()
#list_object.print_reversed_list(first)
#24 54 40 84 10 30 20
"""
