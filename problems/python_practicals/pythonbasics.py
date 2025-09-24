students = [
    {"name": "Arya", "marks": 92},
    {"name": "Ravi", "marks": 85},
    {"name": "Meena", "marks": 95},
    {"name": "John", "marks": 67}
]

def above_90(students):
    result = []
    for student in students:
        if student["marks"]>90:
            result.append(student["name"])
    return result
        
print(above_90(students))
    
logs = [
    ("Ravi", "Delhi"),
    ("Arya", "Mumbai"),
    ("Ravi", "Delhi"),
    ("Meena", "Kolkata"),
    ("Meena", "Mumbai")
]

def avoid_duplicates(logs):
    seen = set()
    for cities in logs:
        if cities[1] not in seen:
            seen.add(cities[1])
    return seen
    
print(avoid_duplicates(logs))
 
 
def students_enrolled(course,students):
    is_enrolled = []
    for name,subjects in students.items():
        if course in subjects:
            is_enrolled.append(name)
    return is_enrolled
        
students = {
    "Shahan": ["Maths", "English", "Hindi"],
    "Arya": ["Science", "Malayalam", "English"],
    "Ravi": ["Social", "Hindi", "Biology"]
}
items_sold = ['pen', 'book', 'pen', 'notebook', 'book', 'pen']

def most_frequent(items_sold):
    freq = {}
    for item in items_sold:
        if item in freq:
            freq[item]+=1 
        else:
            freq[item]=1
    return max(freq,key=freq.get)
    
print(most_frequent(items_sold))

numbers = [5, 3, 1, 5, 2, 3, 4]
def remove_duplicates_and_sort(numbers):
    seen = set()
    for number in numbers:
        seen.add(number)
    return tuple(sorted(seen))

print(remove_duplicates_and_sort(numbers))

fruit_prices = {"apple": 100, "banana": 50, "mango": 50, "guava": 30}

def fruits_price_finder(fruit_prices):
    result = []
    for key,value in fruit_prices.items():
        if value == 50:
            result.append(key)
    return f'The fruits are: {",".join(result)}'

print(fruits_price_finder(fruit_prices))

a = [1, 2, 3, 4, 5, 2]
b = [4, 5, 6, 7, 4]
c = set(a) & set(b)
print(list(c))

stock = {"pen": 10, "book": 5}
changes = [("pen", -3), ("book", 2), ("notebook", 4)]
def updating(stock,changes):
    for item,change in changes:
        if item in stock:      
            stock[item]+=change
        else:
            stock[item]=change
    return stock
print(updating(stock,changes))

