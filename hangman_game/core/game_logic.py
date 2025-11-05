"""
Core game logic for Hangman game
"""

import random
import json
from pathlib import Path
from typing import Tuple, List, Dict, Optional


class HangmanLogic:
    """Core Hangman game logic without UI dependencies"""
    
    def __init__(self, difficulty: str = "medium"):
        """
        Initialize the game logic
        
        Args:
            difficulty: Game difficulty level (easy, medium, hard)
        """
        self.difficulty = difficulty
        self.words_with_clues = self._load_words()
        self.word_to_guess = ""
        self.hint = ""
        self.guessed_letters = []
        self.incorrect_guesses = 0
        self.max_incorrect_guesses = self._get_max_incorrect_guesses()
        self.game_won = False
        self.game_lost = False
        
    def _get_max_incorrect_guesses(self) -> int:
        """Get maximum incorrect guesses based on difficulty"""
        difficulty_map = {
            "easy": 8,
            "medium": 6,
            "hard": 4
        }
        return difficulty_map.get(self.difficulty, 6)
    
    def _load_words(self) -> Dict[str, str]:
        """Load words and clues from data file"""
        data_dir = Path(__file__).parent.parent / "data"
        words_file = data_dir / "words.json"
        
        # Default words if file doesn't exist
        default_words = {
            "python": "A popular programming language.",
            "hangman": "A word guessing game.",
            "challenge": "A task that tests someone's abilities.",
            "programming": "The process of writing computer code.",
            "development": "The process of developing something.",
            "computer": "An electronic device for processing data.",
            "algorithm": "A step-by-step procedure for solving a problem.",
            "database": "An organized collection of data.",
            "network": "A group of interconnected computers.",
            "software": "Programs and operating systems used by computers.",
            "interface": "A point where two systems meet and interact.",
            "function": "A block of code that performs a specific task.",
            "variable": "A storage location with a symbolic name.",
            "debugging": "The process of finding and fixing errors.",
            "repository": "A storage location for software packages."
        }
        
        if words_file.exists():
            try:
                with open(words_file, 'r') as f:
                    words_data = json.load(f)
                    return words_data.get(self.difficulty, default_words)
            except (json.JSONDecodeError, IOError):
                return default_words
        
        return default_words
    
    def start_new_game(self) -> Tuple[str, str]:
        """
        Start a new game with a random word
        
        Returns:
            Tuple of (word, hint)
        """
        self.word_to_guess, self.hint = self._get_random_word_with_hint()
        self.guessed_letters = []
        self.incorrect_guesses = 0
        self.game_won = False
        self.game_lost = False
        return self.word_to_guess, self.hint
    
    def _get_random_word_with_hint(self) -> Tuple[str, str]:
        """Get a random word with its hint"""
        word, hint = random.choice(list(self.words_with_clues.items()))
        return word.lower(), hint
    
    def make_guess(self, letter: str) -> Dict:
        """
        Process a letter guess
        
        Args:
            letter: The guessed letter
            
        Returns:
            Dict with result information
        """
        letter = letter.lower()
        
        # Check if already guessed
        if letter in self.guessed_letters:
            return {
                "valid": False,
                "message": "Already guessed",
                "correct": False
            }
        
        self.guessed_letters.append(letter)
        
        # Check if letter is in word
        if letter in self.word_to_guess:
            # Check if word is complete
            if self.is_word_complete():
                self.game_won = True
                return {
                    "valid": True,
                    "correct": True,
                    "game_won": True,
                    "message": f"Congratulations! You've guessed the word: {self.word_to_guess}"
                }
            return {
                "valid": True,
                "correct": True,
                "game_won": False
            }
        else:
            self.incorrect_guesses += 1
            if self.incorrect_guesses >= self.max_incorrect_guesses:
                self.game_lost = True
                return {
                    "valid": True,
                    "correct": False,
                    "game_lost": True,
                    "message": f"Game Over! The word was: {self.word_to_guess}"
                }
            return {
                "valid": True,
                "correct": False,
                "game_lost": False
            }
    
    def get_display_word(self) -> str:
        """Get the current display state of the word"""
        return " ".join([
            letter if letter in self.guessed_letters else "_"
            for letter in self.word_to_guess
        ])
    
    def is_word_complete(self) -> bool:
        """Check if the word has been completely guessed"""
        return all(letter in self.guessed_letters for letter in self.word_to_guess)
    
    def get_game_state(self) -> Dict:
        """Get current game state"""
        return {
            "display_word": self.get_display_word(),
            "incorrect_guesses": self.incorrect_guesses,
            "max_incorrect_guesses": self.max_incorrect_guesses,
            "guessed_letters": self.guessed_letters,
            "hint": self.hint,
            "game_won": self.game_won,
            "game_lost": self.game_lost,
            "is_game_over": self.game_won or self.game_lost
        }
