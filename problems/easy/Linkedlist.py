class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
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
    
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next 
        print("None")
    
    def insert_at_beginning(self, data):
        print(f"Creating new node with value {data}")
        new_node = Node(data)
        print(f"New node points to old head: {self.head.data if self.head else 'None'}")
        new_node.next = self.head
        self.head = new_node
        print(f"New head is now: {self.head.data}")
        
    def insert_at_index(self, index, data):
        if index == 0:
            self.insert_at_beginning(data)
            return
    
        new_node = Node(data)
        current = self.head
        count = 0
    
        while current is not None and count < index - 1:
            current = current.next
            count += 1
    
        if current is None:
            print("Index out of bounds")
            return
    
        new_node.next = current.next
        current.next = new_node


        

ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.insert_at_beginning(5)
ll.insert_at_beginning(1)
ll.insert_at_index(2, 99)
ll.print_list()
