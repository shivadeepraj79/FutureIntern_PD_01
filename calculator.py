import tkinter as tk
from tkinter import messagebox

# Function to handle button presses
def press(key):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + key)

# Function to clear the input field
def clear():
    entry.delete(0, tk.END)

# Function to evaluate the entered expression
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except ZeroDivisionError:
        messagebox.showerror("Error", "Division by zero is not allowed.")
    except Exception as e:
        messagebox.showerror("Error", "Invalid input.")

# Create the main application window
root = tk.Tk()
root.title("Calculator")

# Allow window to be resizable
root.geometry("360x480")
root.minsize(360, 480)

# Colors
bg_color = "#2d2d2d"
button_color = "#4caf50"
text_color = "#ffffff"
special_button_color = "#ff5722"

root.configure(bg=bg_color)

# Entry widget for input and displaying results
entry = tk.Entry(root, font=("Arial", 24), justify="right", bg="#333333", fg=text_color, bd=0, relief="flat")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=10, padx=10, pady=10, sticky="nsew")

# Define button layout and their corresponding actions
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('.', 4, 2), ('+', 4, 3),
    ('=', 5, 0)
]

# Create buttons dynamically and add them to the grid
for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, bg=special_button_color, fg=text_color,
                        font=("Arial", 14), bd=0, relief="flat", command=calculate)
        btn.grid(row=row, column=col, columnspan=4, padx=10, pady=10, sticky="nsew")
    elif text == 'C':
        btn = tk.Button(root, text=text, bg=special_button_color, fg=text_color,
                        font=("Arial", 14), bd=0, relief="flat", command=clear)
        btn.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
    else:
        btn = tk.Button(root, text=text, bg=button_color, fg=text_color,
                        font=("Arial", 14), bd=0, relief="flat", command=lambda t=text: press(t))
        btn.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

# Configure grid to adjust dynamically
for i in range(6):  # 5 rows (buttons) + 1 row (entry)
    root.grid_rowconfigure(i, weight=1)

for j in range(4):  # 4 columns
    root.grid_columnconfigure(j, weight=1)

# Start the application
root.mainloop()
