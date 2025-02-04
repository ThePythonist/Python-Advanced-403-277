from time import sleep
from random import choice, randint, sample
from os import system


# def password(length):
#     pw = []
#     for i in range(length):
#         # digit = str(choice(range(0, 10)))
#         digit = str(randint(0, 9))
#         pw.append(digit)
#
#     print("".join(pw))

def password(length):
    pw = [str(i) for i in sample(range(0, 9), length)]
    print("".join(pw))


while True:
    print("Password : ", end="")
    password(6)
    sleep(6)
    system("cls")
