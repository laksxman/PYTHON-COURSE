# Q1.  Given a list of numbers, count how many 
#      are positive.

# numbers = [1, -2, -3, -4, -5, -6, -7, 8, 9, 10]
# positive_number_count = 0

# for num in numbers:
#     if num > 0:
#         positive_number_count +=1
# print("Final count of Positive number is: ",
#        positive_number_count )


# Q2. SUM  OF EVEN NUMBERS
#     Calculate the sum of
#     even numbers up to a given number n. 

# n = 10
# sum_even = 0 

# for i in range(1, n+1):
#     if i%2 ==0:
#        sum_even +=1

# print("Sum of even number is: ", sum_even)


# Q3. Print the multiplication table for a given number
#     up to 10. but skip the fifth iteration. 

# number = 3

# for i in range(1, 11):
#     if i ==5:
#         continue
#     print( number, 'x', '=', number*i)


# Q4. Reverse a string using a loop.
#     find the first Non-Repeated Character

# input_str = "Python"
# reversed_str = ""

# for char in input_str:
#     reversed_str =  char + reversed_str 
# print(reversed_str)


# Q5. find the first Non-Repeated Character
#     Given a string. find the first non-repeated character.

# input_str = "teeter"

# for char in input_str:
#     print(char)
#     if input_str.count(char) == 1:
#         print("Char is: ", char)
#         break


# Q6. Factorial Calculator
#     Compute the factorial of a number using a while
#     loop.

# number  =  5
# factorial = 1

# while number > 0:
#     # factorial = factorial * number
#     # number = number - 1
#     factorial *= number
#     number -= 1

# print("Factorial: ", factorial)


# Q7. Validate Input 
#     Keep asking the user for input untill they enter
#     a number between 1 and 10.

# while True:
#     number = int(input("Enter value b/w 1 and 10: "))
#     if 1 <= number <= 10:
#         print("Thanks")
#         break
#     else:
#         print("Invalid number, try again")

# Q8. Prime Number Checker
#     Check if a number is prime.

# number = 20

# is_prime = True

# if number > 1:
#     for i in range(2, number):
#         if (number% i) == 0:
#             is_prime = False
#             break
# print(is_prime)


# Q9. List Uniqueness Checker 
#     Check if all elements in a list are unique.
#     If a duplicate is found, exit the loop and 
#      print the duplicate.

items = ["apple", "banana", "orange", "apple", "mango"]

unique_item = set()

for item in items:
    if item in unique_item:
        print("Duplicate: ", item)
        break
unique_item.add(item)


# Q10. Exponential Backoff
#  Implement an exponential backoff strategy that
#  doubles the wiat time betweem retires, starting
#  from 1 second, but stops after 5 retries.

import time

wait_time = 1
max_retries = 5
attempts = 0

while attempts < max_retries:
    print("Attempt", attempts + 1, "- wait time",
          wait_time, )
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1




