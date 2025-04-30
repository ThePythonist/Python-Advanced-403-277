import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *

# from queries import signin_logic, signup_logic

# root window
root = tk.Tk()
root.geometry("400x250")
root.resizable(False, False)
root.title('Sign In')

# store email address and password
username = tk.StringVar()
password = tk.StringVar()


def login_clicked():
    """ callback when the login button clicked
    """
    print(username.get())
    print(password.get())
    showinfo(
        title='Information',
        message=f"Successfully logged in as {username.get()}"
    )

    # showerror(
    #     title='Information',
    #     message=f"Incorrect credentials"
    # )


# Sign in frame
signin = ttk.Frame(root)
signin.pack(padx=10, pady=10, fill='x', expand=True)

# email
email_label = ttk.Label(signin, text="Username")
email_label.pack(fill='x', expand=True, padx=50, pady=10)

email_entry = ttk.Entry(signin, textvariable=username)
email_entry.pack(fill='x', expand=True, padx=50)
email_entry.focus()

# password
password_label = ttk.Label(signin, text="Password")
password_label.pack(fill='x', expand=True, padx=50, pady=10)

password_entry = ttk.Entry(signin, textvariable=password, show="*")
password_entry.pack(fill='x', expand=True, padx=50)

# login button
login_button = ttk.Button(signin, text="Login", command=login_clicked)
login_button.pack(fill='x', expand=True, pady=30, padx=140)

root.mainloop()
