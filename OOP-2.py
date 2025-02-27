class SedanCar:
    # class attribute
    zarfiat = 5

    # instance attribute
    def __init__(self, name, hp):
        self.name = name
        self.horsepower = hp


car1 = SedanCar("samand", 110)
car2 = SedanCar("dena", 120)

# car1.zarfiat = 4
# print(car1.zarfiat)
# print(car2.zarfiat)

SedanCar.zarfiat = 2
print(car1.zarfiat)
print(car2.zarfiat)
