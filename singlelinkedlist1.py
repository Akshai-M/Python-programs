#creat of node
class Node:
    def __init__(self,da):
        self.data = da
        self.next = None
        print("node is created!")
#linked list 
class LinkedList:
    def __init__(self):
        self.head = None

#insertin at front
    def insert_beg(self,ele):
        nn= Node(ele)
        if self.head ==None:
            self.head =nn
        else:
            nn.next=self.head
            self.head =nn
        

#insertion at end 
    def insert_lst(self,ele):
        nn = Node(ele)
        if self.head == None:
            self.head = nn
        else:
            current=self.head  
            while current.next:
                current=current.next
            current.next = nn
#delete node at begining
    def del_beg(self):
        if self.head==None:
            print("list is empty \n")
        else:
            current = self.head
            self.head = current.next
            print(current.data,"deleted")
            del current

#delete node at last
    def del_lst(self):
        if self.head ==None:
            print("list is empty!")
        else:
            current= self.head
            prev =current
            while current.next:
                prev=current
                current=current.next
            prev.next=None
            del current
#to search a node
    def search(self,key):
        if self.head ==None:
            print("list is empty!")
        else:
            cur = self.head
            while cur.next:
                if cur.data == key :
                    print(f"node found! : {key}")
                    break
                else:
                    cur=cur.next
            else:
                print("Node not found")        

#displaying
    def display(self):
        if self.head ==None:
            print("list is empty\n")
        else:
            cur=self.head  
            while cur:
                print(cur.data,end="->")
                cur = cur.next
    def reverse(self):
        cur=self.head
        prev=None
        while cur:
            next_node=cur.next
            cur.next=prev
            prev=cur
            cur=next_node
        self.head=prev 
        
    #insert after node
    def insertAfterNode(self,target,ele):
        nn=Node(ele)
        cur=self.head
        while cur and cur.data!=target:
            cur=cur.next
        if cur:
            nn.next=cur.next
            cur.next=nn 
        else:
            print("Node with data",target,"not found")
#insert at 
# menu driven
list = LinkedList()
while True:
    print(" 1.insert_begining 2.insert_last 3.del_beg 4.del_last 5.search 6. insert_after 7.Reverse 8.d1isplay 9.Exit")
    ch=int(input("enter choice :"))
    if ch == 1:
        ele = int(input("enter data :"))
        list.insert_beg(ele)
    elif ch ==2 :
        ele = int(input("enter data :"))
        list.insert_lst(ele)
    elif ch==3:
        list.del_beg()
    elif ch==4:
        list.del_lst()
    elif ch == 5:
        key =int(input("enter a node/key to search:"))
        list.search(key)
    elif ch == 6:
        target=int(input("Enter the target:"))
        ele = int(input("enter data :"))
        list.insertAfterNode(target,ele)
    elif ch == 7:
        list.reverse()
        list.display()
    elif ch == 8:
        list.display()
    elif ch == 9:
        break

    
# class Node:
#     def _init_(self,da):
#         self.data = da
#         self.next = None

#     def display(self):
#         if self==None:
#             print("list is empty")
#         else:    
#             while self:
#                 print(self.data)
#                 self = self.next



# node1 = Node(10)
# node2 = Node(20)
# node3 = Node(30)
# node4 = Node(40)
# start = node1

# #to link

# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next =None
# start.display()