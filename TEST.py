import datetime

thisyear = datetime.datetime.now().year

birth = int(input("Enter your birth year : "))

age = thisyear - birth

print(age)

