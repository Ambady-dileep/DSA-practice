######################################################################## Single inheritance in Python 

# Single inheritance is when a child class (subclass) inherits from one parent class (superclass). That means the child gets access to the methods and properties of the parent.
# It’s like one child learning habits from one parent.

# # parent class
# class Animal:
#     def sound(self):
#         print("Animal makes a sound")

# # Child class
# class Dog(Animal):
#     def bark(self):
#         print("Dog barks")

# obj = Dog()
# obj.sound()
# obj.bark()

####################################################################### Multiple inheritance in Python 

# when one child class inherits from more than one parent class. So the child gets features (methods/attributes) from multiple sources.
# class A:
#     def method_a(self):
#         print("Method from A")

# class B:
#     def method_b(self):
#         print("Method from B")

# class C(A,B):
#     def method_c(self):
#         print("Method from C")

# obj = C()
# obj.method_a()
# obj.method_b()
# obj.method_c()

###################################################################### Multilevel inheritance in Python 

# 🧨🧨Multilevel inheritance means a class inherits from a class which already inherited from another class.
# So the chain looks like: Grandparent → Parent → Child
# The Child class indirectly inherits from Grandparent.

# class A:
#     def method_a(self):
#         print("Method from A")

# class B(A):
#     def method_b(self):
#         print("Method from B")

# class C(B):
#     def method_c(self):
#         print("Method from C")

# obj = C()
# obj.method_a()
# obj.method_b()
# obj.method_c()

###################################################################### What is Encapsulation in Python 

# Encapsulation is the concept of hiding internal details of an object and restricting access to them — controlling how data is accessed and modified.
# It’s the idea of data protection + access control.

# Access Levels in Python:

#      Type	         Syntax	                Access Scope

# ✅ Public	      self.name	     Accessible from anywhere
# ⚠️ Protected	   _name	      Accessible inside class & subclasses
# 🔒 Private	   __name	      Not directly accessible (name mangling)

# class Student:
#     def __init__(self, name, grade):
#         self.name = name          # public
#         self._grade = grade       # protected
#         self.__score = 95         # private

#     def get_score(self):          # getter
#         return self.__score

#     def set_score(self, value):   # setter
#         if 0 <= value <= 100:
#             self.__score = value
#         else:
#             print("Invalid score")

# # Creating object
# s = Student("Ambady", "A")

# print(s.name)         # ✅ Accessible
# print(s._grade)       # ⚠️ Accessible (but not recommended)
# # print(s.__score)    # ❌ Error: private
# print(s.get_score())  # ✅ Accessing private using getter
# s.set_score(89)       # ✅ Updating private using setter
# print(s.get_score())  # ✅ 89
