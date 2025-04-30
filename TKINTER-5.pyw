import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import font as tkfont  # Import the font module

# Sample data: city and its temperature
city_temperatures = {
    "New York": "15°C",
    "Los Angeles": "22°C",
    "Chicago": "10°C",
    "Houston": "28°C",
    "Phoenix": "35°C"
}


def show_temperature():
    selected_city = city_combobox.get()
    temperature = city_temperatures.get(selected_city, "Temperature not available")
    (messagebox.showinfo("Temperature", f"The temperature in {selected_city} is {temperature}"))


# Create the main window
root = tk.Tk()
root.title("City Temperature Finder")
root.geometry("300x200")  # Set initial window size

custom_font = tkfont.Font(family="Sans", size=9, weight="bold")
# Create a label
label = ttk.Label(root, text="Select a city:", font=custom_font)
label.pack(pady=(20, 10))  # Add padding (top, bottom)

# Create a combo box
city_combobox = ttk.Combobox(root, values=list(city_temperatures.keys()))
city_combobox.pack(pady=(0, 20), padx=20, fill='x')  # Add padding and fill horizontally

# Create a ttk button to show the temperature
show_button = ttk.Button(root, text="Show Temperature", command=show_temperature)
show_button.pack(pady=(10, 20), padx=20, ipadx=5)  # Add padding and internal padding

# Run the application
root.mainloop()
