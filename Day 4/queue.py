class Queue:
    def __init__(self,size=5):
        self.__queue=[]
        self.__size=size
    def queue_empty(self):
        return True if not len(self.__queue) else False
    def queue_full(self):
        return True if len(self.__queue)==self.__size else False
    def enqueue(self,item):
        #Insert At Rear
        return "Sorry, Queue Is Empty" if self.queue_full() else self.__queue.append(item)
    def dequeue(self):
        #Delete From Front
        return "Sorry, Queue Is Empty" if self.queue_empty() else self.__queue.remove(0)
    def print_queue(self):
        print("Queue")
        for ele in self.__queue:
            print(ele)

class Reversed_Queue:
    def __init__(self,size=5):
        self.__queue=[]
        self.__size=size
    def queue_empty(self):
        return True if not len(self.__queue) else False
    def queue_full(self):
        return True if len(self.__queue)==self.__size else False
    def enqueue(self,item):
        #Insert At Front
        return "Sorry, Queue Is Empty" if self.queue_full() else self.__queue.insert(0,item)
    def dequeue(self):
        #Delete From Rear
        return "Sorry, Queue Is Empty" if self.queue_empty() else self.__queue.pop()
    def print_queue(self):
        print("Queue")
        for ele in self.__queue:
            print(ele)