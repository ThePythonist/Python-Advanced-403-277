# import math
# # Aliasing
# def greetings(name):
#     return "Hello" + " " + name
#
#
# ahvalporsi = greetings
# print(greetings("nima"))
# print(ahvalporsi("nima"))
#
# jazr = math.sqrt
# bechap = print
# bechap(jazr(100))
# ======================================================
def greetings():
    return "Hello"


def compose(func):
    return func()


print(compose(greetings))
