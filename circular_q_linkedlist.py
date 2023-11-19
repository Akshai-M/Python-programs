class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if not self.front:
            self.front = self.rear = new_node
            self.rear.next = self.front
        else:
            self.rear.next = new_node
            self.rear = new_node
            self.rear.next = self.front

    def dequeue(self):
        if not self.front:
            print("Queue is empty")
            return None
        elif self.front == self.rear:
            data = self.front.data
            self.front = self.rear = None
            return data
        else:
            data = self.front.data
            self.front = self.front.next
            self.rear.next = self.front
            return data

    def display(self):
        if not self.front:
            print("Queue is empty")
        else:
            temp = self.front
            while True:
                print(temp.data, end=" ")
                temp = temp.next
                if temp == self.front:
                    break
            print()



cq = CircularQueue()

while True:
    print("\nCircular Queue Menu:")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        data = input("Enter the element to enqueue: ")
        cq.enqueue(data)
        print("Enqueued", data)
    elif choice == '2':
        data = cq.dequeue()
        if data is not None:
            print("Dequeued", data)
    elif choice == '3':
        cq.display()
    elif choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a valid option.")


