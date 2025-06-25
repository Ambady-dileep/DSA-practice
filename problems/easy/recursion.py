def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1) 
    
print(factorial(4))



def fibbonaci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibbonaci(n-1) + fibbonaci(n-2)
    
print(fibbonaci(7))



def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n //10 )
    
print(sum_of_digits(123))


def reverse_string(n):
    if len(n) == 0:
        return ""
    return reverse_string(n[1:]) + n[0]

print(reverse_string("hello"))


# def sum(n):
#     if n == 0:
#         return 0
#     else:
#         return n + sum(n-1)
# print(sum(5))
    