import tkinter


def action_log():
    print("The button was clicked!")


root = tkinter.Tk()

root.title("My First App")
root.geometry("550x550")  # HEIGHTxWIDTH
root.resizable(width=False, height=False)
root.configure(background="#23b491")

message = tkinter.Label(root, text="WELCOME TO MY GUI APP")
message.config(bg="black", fg="white", font="Consolas 16 bold", pady="20px", padx="10px")
message.pack(side="top", anchor="n", fill="x")  # top-left-right-bottom & n-s-w-e
# message.pack(side="top", anchor="n", fill="y", expand=True)  # top-left-right-bottom & n-s-w-e

mybutton = tkinter.Button(root, text="DO NOT CLICK", command=action_log)
mybutton.config(bg="white", fg="black", font="Consolas 16 bold", pady="20px", padx="10px")
mybutton.pack(side="bottom", anchor="n", pady="45px", padx="20px")

root.mainloop()
