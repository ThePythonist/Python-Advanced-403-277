class Dog:
    def sound(self):
        return "Woof!"


class Cat:
    def sound(self):
        return "Meow!"


class Cow:
    def sound(self):
        return "Moo!"


# Polymorphic method
def make_sound(animal):
    print(animal.sound())


# Create instances of different animal classes
# woody = Dog()
# jimmy = Cat()
# taylor = Cow()
#
# # Call the make_sound function with different animal objects
# make_sound(taylor)

# # -----------------------------------------------------------------------
#
# Polymorphism in built-in objects

t = (10, 20, 30, 40, 10, 10)
l = [50, 60, 10, 10]

# Call the __len__() method on each instance
# Magic methods are special methods and they are automatically called when object is created


# print(t.__len__())
# print(l.__len__())

print(dir(t))
print(dir(l))

# print(t.count(10))
# print(l.count(10))

print(t.__doc__)
