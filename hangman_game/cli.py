#!/usr/bin/env python3
"""
Simple command-line version of Hangman game for systems without Tkinter
"""

from hangman_game.core.game_logic import HangmanLogic
from hangman_game.core.statistics import Statistics
from hangman_game.ui.hangman_art import get_hangman_stage


def clear_screen():
    """Clear the terminal screen"""
    import os
    os.system('clear' if os.name != 'nt' else 'cls')


def play_game_cli():
    """Play hangman game in command line"""
    print("\n" + "=" * 50)
    print("      🎮 WELCOME TO HANGMAN GAME! 🎮")
    print("=" * 50)
    
    # Select difficulty
    print("\nSelect difficulty:")
    print("1. Easy (8 wrong guesses)")
    print("2. Medium (6 wrong guesses)")
    print("3. Hard (4 wrong guesses)")
    
    while True:
        choice = input("\nEnter your choice (1-3): ").strip()
        if choice == "1":
            difficulty = "easy"
            break
        elif choice == "2":
            difficulty = "medium"
            break
        elif choice == "3":
            difficulty = "hard"
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
    
    # Initialize game
    game = HangmanLogic(difficulty=difficulty)
    stats = Statistics()
    word, hint = game.start_new_game()
    
    # Game loop
    while not game.game_won and not game.game_lost:
        clear_screen()
        
        # Display hangman
        art = get_hangman_stage(game.incorrect_guesses, game.max_incorrect_guesses)
        print(art)
        
        # Display game state
        print(f"\n{'=' * 50}")
        print(f"Difficulty: {difficulty.capitalize()}")
        print(f"💡 Hint: {hint}")
        print(f"\nWord: {game.get_display_word()}")
        print(f"❌ Wrong guesses: {game.incorrect_guesses}/{game.max_incorrect_guesses}")
        
        if game.guessed_letters:
            print(f"Letters guessed: {', '.join(sorted(game.guessed_letters))}")
        
        print(f"{'=' * 50}")
        
        # Get guess
        while True:
            guess = input("\nGuess a letter: ").strip().lower()
            if len(guess) == 1 and guess.isalpha():
                break
            print("Please enter a single letter.")
        
        # Process guess
        result = game.make_guess(guess)
        
        if not result["valid"]:
            print("\n⚠️  You already guessed that letter!")
            input("Press Enter to continue...")
            continue
        
        if result["correct"]:
            print("\n✓ Correct!")
        else:
            print("\n✗ Wrong guess!")
        
        input("Press Enter to continue...")
    
    # Game over
    clear_screen()
    art = get_hangman_stage(game.incorrect_guesses, game.max_incorrect_guesses)
    print(art)
    print(f"\n{'=' * 50}")
    
    if game.game_won:
        print("🎉 CONGRATULATIONS! YOU WON! 🎉")
        print(f"\nThe word was: {game.word_to_guess.upper()}")
        print(f"You guessed it with {game.incorrect_guesses} wrong guesses!")
        stats.record_game(won=True, difficulty=difficulty, guesses=len(game.guessed_letters))
    else:
        print("😢 GAME OVER - YOU LOST! 😢")
        print(f"\nThe word was: {game.word_to_guess.upper()}")
        stats.record_game(won=False, difficulty=difficulty, guesses=len(game.guessed_letters))
    
    print(f"{'=' * 50}")
    
    # Show stats
    stats_data = stats.get_stats()
    win_rate = stats.get_win_rate()
    print("\n📊 Your Statistics:")
    print(f"  Games played: {stats_data['games_played']}")
    print(f"  Win rate: {win_rate:.1f}%")
    print(f"  Current streak: {stats_data['current_streak']}")
    
    # Play again?
    print("\n" + "=" * 50)
    play_again = input("\nPlay again? (y/n): ").strip().lower()
    if play_again == 'y':
        play_game_cli()
    else:
        print("\nThanks for playing! Goodbye! 👋")


def main():
    """Main entry point for CLI version"""
    try:
        play_game_cli()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Thanks for playing! 👋")
    except Exception as e:
        print(f"\n\nAn error occurred: {e}")


if __name__ == "__main__":
    main()
