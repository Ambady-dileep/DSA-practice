# Count characters in a string without using len()
def func():
    current_input = input("Enter the input to find its length:")
    new_words = current_input.replace(" ","")
    count = 0
    for i in new_words:
        count+=1
    return count
    
print(func())

# Truncate a string if it’s longer than 10 characters.
def func():
    value = input("Enter the data: ").replace(" ", "")
    if len(value) <= 10:
        return f"Your input matches our criteria: {value}"
    return f"Only 10 characters are allowed: {value[:10]}"

print(func())


# Slice a string in the middle using its length.
def func():
    value = input("Enter the value:").strip()
    if value == "":
        return "The string is empty. No halves to slice."
    if len(value) == 1:
        return f"Only one character: '{value}' (no way to slice into halves)"
    mid = len(value)//2
    first_half = value[:mid]
    second_half = value[mid:]
    return f"{first_half} and {second_half}"
    
print(func())