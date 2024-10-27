# tea_varities = ["Black", "Green", "Olong", "White"]
# print(tea_varities)

# print(tea_varities[-1])
# print(tea_varities[:2])

# print(tea_varities[2:])

# print(tea_varities[3])

# tea_varities[3] = "Herbal"

# print(tea_varities)

# print(tea_varities[1:2])

# print(tea_varities)
# print(tea_varities[1:2])

# tea_varities[1:2] = ["Lemon"]
# print(tea_varities)


# tea_varities[1:3] = ["green" , "Masala"]
# print(tea_varities)


# print(tea_varities[1:1])
# tea_varities[1:1] = ["test" , "test"]
# print(tea_varities)

# print(tea_varities[1:3])
# print(tea_varities[1:2])
# tea_varities[1:3] = []
# print(tea_varities)

# for tea in tea_varities:
#     print(tea, end="-")

# print(tea_varities)

# if "Onlong " in tea_varities:
#     print("I have Oolong tea")

# tea_varities.append("Oolong")
# print(tea_varities)

# if "Oolong" in tea_varities:
#     print("I have Oolong tea")


# print(tea_varities.pop())  # with the help of  pop we remove a element from array or a list eassily. and it gives that element 
# print(tea_varities)


# tea_varities.remove("green")
# print(tea_varities)

# tea_varities.insert(1, "green")
# print(tea_varities)


# tea_varities_copy = tea_varities.copy()
# print(tea_varities_copy)

# tea_varities_copy.append("Lemon")
# print(tea_varities_copy)


# square and cube

# squared_nums = [x**2 for x in range(10)]
# print(squared_nums)

# cube_nums = [x**3 for x in range(5)]
# print(cube_nums)

# print(range(10))


# chai_types = {"Masala": "Spicy", "Ginger": "Zesty", "Green":"Mild" }
# print(chai_types)
# print(chai_types["Masala"])
# chai_types["Green"] = "Fresh"
# print(chai_types)

# for chai in chai_types:
#     print(chai)
# for chai in chai_types:
#     print(chai, chai_types[chai])

# for key, value in chai_types.items():
#     print(key,value)

# if "Masala" in chai_types:
#     print("I have masala chai")

# print(len(chai_types))
# print(chai_types)

# chai_types["Earl Grey"] = "Citrus"
# print(chai_types)

# print(chai_types.pop("Ginger"))

# del chai_types["Green"]
# print(chai_types)




tea_shop = {
    "chai":{"Masala" : "Spicy" , "Ginger": "Zesty"},
    "Tea":{"Green":"Mild" ,"Black":"strong" }
}
print(tea_shop["Tea"])
print(tea_shop["chai"]["Ginger"])

squared_num = {x:x**2 for x in range(6)}
print(squared_num)
# squared_num.clear()
# print(squared_num)
keys = ["Masala", "Ginger" , "Lemon"]
print(keys)

default_value = "Delicious"
new_dict = dict.fromkeys(keys, default_value)
print(new_dict)

new_dict = dict.fromkeys(keys,keys)
print(new_dict)

tea_types = ("Black", "Green", "Oolong")
print(tea_types)
print(len(tea_types))

more_tea = ("Herbal", "Earl Grey")
print(more_tea)
all_tea = more_tea + tea_types
print(all_tea)

if "Green" in all_tea:
    print("I have green tea")
    
more_tea = ("Herbal" , "Earl Grey" , "Herbal")
print(more_tea)

print(more_tea.count("Herbal"))

print(more_tea.count("Herb"))

print(tea_types)

(black, green , Oolong) = tea_types
print(black)

print(type(tea_types))

username = input("give me a score value: ")
print(username)
