# 💣 Remember this line:
# "Big O notation is the language. Time complexity is the message."
# When you say O(n log n), you're using Big O to describe the time complexity.


import time      # With this you get a feel for how time grows (or doesn’t grow) with bigger input — it’s how you feel Big O in real life.

def get_first_element(arr):
    return arr[0]


my_list = [10, 20, 30, 40]
print(get_first_element(my_list))

# arr[0] grabs the first item in the list.
# Lists in Python are indexed — arr[0] is direct access.
# No loops. No searching. No calculations.
# That’s constant time — O(1).This is the best time complexity you can get. Because O(1) is the fastest time complexity.

#<<-------------------------------------------------------->>

import time

def get_first_element(arr):
    return arr[0]

# Let's test it on bigger and bigger lists
for size in [10, 100, 1000, 10000, 1000000]:
    test_list = list(range(size))   # creates a list [0, 1, 2, ..., size-1]

    start_time = time.time()        # record time before running the function
    get_first_element(test_list)    # run your function
    end_time = time.time()          # record time after function runs

    elapsed = end_time - start_time # calculate how many seconds passed
    print(f"Size: {size}, Time taken: {elapsed:.10f} seconds")

#<<-------------------------------------------------------->>

def sum_list(arr):
    total = 0 
    for i in arr:
        total += i
    return total

a = [1, 2, 3, 4, 5]
print(sum_list(a))

# One loop through n elements → O(n)
# Doesn’t matter what you do inside the loop (unless it's another loop or recursion)
# ✅ This is O(n)
# Core Reason
# You're looping through every single element in the list once.
#<<-------------------------------------------------------->>

import time
# Task 2: Return the sum of all elements (O(n))
def sum_list(arr):
    total = 0
    for i in arr:
        total += i
    return total

for size in [10, 100, 1000, 10000, 1000000]:
    test_list = list(range(size))
    
    start_time = time.time()
    sum_list(test_list)
    end_time = time.time()
    
    elapsed = end_time - start_time
    print(f"Size: {size}, Time taken: {elapsed:.8f} seconds")

#📌 Lesson: O(n) means work grows linearly with input size.

#<<-------------------------------------------------------->>

# Task 3: Find the largest number (O(n))
def max_in_list(arr):
    max_num = arr[0]
    for num in arr:
        if num > max_num:
            max_num = num
    return max_num

arr = [10, 1000, 100000]
print(max_in_list(arr))

# Big O: O(n) — because it checks every number once.

import time

def max_in_list(arr):
    max_num = arr[0]
    for num in arr:
        if num > max_num:
            max_num = num
    return max_num

for size in [10, 1000, 1000000]:
    test_list = list(range(size))  # Worst case: max is at the end
    start = time.time()
    max_in_list(test_list)
    end = time.time()
    print(f"Size: {size}, Time: {end - start:.8f} seconds")

#<<-------------------------------------------------------->>
# Task 4: Check if a number exists in the list (O(n))
def contain_element(arr,target):
    for num in arr:
        if num == target:
            return True
        return False
target = 10
arr = [10, 1000, 10000, 1000000]
print(contain_element(arr,target))

# arr = [1, 2, 3, 4, ..., 999999]
# target = 999999
# You’d have to check EVERY number before you find it. That's n checks.
# Or worse:
# python
# target = 1000000  # not in the list
# Now you check every number and still return False at the end.
# 📌 Worst case = check all n elements.

# That's why it's O(n).

#<<-------------------------------------------------------->>

def reverse_in_place(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr

arr = [10, 20, 30, 40]
print(reverse_in_place(arr))  # Output: [40, 30, 20, 10]


#<<-------------------------------------------------------->>

#Count even numbers in a list

def find_even(arr):
    count = 0 
    for i in arr:
        if i % 2 ==0:
            count+=1
    return count
        
arr = [10, 20, 30, 40]

print(find_even(arr))

#<<-------------------------------------------------------->>

# Check if a list is sorted in ascending order

def is_sorted_ascending(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
        return True

arr = [10, 20, 30, 40]

print(is_sorted_ascending(arr))