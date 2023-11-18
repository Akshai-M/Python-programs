
s=[]
top=-1
def push(ele):
    global top
    size=5
    if top == size-1:
        print("Stack is full")
    else:
        top+=1
        s.append(ele)
        print(f"Element {ele} pushed into stack")
def pop():
    global top
    if top==-1:
        print("Stack is underflow")
    else:
        s.remove(s[top])
        top-=1
        print("Element poped")
def display():
    global top
    if top == -1:
        print("Stack is empty")
    else:
        for i in range(top+1):
            print(s[i],end=' ')
           
while True:
    print("\n1.Push 2.Pop 3.Display 4.Exit")
    ch=int(input("Enter your choice:"))
    if ch == 1:
        ele=input("Enter a element:")
        push(ele)
    elif ch == 2:
        pop()
    elif ch == 3:
        display()
    elif ch == 4:
        break
    