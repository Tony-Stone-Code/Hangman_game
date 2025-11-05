"""
Hangman visual representations (ASCII art)
"""

HANGMAN_STAGES = [
    # Stage 0 - No wrong guesses
    """
       ________
       |      |
       |
       |
       |
       |
    ___|___
    """,
    # Stage 1
    """
       ________
       |      |
       |      O
       |
       |
       |
    ___|___
    """,
    # Stage 2
    """
       ________
       |      |
       |      O
       |      |
       |
       |
    ___|___
    """,
    # Stage 3
    """
       ________
       |      |
       |      O
       |     /|
       |
       |
    ___|___
    """,
    # Stage 4
    """
       ________
       |      |
       |      O
       |     /|\\
       |
       |
    ___|___
    """,
    # Stage 5
    """
       ________
       |      |
       |      O
       |     /|\\
       |     /
       |
    ___|___
    """,
    # Stage 6 - Game over
    """
       ________
       |      |
       |      O
       |     /|\\
       |     / \\
       |
    ___|___
    """
]

# Extended stages for easy mode (8 wrong guesses)
HANGMAN_STAGES_EASY = [
    # Stage 0 - No wrong guesses
    """
       ________
       |      |
       |
       |
       |
       |
    ___|___
    """,
    # Stage 1 - Head
    """
       ________
       |      |
       |      O
       |
       |
       |
    ___|___
    """,
    # Stage 2 - Body start
    """
       ________
       |      |
       |      O
       |      |
       |
       |
    ___|___
    """,
    # Stage 3 - Left arm
    """
       ________
       |      |
       |      O
       |     /|
       |
       |
    ___|___
    """,
    # Stage 4 - Right arm
    """
       ________
       |      |
       |      O
       |     /|\\
       |
       |
    ___|___
    """,
    # Stage 5 - Body complete
    """
       ________
       |      |
       |      O
       |     /|\\
       |      |
       |
    ___|___
    """,
    # Stage 6 - Left leg
    """
       ________
       |      |
       |      O
       |     /|\\
       |      |
       |     /
    ___|___
    """,
    # Stage 7 - Right leg start
    """
       ________
       |      |
       |      O
       |     /|\\
       |      |
       |     / \\
    ___|___
    """,
    # Stage 8 - Game over
    """
       ________
       |      |
       |      X
       |     /|\\
       |      |
       |     / \\
    ___|___
    """
]

# Compact stages for hard mode (4 wrong guesses)
HANGMAN_STAGES_HARD = [
    # Stage 0
    """
       ________
       |      |
       |
       |
    ___|___
    """,
    # Stage 1
    """
       ________
       |      |
       |      O
       |
    ___|___
    """,
    # Stage 2
    """
       ________
       |      |
       |      O
       |     /|\\
    ___|___
    """,
    # Stage 3
    """
       ________
       |      |
       |      O
       |     /|\\
       |     /
    ___|___
    """,
    # Stage 4
    """
       ________
       |      |
       |      O
       |     /|\\
       |     / \\
    ___|___
    """
]


def get_hangman_stage(incorrect_guesses: int, max_guesses: int = 6) -> str:
    """
    Get the hangman ASCII art for the current number of incorrect guesses
    
    Args:
        incorrect_guesses: Number of incorrect guesses
        max_guesses: Maximum number of incorrect guesses allowed
        
    Returns:
        ASCII art string for the hangman
    """
    if max_guesses == 8:
        stages = HANGMAN_STAGES_EASY
    elif max_guesses == 4:
        stages = HANGMAN_STAGES_HARD
    else:
        stages = HANGMAN_STAGES
    
    # Ensure we don't go out of bounds
    index = min(incorrect_guesses, len(stages) - 1)
    return stages[index]
