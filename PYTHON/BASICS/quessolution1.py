# Question no. 1

# age = 20

# if age < 13:
#     print("child")
# elif age < 20:
#     print("teenager")
# elif age < 60:
#     print("Adult")
# else:
#     print("Senior")


# Question no. 2

# age = 23
# day = "wednesday"

# price = 12 if age >=18 else 8

# if day == "wednesday":
#     price = price-2
#     # price -=2

# print("Ticket  price for you is $",price)


# Question no.  -> Assign a letter grade on a student's score: A(90-100)
# ,B(80-89), C(70-79), D(60-69),F(below 60)

# score = 96

# if score >= 101:
#     print("Please verify your grade again")
#     exit()

# if score >= 90:
#     grade = 'A'
# elif score >= 80:
#     grade = 'B'
# elif score >=70:
#     grade = "C"
# elif score >=60:
#     grade = "D"
# else:
#     grade = 'F'

# print("Grade : ", grade)
# exit()

# # Q4. Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green-Unripe, Yellow- Ripe, Brown- Overripe)

# fruit = "Banana"
# color = "Yellow"

# if fruit == "Banana":
#     if color == "Green":
#         print("Unripe")
#     elif color == "Yellow":
#         print("Ripe")
#     elif color == "Brown":
#         print("OverRipe")
# else:
#     print("Nothing")


# Q5. Suggest an activity based on the weather(e.g., Sunny - Go for a walk, Rainy-Read a book, Snowy - Build a snowman).

# weather = "Sunny"

# if weather == "Sunny":
#     activity = "Go for a walk"
# elif weather == "Rainy":
#     activity = "Read a book"
# elif weather == "Snowy":
#     activity = "Build a snoman"
# print(activity)


# Q6. Choose a mode of transportation based on the distance(e.g., <3 km, 3-15 km: Bike,>15km:Car)

# distance = 52

# if distance<3:
#     transport = "walk"
# elif distance <= 15:
#     transport = "Bike"
# else:
#     transport = "Car"

# print("AI recommends you the transport of: ", transport)


# Q7. Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

# order_size = "Medium"
# extra_shot = True

# if extra_shot:
#     coffee = order_size + " coffee with an extra shot"
# else:
#     coffee = order_size + " coffee"
# print("Order: ", coffee)

# Q8. Check if a password is "Weak", "Medium", or "Strong". Criterua: 6 chars(weak), 6-10 chars (Medium),> 10 chars(Strong)

# password = "Se33cure123P"

# if len(password)< 6:
#     strenth = "weak"
# elif len(password) <=10:
#     strenth = "Medium"
# else:
#     strenth = "Strong"

# print("Password strength is: ", strenth)




# Q9.
year = 4000

if (year % 400 == 0)  or (year % 4 == 0 and year % 100 != 0):
    print(year, " is  a leap year")
else:
    print(year, "is NOT a leap year")