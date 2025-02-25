class Node:
    def __init__(self,data):
        self.data=data
        self.link=None

class Linked_List:
    def getnode(self,element):
        return Node(element)
    def insert_at_front(self,first,element):
        new_node=self.getnode(element)
        new_node.link=first
        return new_node
    def insert_at_end(self,first,element):
        new_node=self.getnode(element)
        if(not first):
            return new_node
        temp=first
        while(temp.link):
            temp=temp.link
        temp.link=new_node
        return first
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
    def print_list(self,first):
        print("Linked List : ",end='')
        temp=first
        while(temp):
            print(temp.data,end=' ')
            temp=temp.link
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
first=list_object.insert_at_front(first,40)
first=list_object.insert_at_front(first,30)
first=list_object.insert_at_front(first,20)
first=list_object.insert_at_front(first,10)
first=list_object.insert_at_position(first,10,2)
first=list_object.insert_at_position(first,24,1)
first=list_object.insert_at_position(first,84,3)
first=list_object.insert_at_position(first,54,2)
first=list_object.insert_at_end(first,30)
first=list_object.insert_at_end(first,20)
list_object.recur_print_list(first)
print()
list_object.print_reversed_list(first)
#24 54 40 84 10 30 20
"""