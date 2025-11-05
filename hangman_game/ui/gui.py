"""
Enhanced GUI for Hangman game with improved UX
"""

import tkinter as tk
from tkinter import messagebox, ttk
from hangman_game.core.game_logic import HangmanLogic
from hangman_game.core.statistics import Statistics
from hangman_game.ui.hangman_art import get_hangman_stage


class HangmanGUI:
    """Enhanced Hangman game GUI"""
    
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game")
        self.master.geometry("600x700")
        self.master.resizable(False, False)
        
        # Game components
        self.difficulty = tk.StringVar(value="medium")
        self.game_logic = None
        self.stats = Statistics()
        
        # UI variables
        self.display_word = tk.StringVar()
        self.hangman_display = tk.StringVar()
        
        # Colors and styling
        self.bg_color = "#f0f0f0"
        self.primary_color = "#2c3e50"
        self.success_color = "#27ae60"
        self.danger_color = "#e74c3c"
        
        self.master.configure(bg=self.bg_color)
        
        self.create_widgets()
        self.start_new_game()
        
        # Bind keyboard events
        self.master.bind('<Key>', self.on_key_press)
    
    def create_widgets(self):
        """Create all GUI widgets"""
        # Title
        title_frame = tk.Frame(self.master, bg=self.bg_color)
        title_frame.pack(pady=10)
        
        title_label = tk.Label(
            title_frame,
            text="🎮 HANGMAN GAME 🎮",
            font=("Helvetica", 24, "bold"),
            bg=self.bg_color,
            fg=self.primary_color
        )
        title_label.pack()
        
        # Hangman visual
        self.hangman_label = tk.Label(
            self.master,
            textvariable=self.hangman_display,
            font=("Courier", 10),
            bg="white",
            fg=self.primary_color,
            justify=tk.LEFT,
            relief=tk.SUNKEN,
            padx=10,
            pady=10
        )
        self.hangman_label.pack(pady=10, padx=20, fill=tk.BOTH)
        
        # Word display
        word_frame = tk.Frame(self.master, bg=self.bg_color)
        word_frame.pack(pady=10)
        
        self.word_label = tk.Label(
            word_frame,
            textvariable=self.display_word,
            font=("Helvetica", 28, "bold"),
            bg=self.bg_color,
            fg=self.primary_color,
            height=2
        )
        self.word_label.pack()
        
        # Hint
        self.hint_label = tk.Label(
            self.master,
            text="",
            font=("Helvetica", 11, "italic"),
            wraplength=500,
            bg=self.bg_color,
            fg="#555"
        )
        self.hint_label.pack(pady=5)
        
        # Incorrect guesses counter
        self.incorrect_label = tk.Label(
            self.master,
            text="",
            font=("Helvetica", 12),
            bg=self.bg_color,
            fg=self.danger_color
        )
        self.incorrect_label.pack(pady=5)
        
        # Letter buttons frame
        buttons_frame = tk.Frame(self.master, bg=self.bg_color)
        buttons_frame.pack(pady=10)
        
        tk.Label(
            buttons_frame,
            text="Click a letter or use your keyboard:",
            font=("Helvetica", 10),
            bg=self.bg_color
        ).pack()
        
        self.guess_frame = tk.Frame(buttons_frame, bg=self.bg_color)
        self.guess_frame.pack(pady=5)
        
        self.letters = 'abcdefghijklmnopqrstuvwxyz'
        self.buttons = {}
        
        # Create letter buttons in a grid
        for index, letter in enumerate(self.letters):
            btn = tk.Button(
                self.guess_frame,
                text=letter.upper(),
                command=lambda l=letter: self.guess(l),
                width=3,
                height=1,
                font=("Helvetica", 10, "bold"),
                bg="#3498db",
                fg="white",
                activebackground="#2980b9",
                relief=tk.RAISED,
                bd=2
            )
            row = index // 9
            col = index % 9
            btn.grid(row=row, column=col, padx=2, pady=2)
            self.buttons[letter] = btn
        
        # Control panel
        control_frame = tk.Frame(self.master, bg=self.bg_color)
        control_frame.pack(pady=10)
        
        # Difficulty selector
        tk.Label(
            control_frame,
            text="Difficulty:",
            font=("Helvetica", 10),
            bg=self.bg_color
        ).grid(row=0, column=0, padx=5)
        
        for idx, diff in enumerate(["easy", "medium", "hard"]):
            rb = tk.Radiobutton(
                control_frame,
                text=diff.capitalize(),
                variable=self.difficulty,
                value=diff,
                font=("Helvetica", 10),
                bg=self.bg_color,
                command=self.change_difficulty
            )
            rb.grid(row=0, column=idx+1, padx=5)
        
        # Buttons
        button_frame = tk.Frame(self.master, bg=self.bg_color)
        button_frame.pack(pady=10)
        
        self.new_game_button = tk.Button(
            button_frame,
            text="🔄 New Game",
            command=self.start_new_game,
            font=("Helvetica", 11, "bold"),
            bg=self.success_color,
            fg="white",
            padx=15,
            pady=5,
            relief=tk.RAISED,
            bd=3
        )
        self.new_game_button.grid(row=0, column=0, padx=5)
        
        stats_button = tk.Button(
            button_frame,
            text="📊 Statistics",
            command=self.show_statistics,
            font=("Helvetica", 11, "bold"),
            bg="#9b59b6",
            fg="white",
            padx=15,
            pady=5,
            relief=tk.RAISED,
            bd=3
        )
        stats_button.grid(row=0, column=1, padx=5)
        
        # Status bar
        self.status_label = tk.Label(
            self.master,
            text="Ready to play!",
            font=("Helvetica", 9),
            bg="#34495e",
            fg="white",
            pady=3
        )
        self.status_label.pack(side=tk.BOTTOM, fill=tk.X)
    
    def start_new_game(self):
        """Start a new game"""
        self.game_logic = HangmanLogic(difficulty=self.difficulty.get())
        word, hint = self.game_logic.start_new_game()
        
        # Update UI
        self.display_word.set(self.game_logic.get_display_word())
        self.hint_label.config(text=f"💡 Hint: {hint}")
        self.update_hangman_display()
        self.update_incorrect_label()
        self.enable_all_buttons()
        self.status_label.config(text=f"Game started! Difficulty: {self.difficulty.get().capitalize()}")
    
    def change_difficulty(self):
        """Handle difficulty change"""
        if messagebox.askyesno("Change Difficulty", "Start a new game with this difficulty?"):
            self.start_new_game()
    
    def guess(self, letter):
        """Handle a letter guess"""
        if self.game_logic.game_won or self.game_logic.game_lost:
            return
        
        result = self.game_logic.make_guess(letter)
        
        if not result["valid"]:
            messagebox.showinfo("Already Guessed", "You've already guessed that letter!")
            return
        
        # Disable the button
        self.buttons[letter].config(
            state=tk.DISABLED,
            bg="#95a5a6" if not result["correct"] else "#27ae60"
        )
        
        # Update display
        self.display_word.set(self.game_logic.get_display_word())
        self.update_hangman_display()
        self.update_incorrect_label()
        
        # Check game state
        if result.get("game_won"):
            self.handle_game_won()
        elif result.get("game_lost"):
            self.handle_game_lost()
        elif result["correct"]:
            self.status_label.config(text="✓ Correct letter!", bg=self.success_color)
        else:
            self.status_label.config(text="✗ Wrong letter!", bg=self.danger_color)
    
    def on_key_press(self, event):
        """Handle keyboard input"""
        if event.char.isalpha() and len(event.char) == 1:
            letter = event.char.lower()
            if letter in self.letters and self.buttons[letter]["state"] != tk.DISABLED:
                self.guess(letter)
    
    def update_hangman_display(self):
        """Update the hangman ASCII art"""
        state = self.game_logic.get_game_state()
        art = get_hangman_stage(
            state["incorrect_guesses"],
            state["max_incorrect_guesses"]
        )
        self.hangman_display.set(art)
    
    def update_incorrect_label(self):
        """Update the incorrect guesses label"""
        state = self.game_logic.get_game_state()
        self.incorrect_label.config(
            text=f"❌ Incorrect guesses: {state['incorrect_guesses']}/{state['max_incorrect_guesses']}"
        )
    
    def handle_game_won(self):
        """Handle game won state"""
        self.disable_all_buttons()
        self.stats.record_game(
            won=True,
            difficulty=self.difficulty.get(),
            guesses=len(self.game_logic.guessed_letters)
        )
        self.status_label.config(text="🎉 Congratulations! You won!", bg=self.success_color)
        messagebox.showinfo(
            "Victory! 🎉",
            f"Congratulations! You've guessed the word:\n\n{self.game_logic.word_to_guess.upper()}\n\n"
            f"Incorrect guesses: {self.game_logic.incorrect_guesses}"
        )
    
    def handle_game_lost(self):
        """Handle game lost state"""
        self.disable_all_buttons()
        self.stats.record_game(
            won=False,
            difficulty=self.difficulty.get(),
            guesses=len(self.game_logic.guessed_letters)
        )
        self.status_label.config(text="😢 Game Over - You lost!", bg=self.danger_color)
        messagebox.showinfo(
            "Game Over 😢",
            f"Sorry, you've run out of guesses!\n\nThe word was:\n\n{self.game_logic.word_to_guess.upper()}"
        )
    
    def enable_all_buttons(self):
        """Enable all letter buttons"""
        for button in self.buttons.values():
            button.config(state=tk.NORMAL, bg="#3498db")
    
    def disable_all_buttons(self):
        """Disable all letter buttons"""
        for button in self.buttons.values():
            button.config(state=tk.DISABLED)
    
    def show_statistics(self):
        """Show statistics window"""
        stats_window = tk.Toplevel(self.master)
        stats_window.title("Game Statistics")
        stats_window.geometry("400x400")
        stats_window.resizable(False, False)
        stats_window.configure(bg=self.bg_color)
        
        # Title
        tk.Label(
            stats_window,
            text="📊 Your Statistics",
            font=("Helvetica", 18, "bold"),
            bg=self.bg_color,
            fg=self.primary_color
        ).pack(pady=15)
        
        stats = self.stats.get_stats()
        win_rate = self.stats.get_win_rate()
        
        # Stats frame
        stats_frame = tk.Frame(stats_window, bg="white", relief=tk.RIDGE, bd=2)
        stats_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
        
        # General stats
        stats_text = f"""
        Games Played: {stats['games_played']}
        Games Won: {stats['games_won']}
        Games Lost: {stats['games_lost']}
        Win Rate: {win_rate:.1f}%
        
        Current Streak: {stats['current_streak']}
        Best Streak: {stats['best_streak']}
        
        By Difficulty:
        
        Easy:
          Played: {stats['by_difficulty']['easy']['played']}
          Won: {stats['by_difficulty']['easy']['won']}
        
        Medium:
          Played: {stats['by_difficulty']['medium']['played']}
          Won: {stats['by_difficulty']['medium']['won']}
        
        Hard:
          Played: {stats['by_difficulty']['hard']['played']}
          Won: {stats['by_difficulty']['hard']['won']}
        """
        
        tk.Label(
            stats_frame,
            text=stats_text,
            font=("Courier", 11),
            bg="white",
            justify=tk.LEFT,
            padx=20,
            pady=10
        ).pack()
        
        # Reset button
        reset_button = tk.Button(
            stats_window,
            text="Reset Statistics",
            command=lambda: self.reset_statistics(stats_window),
            font=("Helvetica", 10),
            bg=self.danger_color,
            fg="white",
            padx=10,
            pady=5
        )
        reset_button.pack(pady=10)
        
        # Close button
        close_button = tk.Button(
            stats_window,
            text="Close",
            command=stats_window.destroy,
            font=("Helvetica", 10),
            bg=self.primary_color,
            fg="white",
            padx=20,
            pady=5
        )
        close_button.pack(pady=5)
    
    def reset_statistics(self, window):
        """Reset all statistics"""
        if messagebox.askyesno("Reset Statistics", "Are you sure you want to reset all statistics?"):
            self.stats.reset_stats()
            window.destroy()
            messagebox.showinfo("Statistics Reset", "All statistics have been reset.")


def main():
    """Main entry point for the GUI"""
    root = tk.Tk()
    app = HangmanGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
