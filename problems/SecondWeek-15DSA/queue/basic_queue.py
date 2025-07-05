# ✅ What is a Queue?
# A Queue is a linear data structure that follows the FIFO rule:
# First In, First Out

# 🔁 Meaning:
# The first element added to the queue is the first one to be removed.
# Think of a line at a movie theatre: the person who comes first gets served first.
# A Queue is like a line — whoever gets in first, gets out first.

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, value):
        self.items.append(value)  # Add at rear

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)  # Remove from front
        return None

    def peek_front(self):
        if not self.is_empty():
            return self.items[0]
        return None

    def peek_rear(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def display(self):
        return self.items


q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print("Front:", q.peek_front())  # ➜ 10
print("Rear:", q.peek_rear())    # ➜ 30

q.dequeue()

print("Queue now:", q.display()) # ➜ [20, 30]



# For learning purpose refer below
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, value):
        self.items.append(value)  # Add at rear
        print(f"{value} added at rear")

    def dequeue(self):
        if not self.is_empty():
            removed = self.items.pop(0)  # Remove from front
            print(f"{removed} removed from front")
            return removed
        else:
            print("Queue is empty")
            return None

    def peek_front(self):
        if not self.is_empty():
            return self.items[0]
        return None

    def peek_rear(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def display(self):
        print("Queue:", self.items)

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()

print("Front:", q.peek_front())  # ➜ 10
print("Rear:", q.peek_rear())    # ➜ 30

q.dequeue()
q.display()
