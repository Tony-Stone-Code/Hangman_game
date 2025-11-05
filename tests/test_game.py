"""
Basic tests for Hangman game logic
"""

import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from hangman_game.core.game_logic import HangmanLogic
from hangman_game.core.statistics import Statistics


def test_game_initialization():
    """Test game initialization"""
    print("Testing game initialization...")
    game = HangmanLogic(difficulty="medium")
    assert game.difficulty == "medium"
    assert game.max_incorrect_guesses == 6
    assert len(game.guessed_letters) == 0
    assert game.incorrect_guesses == 0
    print("✓ Game initialization test passed")


def test_difficulty_levels():
    """Test different difficulty levels"""
    print("\nTesting difficulty levels...")
    
    easy = HangmanLogic(difficulty="easy")
    assert easy.max_incorrect_guesses == 8
    
    medium = HangmanLogic(difficulty="medium")
    assert medium.max_incorrect_guesses == 6
    
    hard = HangmanLogic(difficulty="hard")
    assert hard.max_incorrect_guesses == 4
    
    print("✓ Difficulty levels test passed")


def test_start_new_game():
    """Test starting a new game"""
    print("\nTesting new game start...")
    game = HangmanLogic()
    word, hint = game.start_new_game()
    assert len(word) > 0
    assert len(hint) > 0
    assert len(game.guessed_letters) == 0
    assert game.incorrect_guesses == 0
    print(f"✓ New game started with word: {word}")


def test_correct_guess():
    """Test making a correct guess"""
    print("\nTesting correct guess...")
    game = HangmanLogic()
    word, hint = game.start_new_game()
    
    # Guess the first letter of the word
    first_letter = word[0]
    result = game.make_guess(first_letter)
    
    assert result["valid"] == True
    assert result["correct"] == True
    assert first_letter in game.guessed_letters
    assert game.incorrect_guesses == 0
    print(f"✓ Correct guess test passed (guessed: {first_letter})")


def test_incorrect_guess():
    """Test making an incorrect guess"""
    print("\nTesting incorrect guess...")
    game = HangmanLogic()
    word, hint = game.start_new_game()
    
    # Find a letter not in the word
    for letter in "xyz":
        if letter not in word:
            result = game.make_guess(letter)
            assert result["valid"] == True
            assert result["correct"] == False
            assert letter in game.guessed_letters
            assert game.incorrect_guesses == 1
            print(f"✓ Incorrect guess test passed (guessed: {letter})")
            break


def test_duplicate_guess():
    """Test guessing the same letter twice"""
    print("\nTesting duplicate guess...")
    game = HangmanLogic()
    word, hint = game.start_new_game()
    
    first_letter = word[0]
    game.make_guess(first_letter)
    result = game.make_guess(first_letter)
    
    assert result["valid"] == False
    assert result["message"] == "Already guessed"
    print("✓ Duplicate guess test passed")


def test_display_word():
    """Test display word generation"""
    print("\nTesting display word...")
    game = HangmanLogic()
    game.word_to_guess = "python"
    game.guessed_letters = ["p", "y"]
    
    display = game.get_display_word()
    assert display == "p y _ _ _ _"
    print(f"✓ Display word test passed: {display}")


def test_word_complete():
    """Test word completion check"""
    print("\nTesting word completion...")
    game = HangmanLogic()
    game.word_to_guess = "cat"
    game.guessed_letters = ["c", "a", "t"]
    
    assert game.is_word_complete() == True
    print("✓ Word completion test passed")


def test_statistics():
    """Test statistics tracking"""
    print("\nTesting statistics...")
    stats = Statistics()
    
    initial_played = stats.stats["games_played"]
    stats.record_game(won=True, difficulty="medium", guesses=5)
    
    assert stats.stats["games_played"] == initial_played + 1
    assert stats.stats["current_streak"] >= 1
    print("✓ Statistics test passed")


def test_game_state():
    """Test game state retrieval"""
    print("\nTesting game state...")
    game = HangmanLogic()
    word, hint = game.start_new_game()
    
    state = game.get_game_state()
    assert "display_word" in state
    assert "incorrect_guesses" in state
    assert "guessed_letters" in state
    assert "hint" in state
    assert state["is_game_over"] == False
    print("✓ Game state test passed")


def run_all_tests():
    """Run all tests"""
    print("=" * 50)
    print("Running Hangman Game Tests")
    print("=" * 50)
    
    try:
        test_game_initialization()
        test_difficulty_levels()
        test_start_new_game()
        test_correct_guess()
        test_incorrect_guess()
        test_duplicate_guess()
        test_display_word()
        test_word_complete()
        test_statistics()
        test_game_state()
        
        print("\n" + "=" * 50)
        print("✅ All tests passed!")
        print("=" * 50)
        return True
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        return False
    except Exception as e:
        print(f"\n❌ Error during testing: {e}")
        return False


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
