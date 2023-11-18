class Node:
    def __init__(self,val):
        self.data=val
        self.next=None
class Queue:
    def __init__(self):
        self.front=self.rear=None
    def enq(self):
        ele=int(input("Enter element:"))
        nn=Node(ele)
        if self.rear is None:
            self.front=self.rear=nn
        else:
            self.rear.next=nn
            self.rear=nn
    def peek(self):
        if self.front is None:
            print("Queue Empty")
        else:
            print(self.front.data,end=' ')
que=Queue()
while True:
    choice = int(input("Enter your choice:"))
    

    if choice == 1:
        que.equ()

    if choice == 2:
        que.display()

    if choice == 3:
        que.peek()

    if choice == 4:
        break
