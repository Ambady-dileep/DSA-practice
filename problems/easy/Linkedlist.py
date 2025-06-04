class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList():
    def __init__(self):
        self.head = None
    
    def append(self, data):
        print(f"Appending {data}")
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            print("List was empty. Set as head.")
            return 
        
        current = self.head 
        while current.next:
            current = current.next
        current.next = new_node
        print(f"Appended {data} to the end.")

    def print(self):
        print("Linked List:")
        current = self.head
        index = 0
        while current:
            print(f"[{index}] {current.data} --> ", end="")
            current = current.next
            index += 1
        print("None\n")
        
    def reverse(self):
        print("Reversing the linked list...")
        prev = None
        current = self.head
        step = 0
        while current:
            next_node = current.next
            current.next = prev
            print(f" Step {step}: Reversing {current.data}")
            prev = current
            current = next_node
            step += 1
        self.head = prev
        print("Reversal complete.\n")
    
    def insert_at_position(self, pos, data):
        print(f"Inserting {data} at position {pos}")
        new_node = Node(data)
        
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            print("Inserted at the beginning.")
            return
        
        current = self.head
        count = 0
        
        while current is not None and count < pos - 1:
            current = current.next
            count += 1
        
        if current is None:
            print("Index out of bounds.\n")
            return
        
        new_node.next = current.next
        current.next = new_node
        print(f"Inserted {data} after position {count}\n")
    
    def insert_at_beginning(self, data):
        print(f"Inserting {data} at the beginning")
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print("Inserted at head.\n")

    def delete_at_position(self, pos):
        print(f"Deleting node at position {pos}")
        if self.head is None:
            print("List is empty.\n")
            return
    
        if pos == 0:
            deleted_value = self.head.data
            self.head = self.head.next
            print(f"Deleted head node with value {deleted_value}\n")
            return
    
        current = self.head
        count = 0

        while current and count < pos - 1:
            current = current.next
            count += 1

        if current is None or current.next is None:
            print("Position out of bounds.\n")
            return

        deleted_value = current.next.data
        current.next = current.next.next
        print(f"Deleted node with value {deleted_value} at position {pos}\n")

ll = LinkedList()

ll.append(10)
ll.append(20)
ll.append(30)
ll.print()

ll.reverse()
ll.print()

ll.insert_at_position(1, 15)
ll.insert_at_position(0, 5)     
ll.insert_at_position(10, 99)  
ll.print()

ll.delete_at_position(2)
ll.print()

ll.insert_at_beginning(1)
ll.print()
