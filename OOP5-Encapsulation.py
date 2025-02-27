class MyClass:
    def __init__(self):
        self.a = "I am a public member"
        self._b = "I am a protected member"
        self.__c = "I am a private member"

    def public_method(self):
        print("This is a public method")

    def _protected_method(self):
        print("This is a protected method")

    def __private_method(self):
        print("This is a private method")
        print(self.__private_member)


# Creating an instance of the class
obj = MyClass()


# Accessing public members and calling public methods

# print(obj.a)
# obj.public_method()
#
# print("-"*50)
#
# obj.public_member = "Im not a public member"
# print(obj.public_member)

# Accessing protected members and calling protected methods
# print(obj._b)
# obj._protected_method()
#
# print("-" * 50)
#
# obj._b = "Im not a protected member"
# print(obj._b)

# Trying to access private members and calling private methods (will result in an error)

# print(obj.__c)
# obj.__private_method()

# obj.__c = "yechizi"
# print(obj.__c)

# --------------------------------------------------------------------------------------------


# class Person:
#     def __init__(self):
#         self.fname = "Ahura"
#         self.lname = "Kiani"
#         self._phonenumber = "09336121020"
#         self.__nationalcode = "0012056971"
#
#     def talk(self):
#         print(f"Hi my name is {self.fname}")
#
#     def _transferinformation(self):
#         print(f"This is my phone number : {self._phonenumber}")
#
#     def __signcontract(self):
#         print(f"My national ID is {self.__nationalcode} and I accept the terms of this contract")
#
#
# user = Person()
#
# print(user.fname)
# user.talk()
#
# print(user._phonenumber)
# user._transferinformation()
#
# print(user.__nationalcode)
# user.__signcontract()

# --------------------------------------------------------------------------------------------

class Car:
    def __init__(self):
        self.color = "Black"  # Public member
        self.__mileage = 0  # Private member

    def _drive(self, kilometers):
        print("Driving the car")
        for i in range(kilometers):
            self.__increase_mileage()

        print(f"Mileage : {self.__mileage}")

    def __increase_mileage(self):  # The Getter method
        self.__mileage += 1  # Accesing private member


my_car = Car()
my_car._drive(35)
my_car._drive(2)
print(my_car.__milage)
