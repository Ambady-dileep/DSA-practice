# # ✅ Basic Modification

# lst = [1, 2, 3]
# lst.append(10)
# print(lst)
# # Expected Output: [1, 2, 3, 10]

# lst = [1, 2, 3]
# lst.extend([4,5])
# print(lst)
# # Expected Output: [1, 2, 3, 4, 5]

# lst = ["I", "Love"]
# lst.insert(1,"Python")
# print(lst)
# # Expected Output: ['I', 'Python', 'Love']

# lst = ["apple", "banana", "apple", "cherry"]
# lst.remove("apple")
# print(lst)
# # Expected Output: ['banana', 'apple', 'cherry']

# lst = [10, 20, 30]
# lst.pop()
# print(lst)
# # Expected Output: [10, 20]

# lst = ["a", "b", "c"]
# lst.pop(1)
# print(lst)
# # Expected Output: ['a', 'c']

# # 🧠 Summary:
# # Action	         Use This

# # Remove by index	pop(index)
# # Remove last item	pop()
# # Remove by value	remove(value)

# lst = [1, 2, 3]
# lst.clear()
# print(lst)
# # Expected Output: []

# # ✅ Search & Count

# lst = ["a", "b", "x", "d"]
# a = lst.index("x")
# print(a)
# # Expected Output: 2

# # Q9. Count how many times "a" occurs.
# lst = ["a", "b", "a", "c", "a"]
# a = lst.count("a")
# print(a)
# # Expected Output: 3

# lst = [5, 2, 9, 1]
# lst.sort()
# print(lst)
# # Expected Output: [1, 2, 5, 9]

# lst = [5, 2, 9, 1]
# lst.sort(reverse=True)
# print(lst)
# # Expected Output: [9, 5, 2, 1]

# lst = [1, 2, 3, 4]
# lst.reverse()
# print(lst)
# # Expected Output: [4, 3, 2, 1]

# lst = [10, 20, 30]
# lst_copy = lst.copy()
# a = lst.index(20)
# lst[a] = 99
# print("Original:", lst)
# print("Copy:", lst_copy)
# # Output:
# # Original: [10, 99, 30]
# # Copy: [10, 20, 30]

# # ✅ Combined Use Cases

# # Q14. Append 50, insert 40 at index 1, then remove 20.
# lst = [10, 20, 30]
# lst.append(50)
# lst.insert(1,40)
# print(lst)
# # Expected Output: [10, 40, 30, 50]

# # Q15. Extend list with [4, 5], then pop last and reverse.
# lst = [1, 2, 3]
# lst.extend([4,5])
# lst.reverse()
# print(lst)
# # Expected Output: [5, 4, 3, 2, 1]

# # Q16. Add items, sort them, and then count 3s.
# lst = [3, 1, 3, 2]
# lst.extend([6,8])
# lst.sort()
# a = lst.count(3)
# print(f"count of 3 is {a}")
# # Expected Output: count of 3 is 2

# # Q17. Clear a list, then append "Restart"
# lst = ["old", "data"]
# lst.clear()
# lst.append("Restart")
# print(lst)
# # Expected Output: ['Restart']

# # Q18. Insert "start" at beginning, "end" at end
# lst = ["middle"]
# lst.insert(0,"start")
# lst.append("end")
# print(lst)
# # Expected Output: ['start', 'middle', 'end']

# # Q19. Find index of "b" only after index 2
# lst = ["a", "b", "c", "b", "d"]
# a = lst.index("b",3)
# print(a)
# # Expected Output: 3

# # Q20. Create a list of 3 items, copy it, reverse original, sort copy
# lst = [3, 1, 2]
# lst.reverse()
# lst_2 = lst.copy()
# print(f"Original reversed: {lst}")
# print(f"Copy sorted: {lst_2}")
# # Expected Output:
# # Original reversed: [2, 1, 3]
# # Copy sorted: [1, 2, 3]

# ⚔️ 15 Medium Python List Method Practice Questions

# lst = [1, 2, 2, 3, 4, 3, 5]
# a = []
# for i in lst:
#     if i not in a:
#         a.append(i)
# print(a)
# # Expected Output: [1, 2, 3, 4, 5]

# lst = [1, 2, 3, 4, 5]
# a = [i*2 if i%2==0 else i for i in lst]
# print(a)
# # Expected Output: [1, 4, 3, 8, 5]
