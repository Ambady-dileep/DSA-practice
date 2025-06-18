class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        
    def append(self,data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current
        
    def print_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <--> ")
            current = current.next
        print("None")
            
    def print_backward(self):
        if self.head is None:
            print("No Linkedlist exists")
            return
        
        current = self.head
        while current.next:
            current = current.next
        
        while current:
            print(current.data, end = "<-->")
            current = current.prev
        print("None")
        
    def add_to_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        
        if self.head is not None:
            self.head.prev = new_node
            
        self.head = new_node

    def delete_at_beginning(self):
        if self.head is None:
            print("No Linked List exists!")
            return
        if self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None

 
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.add_to_beginning(10)
dll.print_forward()
dll.delete_at_beginning()
dll.print_forward()
dll.print_backward()
