class Node:
    def __init__(self,data):
        self.data=data
        self.next = None
        self.prev = None
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self,data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail

            self.tail = new_node

    def display_forward(self):
        current = self.head
        
        while current:
            print(current.data,end="<->")
            current = current.next
        print("None")
    
    def display_backward(self):
        current = self.tail

        while current:
            print(current.data,end="<->")
            current = current.prev
        print("None")

dll = DoublyLinkedList()

dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.append(5)

dll.display_forward()
dll.display_backward()

