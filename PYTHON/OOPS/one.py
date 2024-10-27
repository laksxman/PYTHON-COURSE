# Q1. Basic Class and Object
#  Create a car class with attributes like and model. Then crate an instance of this class.

# class Car:
#         def __init__(self, brand , model):
#                 self.brand = brand
#                 self.model = model
                
                
# my_car = Car("Toyota" , "Corolla")
# print(my_car.brand)
# print(my_car.model)

# my_new_car = Car("Tata","Safari")
# print(my_new_car.brand)
# print(my_new_car.model)


# Q2. Class Method to the car class that displays the
#   full name of the car(brand and model).


# class Car:
#         def __init__(self, brand , model):
#                 self.brand = brand
#                 self.model = model
                

#         def full_name(self):
#                 return f"{self.brand} {self.model}"
                
# my_car = Car("Toyota" , "Corolla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

# my_new_car = Car("Tata","Safari")
# print(my_new_car.brand)



# Q3. Inheritence
#  Create an ElectricCar class that inherits from the
#  Car class and has an additional attribute battery_size.


# class Car:
#         def __init__(self, brand , model):
#                 self.brand = brand
#                 self.model = model
                

#         def full_name(self):
#                 return f"{self.brand} {self.model}"
        

# class Electriccar(Car):
#         def __init__(self, brand, model,battery_size):
#                 super().__init__(brand, model)
#                 self.battery_size = battery_size


# my_tesla = Electriccar("Tesla", "Model S", "85kwh")
# # print(my_tesla.model)
# print(my_tesla.full_name())

                

# Q4. Encapsulation
#  Modify the Car class to encapsulate the brnad 
#  attribute, making it private, and provide a getter
#   method for it.


# class Car:
#         def __init__(self, brand , model):
#                 self.__brand = brand
#                 self.model = model

#         def get_brnad(self):
#                 return self.__brnad + " !"
                

#         def full_name(self):
#                 return f"{self.__brand} {self.model}"
        

# class Electriccar(Car):
#         def __init__(self, __brand, model,battery_size):
#                 super().__init__(__brand, model)
#                 self.battery_size = battery_size

# my_tesla = Electriccar("Tesla", "Model S", "85kwh")
# # print(my_tesla.__brand)
# print(my_tesla.get_brnad())


class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number   # Public attribute
        self.__balance = balance                # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds or invalid amount.")

    def get_balance(self):
        return self.__balance                   # Accessing the private attribute

# Example usage:
account = BankAccount("123456789")
account.deposit(100)
account.withdraw(50)
print(f"Current Balance: ${account.get_balance()}")

# Trying to access the private attribute directly (will raise an error)
# print(account.__balance)  # This will raise an AttributeError


# Q5. Polymorphism
#  Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviours.







# Q6. Class variables
#  Add a class variable to Car that keeps of the number of cars created.

class Car:
    car_count = 0

    def __init__(self,make, model ):
        self.model = model
        self.make = make

        Car.car_count +=1

car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

print(f"Total cars created: {Car.car_count}")



# Q7. Static method
#  Add a static method to the Car class that returns a general description of a car.

class Car:
    car_count = 0

    def __init__(self,make, model ):
        self.model = model
        self.make = make

        Car.car_count +=1

    @staticmethod
    def general_description():
        return "A car is a wheeled motor vehicle used for transportation."


car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

print(f"Total cars created: {Car.car_count}")
print(Car.general_description())


# Q8. Property Decorators 
#  Use a property decorator in the Car class to make the model attribute read_only.

class Car:
    car_count = 0

    def __init__(self,make, model):
        self.make = make
        self.model = model

        Car.car_count +=1

    @property
    def modelo(self):
        return self._model

    @staticmethod
    def general_description():
        return "A car is a wheeled motor vehicle used for transportation."

car1 = Car("Toyota", "Corolla")

print(f"Total cars created: {Car.car_count}")
print(car1.model)

try:
    car1.model = "Camry"
except AttributeError as e:
    print(e)
       


# Q9. Class iinheritance and isinstance Function
#  Demonstrate the use of isinstance() to check if my_tels is an instance of Car and ElectricCar.


#  if isinstance(my_tels, Car) and isinstances(my_tels, ElestricCar):
#     print("my_tels is an instance of both Car and ElecticCar.")
# else:
#     print("my_tels is not an instance of both Car and ElecticCar.")

# Q10. Multiple Inheritance
#  Create two classes Bettery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.


class Battery:
    def __init__(self, capacity):
        self.capacity = capacity

    def display_capacity(self):
        print(f"Battery capacity: {self.capacity} kWh")

class Engine:
    def __init__(self, power):
        self.power = power

    def display_power(self): 
        print(f"Engine power: {self.power} HP")

class ElectricCar(Battery, Engine):
    def __init__(self, capacity, power):
        Battery.__init__(self, capacity)
        Engine.__init__(self, power)

# Example usage
my_tels = ElectricCar(100, 400)
my_tels.display_capacity()
my_tels.display_power()


