class OpenAddressingHashMap:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        for i in range(self.size):
            new_index = (index + i) % self.size
            slot = self.table[new_index]

            # Insert if empty or update if same key
            if slot is None or slot[0] == key:
                self.table[new_index] = (key, value)
                return
        print("HashMap is full! Cannot insert:", key)


    def insert(self,key,value):
        index = self._hash(key)
        for i in range(self.size):
            new_index = (index+i)%self.size
            slot = self.table[index]
            if self.slot is None or slot[0]==key:
                self.table[new_index]=(key,value)
                return 
        print("Hashmap is empty")

    def get(self, key):
        index = self._hash(key)
        for i in range(self.size):
            new_index = (index + i) % self.size
            slot = self.table[new_index]

            if slot is None:
                return None  # Key not found
            if slot[0] == key:
                return slot[1]
        return None

    def delete(self, key):
        index = self._hash(key)
        for i in range(self.size):
            new_index = (index + i) % self.size
            slot = self.table[new_index]

            if slot is None:
                return False  # Key not found
            if slot[0] == key:
                self.table[new_index] = None
                return True
        return False

    def __str__(self):
        result = ""
        for i, item in enumerate(self.table):
            result += f"{i}: {item}\n"
        return result


h = OpenAddressingHashMap(5)

h.insert("apple", 10)
h.insert("banana", 20)
h.insert("grape", 30)
h.insert("orange", 40)

print("apple =", h.get("apple"))
print("banana =", h.get("banana"))

h.delete("banana")
print("After deleting banana:")
print(h)

h.insert("melon", 50)
h.insert("kiwi", 60)  # Should say hashmap is full

print("Final State:")
print(h)
