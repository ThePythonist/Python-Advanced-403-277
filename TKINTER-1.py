import tkinter

root = tkinter.Tk()
root.title("My First GUI App")
root.geometry("512x480")  # widthxheight
root.resizable(width=False, height=False)
# root.configure(bg="black")
root.configure(bg="#61273a")

message1 = tkinter.Label(root, text="Welcome To My GUI App")
message1.configure(bg="black", fg="white", font="Consolas 14 bold", padx=40, pady=2)
# message1.pack(anchor="s", side="left")
# message1.pack(fill="y", expand=True)
# message1.pack(fill="x", expand=True)
message1.pack(fill="x")
# message1.place(x=20, y=10)
root.mainloop()
