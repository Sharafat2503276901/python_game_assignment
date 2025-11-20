# I acknowledge the use of ChatGPT to create parts of this code.

import random
import tkinter as tk
from tkinter import messagebox

# Game logic
class NumberGuessingGame:
    def __init__(self):
        self.secret_number = random.randint(1, 50)
        self.attempts = 0

    def check_guess(self, guess):
        self.attempts += 1
        if guess < self.secret_number:
            return "Too low!"
        elif guess > self.secret_number:
            return "Too high!"
        else:
            return f"Correct! You guessed in {self.attempts} attempts."

# GUI setup
def start_game():
    game = NumberGuessingGame()

    def submit_guess():
        try:
            guess = int(entry.get())
            result = game.check_guess(guess)
            messagebox.showinfo("Result", result)
            if "Correct!" in result:
                window.destroy()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")

    window = tk.Tk()
    window.title("Number Guessing Game")

    label = tk.Label(window, text="Guess a number between 1 and 50:")
    label.pack(pady=10)

    entry = tk.Entry(window)
    entry.pack(pady=5)

    submit_button = tk.Button(window, text="Guess", command=submit_guess)
    submit_button.pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    start_game()
