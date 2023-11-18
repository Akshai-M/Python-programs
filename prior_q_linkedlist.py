class Node:
    def __init__(self,val,priority):
        self.data=val
        self.priority=priority
        self.next=None
class priorityQueue:
    def __init__(self):
        self.front=None
    def is_empty(self):
        return self.front is None
    def enq(self,data,priority):
        nn=Node(data,priority)
        if self.is_empty() or priority>self.front.priority:
            nn.next=self.front
            self.front=nn
        else:

    def deq(self):
        if self.is_empty():
            print("Queue is Underflow")
            return None
        data=self.font.data
        self.front=self.front.next
        return data
    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            current=self.front
            while current:
                print(f"({current.data},{current.priority})",end=' ')
                current=current.next
            print()
pq=priorityQueue()
while True:
    print("1.Insert 2.Delete 3.Peek 4.Display 5.Exit")
    ch=int(input("Enter choice:"))
    if ch == 1:
        ele=int(input("Enter element to be inserted:"))
        priority=int(input("Enter priority:"))
        pq.enqueue(ele,prior)
