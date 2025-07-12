
# Merge two sorted arrays
# Hash table implementation
# Circular queue implementation important
# Double ended queue implementation
# Implement stack using LL
# implement stack
# implement queue



# 💪 TL;DR Summary
# Need	                 Use This Sort

# Fastest average case	⚡ Quick Sort
# Stable sort needed	🧊 Merge / Timsort
# Memory is tight	    💪 Heap / Quick
# Already sorted	    🧽 Insertion Sort
# Real-world use	    🔥 Timsort
# Linked list sorting	🧊 Merge Sodrt


# 📚 Detailed Use Cases of Each Sort

# 🔁 Bubble Sort
# ✔️ Use: Teaching, very small inputs
# ❌ Don’t use in production — very slow (O(n²))
# ✅ Stable, easy to write

# 🧽 Insertion Sort
# ✔️ Use: Small data, nearly sorted data
# ⚡ Very fast for almost-sorted arrays
# ✅ Stable, in-place

# 🥶 Selection Sort
# ✔️ Use: Only for very small, fixed-size lists
# ❌ Not stable, always O(n²)

# 🧊 Merge Sort
# ✔️ Use: Linked lists, stable sort needs, external sorting
# ✅ Consistent O(n log n), stable
# ❌ Needs O(n) space

# ⚡ Quick Sort
# ✔️ Use: Arrays, fast sorting, in-place
# ⚠️ Worst case O(n²), but usually fastest
# ❌ Not stable

# ✅ O(1) space (in-place)
# 💪 Heap Sort
# ✔️ Use: Limited memory environments (embedded, OS sorting)
# ❌ Not stable
# ✅ In-place (no extra memory), always O(n log n)

# 🔥 Timsort
# ✔️ Use: Real-world → Python’s sort(), Java’s Arrays.sort()
# ✅ Stable, hybrid of merge + insertion
# ⚡ Best performance in practice

# 🧠 Summary — When in Doubt:

# 🔒 Need stability? → Use Merge Sort or Timsort
# ⚡ Need speed and low memory? → Use Quick Sort
# 📦 Need minimal space? → Use Heap Sort
# 🎯 Know data is almost sorted? → Use Insertion Sort

# ⚡ Cheatsheet for Patterns

# Code Pattern	           Time	          Space
# Single loop	           O(n)           O(1)
# Nested loop	           O(n²)	      O(1)
# Sorting (Merge, Quick)  O(n log n)      O(n) / O(log n)
# Recursion (Fibonacci)	   O(2ⁿ)	      O(n) stack
# Hash map / dict build    O(n)	          O(n)
# Set operations	      O(1) avg	      O(n)