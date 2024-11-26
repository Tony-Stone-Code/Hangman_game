import random
import tkinter as tk
from tkinter import messagebox

class HangmanGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game")
        self.master.geometry("400x350")  # Adjusted window size to fit clue
        
        self.words_with_clues = {
            "python": "A popular programming language.",
            "hangman": "A word guessing game.",
            "challenge": "A task that tests someone's abilities.",
            "programming": "The process of writing computer code.",
            "development": "The process of developing something."
        }
        
        self.word_to_guess, self.hint = self.get_random_word_with_hint()
        self.guessed_letters = []
        self.incorrect_guesses = 0
        self.max_incorrect_guesses = 6
        
        self.display_word = tk.StringVar()
        self.display_word.set("_ " * len(self.word_to_guess))

        self.create_widgets()

    def get_random_word_with_hint(self):
        word, hint = random.choice(list(self.words_with_clues.items()))
        return word, hint

    def create_widgets(self):
        self.word_label = tk.Label(self.master, textvariable=self.display_word, font=("Helvetica", 18))
        self.word_label.pack(pady=20)

        self.hint_label = tk.Label(self.master, text=f"Hint: {self.hint}", font=("Helvetica", 12), wraplength=300)
        self.hint_label.pack(pady=10)

        self.guess_frame = tk.Frame(self.master)
        self.guess_frame.pack(pady=10)

        self.letters = 'abcdefghijklmnopqrstuvwxyz'
        self.buttons = []

        # Create buttons for each letter and arrange them in 5 columns
        for index, letter in enumerate(self.letters):
            btn = tk.Button(self.guess_frame, text=letter, command=lambda l=letter: self.guess(l), width=4)
            btn.grid(row=index // 5, column=index % 5, padx=2, pady=2)  # Use grid layout for 5 columns
            self.buttons.append(btn)

        self.incorrect_label = tk.Label(self.master, text=f"Incorrect guesses: {self.incorrect_guesses}/{self.max_incorrect_guesses}")
        self.incorrect_label.pack(pady=10)

        self.reset_button = tk.Button(self.master, text="Reset Game", command=self.reset_game)
        self.reset_button.pack(pady=10)

    def guess(self, letter):
        if letter in self.guessed_letters:
            messagebox.showinfo("Already Guessed", "You've already guessed that letter!")
            return
        
        self.guessed_letters.append(letter)

        if letter in self.word_to_guess:
            self.update_display_word()
            if "_" not in self.display_word.get():
                messagebox.showinfo("Congratulations!", f"You've guessed the word: {self.word_to_guess}")
                self.disable_buttons()
        else:
            self.incorrect_guesses += 1
            self.incorrect_label.config(text=f"Incorrect guesses: {self.incorrect_guesses}/{self.max_incorrect_guesses}")
            if self.incorrect_guesses >= self.max_incorrect_guesses:
                messagebox.showinfo("Game Over", f"Sorry, you've run out of guesses. The word was: {self.word_to_guess}")
                self.disable_buttons()

    def update_display_word(self):
        displayed = " ".join([letter if letter in self.guessed_letters else "_" for letter in self.word_to_guess])
        self.display_word.set(displayed)

    def disable_buttons(self):
        for button in self.buttons:
            button.config(state=tk.DISABLED)

    def reset_game(self):
        self.word_to_guess, self.hint = self.get_random_word_with_hint()
        self.guessed_letters = []
        self.incorrect_guesses = 0
        self.display_word.set("_ " * len(self.word_to_guess))
        self.incorrect_label.config(text=f"Incorrect guesses: {self.incorrect_guesses}/{self.max_incorrect_guesses}")
        self.hint_label.config(text=f"Hint: {self.hint}")
        for button in self.buttons:
            button.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
