# I acknowledge the use of ChatGPT to create parts of this code.

import random
import tkinter as tk
from tkinter import messagebox

class NumberGuessingGame:
    def __init__(self):
        self.level = 1
        self.max_number = 50
        self.start_new_level()

    def start_new_level(self):
        self.secret_number = random.randint(1, self.max_number)
        self.attempts = 0

    def check_guess(self, guess):
        self.attempts += 1
        if guess < self.secret_number:
            return "Too low!"
        elif guess > self.secret_number:
            return "Too high!"
        else:
            self.level += 1
            self.max_number += 50  # Increase difficulty
            self.start_new_level()
            return f"Correct! Moving to level {self.level}, number range is now 1-{self.max_number}."

def start_game():
    game = NumberGuessingGame()

    def submit_guess():
        try:
            guess = int(entry.get())
            result = game.check_guess(guess)
            messagebox.showinfo("Result", result)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")

    window = tk.Tk()
    window.title("Number Guessing Game: Multiple Levels")

    label = tk.Label(window, text=f"Guess a number between 1 and {game.max_number}:")
    label.pack(pady=10)

    entry = tk.Entry(window)
    entry.pack(pady=5)

    submit_button = tk.Button(window, text="Guess", command=submit_guess)
    submit_button.pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    start_game()
