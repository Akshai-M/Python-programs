class Node:
    def __init__(self,da):
        self.data=da
        self.next=None
        print("Node is created!")
class LinkedList:
    def __init__(self):
        self.head=None
    def insert_beg(self,ele):
        nn=Node(ele)
        if self.head==None:
            self.head=nn
        else:
            nn.next=self.head
            self.head=nn
    def del_
    def insert_end(self,ele):
        nn=Node(ele)
        if self.head==None:
            self.head=n
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=nn
    def display(self):
        if self.head==None:
            print("List is empty")
        else:
            current=self.head
            while current:
                print(current.data,end=' ')
                current=current.next
            print()        
list=LinkedList()
while True:
    print("1.Insert at beginning\n2.Insert at end\n3.Display")
    choice=int(input("Enter your choice:"))
    if choice==1:
        ele=int(input("Enter a number:"))
        list.insert_beg(ele)
    if choice==2:
        ele=int(input("Enter a number:"))
        list.insert_end(ele)
    if choice==3:
        list.display()