def factorial(x):
    if x == 1:
        return x
    else:
        return x * factorial(x - 1)


x = int(input("Enter any number : "))
if x > 0:
    print(f"Factorial of {x} is", factorial(x))
elif x < 0:
    print("Factorial doesnt exists")
else:
    print("Factorial of zero is one")
