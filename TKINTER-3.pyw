import tkinter
from tkinter import messagebox


def login():
    # messagebox.showwarning("Result", "Successfully Logged In")
    # messagebox.showerror("Result", "Successfully Logged In")
    # messagebox.showinfo("Result", "Successfully Logged In")
    messagebox.askyesnocancel("Result", "Do you want to continue?")


root = tkinter.Tk()
root.title('Test Window')
root.geometry("400x400")
root.resizable(width=False, height=True)
root.configure(background="#11a192")

btn = tkinter.Button(root, font=("consolas", 17, "bold"), fg="black", text="Login", command=login)
btn.pack(pady=20, padx=20, fill="x")

root.mainloop()
