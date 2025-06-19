class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
        
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head

    def print_list(self):
        if self.head is None:
            print("Empty list")
            return

        current = self.head
        while True:
            print(current.data, end="<-->")
            current = current.next
            if current == self.head:
                break
        print("(head)")

    def add_to_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        # Find the last node
        current = self.head
        while current.next != self.head:
            current = current.next

        # Rearrange pointers
        new_node.next = self.head
        current.next = new_node
        self.head = new_node

    def delete_at_beginning(self):
        if self.head is None:
            print("List is empty!")
            return

        if self.head.next == self.head:
            # Only one node
            self.head = None
            return

        # Find the last node
        current = self.head
        while current.next != self.head:
            current = current.next

        # Point last node to the new head
        current.next = self.head.next
        self.head = self.head.next


cll = CircularLinkedList()
cll.append(10)
cll.append(20)
cll.append(30)
cll.add_to_beginning(5)
cll.print_list()
cll.delete_at_beginning()
cll.print_list()


