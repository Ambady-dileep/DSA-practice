class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class StackLL:
    def __init__(self):
        self.top = None 
        
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        
    def is_empty(self):
        return self.top is None
        
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        value = self.top.data
        self.top = self.top.next
        return value
        
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.top.data
    
    def print(self):
        temp = self.top
        while temp:
            print(temp.data,end="->")
            temp = temp.next
        print(None)
    

def reverse_str(s):
    stack = StackLL()
    for ch in s:
        stack.push(ch)
        
    reverse_string=""
    while not stack.is_empty():
        reverse_string+=stack.pop()
    return reverse_string


sll = StackLL();
sll.push(1)
sll.push(2)
sll.push(3)
sll.push(4)
sll.print()
print(sll.pop())
print(sll.peek())
sll.print()
print(reverse_str("hello"))
    