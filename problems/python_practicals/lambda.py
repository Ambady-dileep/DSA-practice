# # ✅ Basic Level (Q1–Q10)

# # Q1. Create a lambda to add 10 to a number.
# a = lambda x : x + 10
# print(a(15))
# # Expected Output: 25 (if input is 15)

# # Q2. Lambda to square a number.
# a = lambda x : x**2
# print(a(7))
# # Expected Output: 49 (if input is 7)

# # Q3. Lambda to return the cube of a number.
# a = lambda x : x**3
# print(a(4))
# # Expected Output: 64 (if input is 4)

# # Q4. Lambda to multiply two numbers.
# a = lambda x,y : x*y
# print(a(6,8))
# # Expected Output: 48 (if inputs are 6, 8)

# # Q5. Lambda to find the max of two numbers.
# a = lambda x,y : max(x,y)
# print(a(3,9))
# # Expected Output: 9 (if inputs are 3 and 9)

# # 🔍 With map()

# # Q6. Use lambda + map to double each number in the list.
# lst = [1, 2, 3, 4]
# a = map(lambda x:x*2,lst)
# print(list(a))
# # Expected Output: [2, 4, 6, 8]

# # Q7. Use lambda + map to convert list of strings to uppercase.
# lst = ["hello", "python"]
# a = map(lambda x : x.upper(),lst)
# print(list(a))
# # Expected Output: ['HELLO', 'PYTHON']

# # Q8. Use lambda + map to square each number in list.
# lst = [2, 3, 4]
# a = map(lambda x : x **2, lst)
# print(list(a))
# # Expected Output: [4, 9, 16]

# # Q9. Use lambda + map to add 5 to each item in the list.
# lst = [10, 20, 30]
# a = map(lambda x:x*5,lst)
# print(list(a))
# # Expected Output: [15, 25, 35]

# # Q10. Use lambda + map to get lengths of each string.
# lst = ["a", "abcd", "xyz"]
# a = map(lambda x : len(x),lst)
# print(list(a))
# # Expected Output: [1, 4, 3]

# # ✅ With filter()

# # Q11. Use lambda + filter to keep only even numbers.
# lst = [1, 2, 3, 4, 5, 6]
# a = filter(lambda x : x%2==0,lst)
# print(list(a))
# # Expected Output: [2, 4, 6]

# # Q12. Use lambda + filter to keep strings longer than 3 chars.
# lst = ["a", "ab", "abcd", "hello"]
# a = filter(lambda x: len(x) > 3, lst)
# print(list(a))
# # Expected Output: ['abcd', 'hello']

# # Q13. Use lambda + filter to keep numbers > 10.
# lst = [5, 10, 15, 20]
# a = filter(lambda x : x > 10,lst)
# print(list(a))
# # Expected Output: [15, 20]

# # Q14. Use lambda + filter to remove empty strings.
# lst = ["python", "", "django", "", "AI"]
# a = filter(lambda x : x,lst)
# print(list(a))
# # Expected Output: ['python', 'django', 'AI']

# # Q15. Use lambda + filter to keep only negative numbers.
# lst = [-5, 3, 0, -2, 7]
# a = filter(lambda x:x<0,lst)
# print(list(a))
# # Expected Output: [-5, -2]

# 💡 With sorted() or reduce()

# # Q16. Sort list of tuples by second value using lambda.
# lst = [(1, 3), (2, 2), (3, 1)]
# a = sorted(lst,key=lambda x :x[1])
# print(list(a))
# # Expected Output: [(3, 1), (2, 2), (1, 3)]

# # Q17. Sort strings by length using lambda.
# lst = ["aaa", "b", "cccc"]
# a = sorted(lst,key = lambda x :len(x))
# print(list(a))
# # Expected Output: ['b', 'aaa', 'cccc']

# Q18. Find max in a list using reduce + lambda.
from functools import reduce
lst = [3, 9, 2, 7]
# Expected Output: 9

# Q19. Use lambda + sorted to sort dict by values.
d = {"a": 3, "b": 1, "c": 2}
# Expected Output: [('b', 1), ('c', 2), ('a', 3)]

# Q20. Combine map and lambda to convert Celsius to Fahrenheit.
celsius = [0, 25, 100]
# Expected Output: [32.0, 77.0, 212.0]
