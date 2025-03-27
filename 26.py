import sqlite3


class User:
    def __init__(self, username, password, email=None):
        self.username = username
        self.password = password
        self.email = email

        conn = sqlite3.connect("accounts.db")
        cur = conn.cursor()

        query = "CREATE TABLE IF NOT EXISTS users (username,password,email);"
        cur.execute(query)

        query = f"""
        INSERT INTO users VALUES 
        {(self.username, self.password, self.email if bool(self.email) else 'null')};"""
        cur.execute(query)

        conn.commit()
        conn.close()


def validate_username(username):
    conn = sqlite3.connect("accounts.db")
    cur = conn.cursor()

    cur.execute("SELECT username FROM users;")
    usernames = cur.fetchall()

    for i in usernames:
        if i[0] == username:
            return False
    else:
        return True


def validate_password(password):
    # TODO : password must contain 8 letters, 1 capital character, 1 numeric character
    pass


def signup(username, password, email=None):
    user = User(username, password, email)
    print("Successfully signed up!")


def signin(username, password):
    # TODO : username can be username or email
    conn = sqlite3.connect("accounts.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM users;")
    users = cur.fetchall()

    for i in users:
        if i[0] == username and i[1] == password:
            return "Successfully logged in"
    else:
        return "Incorrect username or password"


def main():
    operation = input("""
1 ) Create an account
2 ) Sign in to your account
Choose an operation : """)

    if operation == "1":
        us = input("Choose a username : ")
        if not validate_username(us):
            print("Username is already taken")
            main()
        else:
            pw = input("Choose a strong password : ")
            em = input("Enter a valid email address or leave blank : ")
            signup(us, pw, em)

    elif operation == "2":
        us = input("Enter your username : ")
        pw = input("Enter your password : ")
        print(signin(us, pw))

    else:
        print("Invalid option, Try again.")
        main()


main()
