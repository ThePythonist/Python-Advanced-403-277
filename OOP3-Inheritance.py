# class A:
#     def say_hello(self):
#         print("HELLO")
#
#
# class B(A):
#     def say_goodbye(self):
#         print("GOODBYE")
#
#
# parent = A()
# child = B()
#
# child.say_hello()

# =======================================================================================================

# class Parent:
#     def __init__(self, age, address, city, job):
#         self.age = age
#         self.address = address
#         self.city = city
#         self.job = job
#
#     def parent_method(self):
#         print("hello from parent method")
#
#
# class Child(Parent):
#     def __init__(self, age, address, city, university, job=None): # job : optional argument
#         super().__init__(age, address, city, job)
#         self.university = university
#
#     def child_method(self):
#         print("hello from child method")
#
#
# valed = Parent(50, "ekbatan/block_a", "tehran", "teacher")
# farzand = Child(23, "marzadaran/alvand", "tehran", "sharif","engineer")
#
# print(farzand.job)

# =======================================================================================================

class Parent:
    def __init__(self, age, address, city, job):
        self.age = age
        self.address = address
        self.city = city
        self.job = job


class Child:
    def __init__(self, name, university):
        self.name = name
        self.university = university


valed = Parent(50, "ekbatan/block_a", "tehran", "teacher")
farzand = Child("ali", "sharif")
farzand.parent = valed

print(farzand.university)
print(farzand.parent.address)
