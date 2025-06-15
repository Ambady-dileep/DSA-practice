# 🔰 Basic Level (Q1–Q5)

# Q1. Get the first 3 elements
lst = [10, 20, 30, 40, 50]
a = lst[:3]
print(a)
# Expected Output: [10, 20, 30]

# # Q2. Get the last 2 elements
# lst = [1, 2, 3, 4, 5]
# a = lst[3:]
# # a = lst[-2:]
# print(a)
# # Expected Output: [4, 5]

# # Q3. Get everything except the first and last
# lst = [11, 22, 33, 44, 55]
# a = lst[1:4]
# print(a)
# # Expected Output: [22, 33, 44]

# # Q4. Reverse the list using slicing
# lst = [1, 2, 3, 4]
# a = lst[::-1]
# print(a)
# # Expected Output: [4, 3, 2, 1]

# # Q5. Get every second element
# lst = [10, 20, 30, 40, 50]
# a = lst[0:5:2]
# print(a)
# # Expected Output: [10, 30, 50]

# ⚙️ Moderate Level (Q6–Q10)

# Q6. Get last 3 elements using negative indexing
lst = [1, 2, 3, 4, 5, 6]
# Expected Output: [4, 5, 6]

# Q7. Get all elements except last 2
lst = [5, 6, 7, 8, 9]
# Expected Output: [5, 6, 7]

# Q8. Slice from index 1 to 4 with step 2
lst = [100, 200, 300, 400, 500]
# Expected Output: [200, 400]

# Q9. Reverse every 2 elements (pair-wise reverse)
lst = [10, 20, 30, 40, 50, 60]
# Expected Output: [20, 10, 40, 30, 60, 50]

# Q10. Extract middle third of a list
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Output: [4, 5, 6]

# 🧠 Intermediate Level (Q11–Q15)

# Q11. Replace first 3 elements with [99, 88, 77] using slicing
lst = [1, 2, 3, 4, 5]

# Expected Output: [99, 88, 77, 4, 5]

# Q12. Delete last 3 elements using slicing
lst = [10, 20, 30, 40, 50, 60]

# Expected Output: [10, 20, 30]

# Q13. Extract all elements at odd positions (index-wise)
lst = ['a', 'b', 'c', 'd', 'e']

# Expected Output: ['b', 'd']

# Q14. Use slicing to clear a list (without using clear())
lst = [1, 2, 3, 4]
lst[:] = []

# Expected Output: []

# Q15. Create a copy of the list using slicing
lst = [5, 10, 15]
copy = lst[:]
# Expected Output: [5, 10, 15]