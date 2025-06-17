# # 🧠 What is enumerate() in Python?
# # enumerate() is a built-in function that adds a counter (index) to any iterable (like list, tuple, string).

fruits = ['apple', 'banana', 'cherry']
for index,fruit in enumerate(fruits):
    print(index,fruit)

for i, name in enumerate(["Ram", "Shyam", "Geeta"], start=1):
    print(f"{i}. {name}")


a = ['apple', 'banana', 'cherry']
for i,j in enumerate( a ,start =1):
    print(f"{i}. {j}")

