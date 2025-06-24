# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#         self.prev = None
        
# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None
        
#     def append(self,data):
#         new_node = Node(data)
        
#         if self.head is None:
#             self.head = new_node
#             return
        
#         current = self.head
#         while current.next:
#             current = current.next
#         current.next = new_node
#         new_node.prev = current
        
#     def print_forward(self):
#         current = self.head
#         while current:
#             print(current.data, end=" <--> ")
#             current = current.next
#         print("None")
            
#     def print_backward(self):
#         if self.head is None:
#             print("No Linkedlist exists")
#             return
        
#         current = self.head
#         while current.next:
#             current = current.next
        
#         while current:
#             print(current.data, end = "<-->")
#             current = current.prev
#         print("None")
        
#     def add_to_beginning(self, data):
#         new_node = Node(data)
#         new_node.next = self.head
        
#         if self.head is not None:
#             self.head.prev = new_node
            
#         self.head = new_node
        
#     def delete_at_beginning(self):
#         if self.head is None:
#             print("No Linkedlist exist's")
#             return
#         if self.head.next is None:
#             self.head = None
#         else:
#             self.head = self.head.next
#             self.head.prev = None
        
#     def delete_at_end(self):
#         if self.head is None:
#             print("No Linkedlist found!")
#             return
#         if self.head.next is None:
#             self.head = None
#             return
        
#         current = self.head
#         while current.next:
#             current = current.next
        
#         current.prev.next = None    
        
#     def insert_at_position(self,pos,data):
#         new_node = Node(data)
#         if pos == 0:
#             self.add_to_beginning(data)
#             return
        
#         current = self.head
#         count = 0
        
#         while current and count > pos -1:
#             current = current.next
#             count+=1
        
#         if current is None:
#             print("Position out of bound!!")
#             return
        
#         new_node.next = current.next
#         new_node.prev = current
        
#         if current.next:
#             current.next.prev = new_node
            
#         current.next = new_node
        
#     def delete_at_position(self,pos):
#         if self.head is None:
#             print("No LinkedList exists!")
#             return
        
#         if pos == 0:
#             self.delete_at_beginning()
#             return
        
#         current = self.head
#         count = 0
        
#         while current and count < pos:
#             current = current.next
#             count+=1
            
#         if current is None:
#             print("Position out of bounds!")
#             return
        
#         if current.prev:
#             current.prev.next = current.next
            
#         if current.next:
#             current.next.prev = current.prev
        
        
        
# dll = DoublyLinkedList()
# dll.append(20)
# dll.append(30)
# dll.append(40)
# dll.print_forward()
# dll.add_to_beginning(10)
# dll.print_forward()
# dll.print_backward()
# dll.print_forward()
# dll.delete_at_beginning()
# dll.print_forward()
# dll.delete_at_end()
# dll.print_forward()
# dll.insert_at_position(2, 25)
# dll.print_forward()



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
        
    def print_backward(self):
        current = self.head
        if current is None:
            print("None (empty list)")
            return
        
        while current.next:
            current = current.next
            
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")
        
    def print_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

        
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)
dll.print_forward()
dll.print_backward()


# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#         self.prev = None
        
    
# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None
        
#     def append(self,data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return
        
#         current = self.head
#         while current.next:
#             current = current.next
#         current.next = new_node
#         new_node.prev = current
        
#     def print_forward(self):
#         if self.head is None:
#             print("No LinkedList exists!")
#             return
#         current = self.head
#         while current:
#             print(current.data,end ="<-->")
#             current = current.next
#         print("None")
        
#     def print_backward(self):
#         if self.head is None:
#             print("No LinkedList exists!")
#             return
#         current = self.head
#         while current.next:
#             current = current.next
            
#         while current:
#             print(current.data,end ="<-->")
#             current = current.prev
#         print("None")
        
#     def delete_by_value(self,value):
#         if self.head is None:
#             print("No LinkedList exists!")
#             return
        
#         current = self.head
#         if current.data == value:
#             self.head = current.next
#             if self.head:
#                 self.head.prev = None
#             return
        
#         while current and current.data != value:
#             current = current.next
            
#         if current is None:
#             print("No value found!")
#             return
           
#         if current.next:
#             current.next.prev = current.prev 
#         if current.prev:
#             current.prev.next = current.next
        
        
#     def delete_by_position(self,pos):
#         if self.head is None:
#             print("No LinkedList exists!")
#             return
        
#         if pos == 0:
#             self.head = self.head.next
#             if self.head:
#                 self.head.prev = None
#             return
        
#         current = self.head
#         count = 0
        
#         while current and count < pos:
#             current = current.next
#             count+=1
        
#         if current is None:
#             print("Out of bound!")
#             return
        
#         if current.prev:
#             current.prev.next = current.next
            
#         if current.next:
#             current.next.prev = current.prev

#     def search(self, value):
#         current = self.head
#         index = 0
#         while current:
#             if current.data == value:
#                 return index
#             current = current.next
#             index+=1
#         return index

#     def insert_at_position(self,data,pos):
#         new_node = Node(data)
#         if self.head is None:
#             print("No linkedlist exists!")
#             return
        
#         if pos == 0:
#             new_node.next = self.head
#             if self.head:
#                 self.head.prev = new_node
#             self.head = new_node
#             return -1
        
#         current = self.head
#         count = 0
          
#         while current and count < pos -1:
#             current = current.next
#             count+=1
            
#         if current is None:
#             print("postion out of bounds")
#             return
        
#         new_node.next = current.next
#         new_node.prev = current
        
#         if current.next:
#             current.next.prev = new_node
#         current.next = new_node
        
#     def delete_at_end(self):
#         if self.head is None:
#             print("No Linkedlist found!")
#             return
#         if self.head.next is None:
#             self.head = None
#             return
        
#         current = self.head
#         while current.next:
#             current = current.next
        
#         current.prev.next = None  
        
#     def delete_at_beginning(self):
#         if self.head is None:
#             print("No Linkedlist exist's")
#             return
#         if self.head.next is None:
#             self.head = None
#         else:
#             self.head = self.head.next
#             self.head.prev = None
            
#     def add_to_beginning(self, data):
#         new_node = Node(data)
#         new_node.next = self.head
        
#         if self.head is not None:
#             self.head.prev = new_node
            
#         self.head = new_node    
        
        
# dll = DoublyLinkedList() 
# dll.append(10)
# dll.append(20)
# dll.append(30)
# dll.append(40)
# dll.append(50)
# dll.print_forward()
# dll.print_backward()
# dll.delete_by_value(10)
# dll.print_forward()
# dll.delete_by_position(2)
# dll.print_forward()
# print(dll.search(40))
# dll.print_forward()
# dll.insert_at_position(3,1)
# dll.print_forward()
# dll.print_backward()


