import random


def irancell():
    prefix = ["0939", "0938", "0936", "0902"]

    phonenumber = f"{random.choice(prefix)}"

    for i in range(7):
        phonenumber += str(random.randint(0, 9))

    print(phonenumber)


def hamrahaval():
    prefix = ["0912", "0911", "0919", "0993"]

    phonenumber = f"{random.choice(prefix)}"

    for i in range(7):
        phonenumber += str(random.randint(0, 9))

    print(phonenumber)


def rightel():
    prefix = ["0921", "0922", "0923"]

    phonenumber = f"{random.choice(prefix)}"

    for i in range(7):
        phonenumber += str(random.randint(0, 9))

    print(phonenumber)
