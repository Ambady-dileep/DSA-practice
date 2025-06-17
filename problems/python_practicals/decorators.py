# def decorator_function(original_function):
#     def wrapper():
#         print("Before the function runs")
#         original_function()
#         print("After the function runs")
#     return wrapper

# @decorator_function
# def say_hello():
#     print("Hello!")

# say_hello()

# def first_func(para1):
#     def second_func():
#         print("hello")
#         para1()
#         print("second hello")
#     return second_func

# @first_func
# def say_more():
#     print("okay wait for the second hello")

# say_more()