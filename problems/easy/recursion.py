# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n-1) 
    
# print(factorial(4))



# def fibbonaci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     return fibbonaci(n-1) + fibbonaci(n-2)
    
# print(fibbonaci(7))



# def sum_of_digits(n):
#     if n == 0:
#         return 0
#     return n % 10 + sum_of_digits(n //10 )
    
# print(sum_of_digits(123))


# def reverse_string(n):
#     if len(n) == 0:
#         return ""
#     return reverse_string(n[1:]) + n[0]

# print(reverse_string("hello"))

#####################################################################################################################################

# def sum(n):
#     if n == 0:
#         return 0
#     else:
#         return n + sum(n-1)
# print(sum(5))

# def reversing(n):
#     if len(n)==0:
#         return ""
#     else:
#         return reversing(n[1:]+n[0])
# print(reversing("hello"))

# def is_palindrome(n):
#     if len(n)<=1:
#         return True
#     if n[0]!=n[-1]:
#         return False
#     return is_palindrome(n[1:-1])
# print(is_palindrome("medem"))

#best way to do palindrome finding
# def is_palindrome(s,left,right):
#     if left >= right:
#         return True
#     if s[left] != s[right]:
#         return False
#     return is_palindrome(s,left+1,right-1)

# word = "RaceCar".lower().replace(" ", "")  
# print(is_palindrome(word, 0, len(word) - 1))
