import sqlite3


def signup(username, password):
    pass


def signin(username, password):
    pass


def main():
    operation = input("""
1 ) Create an account
2 ) Sign in to your account
Choose an operation : """)

    if operation == "1":
        us = input("Choose a username : ")
        pw = input("Choose a strong password : ")
        signup(us, pw)

    elif operation == "2":
        us = input("Enter your username : ")
        pw = input("Enter your password : ")
        signin(us, pw)

    else:
        print("Invalid option, Try again.")
        main()


main()
