import tkinter as tk
from tkinter import messagebox, ttk
import random

# Function to initialize or reset the game
def start_game():
    global number_to_guess, attempts
    number_to_guess = random.randint(1, 100)
    attempts = 0
    entry_box.delete(0, tk.END)
    feedback_label.config(text="Guess a number between 1 and 100!")

# Function to process the user's guess
def check_guess():
    global attempts
    try:
        guess = int(entry_box.get())
        attempts += 1

        if guess < 1 or guess > 100:
            feedback_label.config(text="Please guess a number between 1 and 100.")
        elif guess < number_to_guess:
            feedback_label.config(text="Too low! Try again.")
        elif guess > number_to_guess:
            feedback_label.config(text="Too high! Try again.")
        else:
            messagebox.showinfo("Congratulations!", f"You guessed it right in {attempts} attempts!")
            start_game()  # Restart the game
    except ValueError:
        feedback_label.config(text="Invalid input. Please enter a number.")

# Create the main application window
root = tk.Tk()
root.title("Number Guessing Game")

# Allow the window to be resizable
root.geometry("500x350")
root.minsize(500, 350)

# Colors
bg_color = "#2d2d2d"
text_color = "#ffffff"
guess_button_color = "#2196F3"  # Vibrant blue
reset_button_color = "#FF9800"  # Bright orange
hover_guess_color = "#42A5F5"  # Light blue for hover
hover_reset_color = "#FFB74D"  # Light orange for hover

root.configure(bg=bg_color)

# Styling for buttons (using ttk)
style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=10, background=guess_button_color, foreground=text_color, borderwidth=0)
style.map("TButton",
          background=[("active", hover_guess_color)],
          foreground=[("active", text_color)])
style.configure("Reset.TButton", background=reset_button_color, padding=10)
style.map("Reset.TButton",
          background=[("active", hover_reset_color)],
          foreground=[("active", text_color)])

# Widgets for the UI
title_label = tk.Label(root, text="Number Guessing Game", font=("Arial", 20, "bold"), bg=bg_color, fg=text_color)
title_label.pack(pady=15)

feedback_label = tk.Label(root, text="Guess a number between 1 and 100!", font=("Arial", 14), bg=bg_color, fg=text_color)
feedback_label.pack(pady=10)

entry_box = tk.Entry(root, font=("Arial", 16), justify="center", width=10, bg="#444444", fg=text_color, insertbackground=text_color, bd=0)
entry_box.pack(pady=10)

button_frame = tk.Frame(root, bg=bg_color)
button_frame.pack(pady=20)

guess_button = ttk.Button(button_frame, text="Guess", style="TButton", command=check_guess)
guess_button.grid(row=0, column=0, padx=10)

reset_button = ttk.Button(button_frame, text="Restart Game", style="Reset.TButton", command=start_game)
reset_button.grid(row=0, column=1, padx=10)

# Initialize the game
start_game()

# Start the application
root.mainloop()
