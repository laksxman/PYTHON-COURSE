# Q1. Timing function Execution
#  Write a decorator that measures the time a function takes to execute.

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result
    
    return wrapper

@timer
def example_function(n):
    time.sleep(n)

example_function(2)

# Q2. Debugging function Calls
#  Create a decorator to print the function name and the values of its 
#  arguments every time the functin is called.

# def debug(func):
#     def wrapper(*args, **kwargs):
#         args_value = ', '.join(str(arg) for arg in args)
#         kwargs_value = ', '.join(f"{k}={v}"for k, v in kwargs.item())
#         print(f"calling: {func.__name__} with args {args_value}
#         and kwargs {kwargs_value}")
#         return func(*args, **kwargs)

#     return wrapper


# @debug
# def hello():
#     print("hello")

# @debug
# def greet(name, greeting ="Hello"):
#     print(f"{greeting},name")

# hello()
# greet("chai", greeting="hanji ")

# print(2**16)







def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Function '{func.__name__}' called with arguments: {args} and keyword arguments: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_function_call
def example_function(x, y, z=1):
    return x + y + z

# Example usage:
example_function(2, 3, z=4)



