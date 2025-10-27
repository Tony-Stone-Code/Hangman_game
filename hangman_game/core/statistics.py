"""
Statistics tracking for Hangman game
"""

import json
from pathlib import Path
from typing import Dict
from datetime import datetime


class Statistics:
    """Track game statistics"""
    
    def __init__(self):
        self.stats_file = Path.home() / ".hangman_stats.json"
        self.stats = self._load_stats()
    
    def _load_stats(self) -> Dict:
        """Load statistics from file"""
        default_stats = {
            "games_played": 0,
            "games_won": 0,
            "games_lost": 0,
            "total_guesses": 0,
            "best_streak": 0,
            "current_streak": 0,
            "by_difficulty": {
                "easy": {"played": 0, "won": 0},
                "medium": {"played": 0, "won": 0},
                "hard": {"played": 0, "won": 0}
            }
        }
        
        if self.stats_file.exists():
            try:
                with open(self.stats_file, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                return default_stats
        
        return default_stats
    
    def _save_stats(self):
        """Save statistics to file"""
        try:
            with open(self.stats_file, 'w') as f:
                json.dump(self.stats, f, indent=2)
        except IOError:
            pass
    
    def record_game(self, won: bool, difficulty: str = "medium", guesses: int = 0):
        """
        Record a game result
        
        Args:
            won: Whether the game was won
            difficulty: Game difficulty level
            guesses: Number of guesses made
        """
        self.stats["games_played"] += 1
        self.stats["total_guesses"] += guesses
        
        if won:
            self.stats["games_won"] += 1
            self.stats["current_streak"] += 1
            if self.stats["current_streak"] > self.stats["best_streak"]:
                self.stats["best_streak"] = self.stats["current_streak"]
        else:
            self.stats["games_lost"] += 1
            self.stats["current_streak"] = 0
        
        # Update difficulty stats
        if difficulty in self.stats["by_difficulty"]:
            self.stats["by_difficulty"][difficulty]["played"] += 1
            if won:
                self.stats["by_difficulty"][difficulty]["won"] += 1
        
        self._save_stats()
    
    def get_stats(self) -> Dict:
        """Get current statistics"""
        return self.stats.copy()
    
    def get_win_rate(self) -> float:
        """Get win rate percentage"""
        if self.stats["games_played"] == 0:
            return 0.0
        return (self.stats["games_won"] / self.stats["games_played"]) * 100
    
    def reset_stats(self):
        """Reset all statistics"""
        self.stats = {
            "games_played": 0,
            "games_won": 0,
            "games_lost": 0,
            "total_guesses": 0,
            "best_streak": 0,
            "current_streak": 0,
            "by_difficulty": {
                "easy": {"played": 0, "won": 0},
                "medium": {"played": 0, "won": 0},
                "hard": {"played": 0, "won": 0}
            }
        }
        self._save_stats()
