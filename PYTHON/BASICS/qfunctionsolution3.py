# Q1. Basic Function syntax
# Write a function to calculate and return the square
# of a number.

def square(number):
#    print(number ** 2) 
    return number ** 2

result = square(4)
print(result)

# Q2. Function with multiple Parameters
# Create a function that takes two numbers as 
# parameters and returns thier sum.

def add(numOne, numTwo):
    return numOne + numTwo
print(add(5,5))


# Q3. Polymorphism in Functions 
# Write a function multiply that multiplies two numbers,
# but can also accept and multilpy strings.

def multiply(p1, p2):
    return p1 * p2

print(multiply(8, 5))
print(multiply('a', 5))
print(multiply(5, 'a'))

# Q4. Function returning multiple values
#  Create a function that returns both the area and 
#  circumference of a circle given its radius.
import math

def circle_stats(radius):
   
   area = math.pi * radius ** 2
   circumference = 2 * math.pi * radius
   return area, circumference
a, c = circle_stats(12)
print("Area: ", a, "Circumference: ", c)

# Q5. Default parameter Value
# write a function that greets a auser. If no name is 
# provided, it should greet with a default name.


def greet(name = "User"):
    return "Hello, " + name + " !"
print(greet("chai"))
print(greet())

# Q6. Lambda function
# Create a lambda function to compute the cube of a number.

# first method
cube = lambda x: x ** 3
print(cube(3))

# second method
def cube(num):
    return num ** 3
print(cube(3))

# Q7. Function with *args 
# Write a function that takes variable numberof arguments and returns heir sum.

def summ_all(*args):
    print(args)
    for i in args:
        print(i*2)
    return sum(args)

print(summ_all(1,2,3))
# print(summ_all(1,2,3,4,5))
# print(summ_all(1,2,3,4,5,6,7,8))

# Q8. Function with **kwargs
# Create a function that accepts any number of keyword arguments and prints them in the formats key value.

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="shaktiman", power="lazer")
print_kwargs(name="shaktiman")
print_kwargs(name="shaktiman", power="lazer", enemy = "Dr. jackaal")

# Q9. Generator Function with yeild
#  write a generator function that yields even numbers up to a specified limit.

def even_generator(limit):
    # li = []
    for i in  range(2, limit +1, 2):
        yield i
        # li.append(i)

        # print(i)
    # return li

# print(even_generator(10))
for num in even_generator(10):
    print(num)

# Q10. recursive Function
#  Create a recursive function to calculate the factorial of a number.
def factorial(n):
    if n == 0 :
        return 1
    else:
        return n*factorial(n-1)









