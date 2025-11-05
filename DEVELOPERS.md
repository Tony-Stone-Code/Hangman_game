# Developer Guide

## Project Structure

```
Hangman_game/
├── hangman_game/           # Main package
│   ├── __init__.py         # Package metadata
│   ├── __main__.py         # Module entry point
│   ├── cli.py              # CLI version
│   ├── core/               # Core game logic
│   │   ├── __init__.py
│   │   ├── game_logic.py   # Game logic (no UI dependencies)
│   │   └── statistics.py   # Statistics tracking
│   ├── ui/                 # User interface
│   │   ├── __init__.py
│   │   ├── gui.py          # Tkinter GUI
│   │   └── hangman_art.py  # ASCII art
│   └── data/               # Game data
│       ├── __init__.py
│       └── words.json      # Word database
├── tests/                  # Test files
│   ├── __init__.py
│   └── test_game.py        # Unit tests
├── setup.py                # Package setup (setuptools)
├── pyproject.toml          # Modern Python packaging
├── MANIFEST.in             # Additional files to include
├── README.md               # User documentation
├── INSTALL.md              # Installation guide
├── CHANGELOG.md            # Version history
└── .gitignore              # Git ignore rules
```

## Development Setup

### 1. Clone and Setup

```bash
# Clone the repository
git clone https://github.com/Tony-Stone-Code/Hangman_game.git
cd Hangman_game

# Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e .
```

### 2. Running Tests

```bash
# Run all tests
python tests/test_game.py

# Or with pytest (if installed)
pytest tests/
```

### 3. Running the Application

```bash
# GUI version
python -m hangman_game
# or
hangman

# CLI version
python hangman_game/cli.py
# or
hangman-cli
```

## Code Architecture

### Core Components

#### 1. Game Logic (`core/game_logic.py`)

The `HangmanLogic` class contains all game logic without UI dependencies:

```python
from hangman_game.core.game_logic import HangmanLogic

game = HangmanLogic(difficulty="medium")
word, hint = game.start_new_game()
result = game.make_guess("a")
state = game.get_game_state()
```

**Key methods:**
- `start_new_game()` - Initialize a new game
- `make_guess(letter)` - Process a guess
- `get_display_word()` - Get current word state
- `get_game_state()` - Get complete game state

#### 2. Statistics (`core/statistics.py`)

The `Statistics` class tracks game performance:

```python
from hangman_game.core.statistics import Statistics

stats = Statistics()
stats.record_game(won=True, difficulty="medium", guesses=5)
stats_data = stats.get_stats()
win_rate = stats.get_win_rate()
```

#### 3. GUI (`ui/gui.py`)

Tkinter-based graphical interface:
- Event handling for button clicks
- Keyboard input support
- Visual feedback
- Statistics display

#### 4. CLI (`cli.py`)

Terminal-based interface:
- No Tkinter dependency
- ASCII art display
- Keyboard input
- Same core functionality

### Data Files

#### Words Database (`data/words.json`)

JSON structure:
```json
{
  "easy": {
    "word": "hint for the word",
    ...
  },
  "medium": {...},
  "hard": {...}
}
```

**Adding new words:**
1. Edit `hangman_game/data/words.json`
2. Add entries in the appropriate difficulty level
3. Format: `"word": "Hint description"`

### Statistics Storage

Statistics are saved in `~/.hangman_stats.json`:
```json
{
  "games_played": 0,
  "games_won": 0,
  "games_lost": 0,
  "total_guesses": 0,
  "best_streak": 0,
  "current_streak": 0,
  "by_difficulty": {...}
}
```

## Building and Distribution

### Build Distribution Packages

```bash
# Clean previous builds
rm -rf build dist *.egg-info

# Build wheel and source distribution
python setup.py sdist bdist_wheel

# Check the built packages
ls -lh dist/
```

### Install from Built Package

```bash
# Install the wheel file
pip install dist/hangman_game-1.0.0-py3-none-any.whl

# Or install from source tarball
pip install dist/hangman-game-1.0.0.tar.gz
```

### Testing the Package

```bash
# Install in a fresh virtual environment
python3 -m venv test_env
source test_env/bin/activate
pip install dist/hangman_game-1.0.0-py3-none-any.whl

# Test the commands
hangman --help
hangman-cli

# Test module import
python -c "from hangman_game.core.game_logic import HangmanLogic; print('OK')"

# Deactivate when done
deactivate
```

## Making Changes

### Adding New Features

1. **Add core logic** in `hangman_game/core/`
2. **Update UI** in `hangman_game/ui/gui.py` and/or `hangman_game/cli.py`
3. **Add tests** in `tests/test_game.py`
4. **Update documentation** in README.md and CHANGELOG.md

### Adding New Words

Edit `hangman_game/data/words.json`:
```json
{
  "medium": {
    "newword": "Your hint for the new word",
    ...
  }
}
```

### Code Style

- Follow PEP 8 guidelines
- Use meaningful variable names
- Add docstrings to functions and classes
- Keep functions focused and small
- Separate UI from logic

### Testing Checklist

Before committing:
- [ ] Run all tests: `python tests/test_game.py`
- [ ] Test GUI version: `python -m hangman_game`
- [ ] Test CLI version: `python hangman_game/cli.py`
- [ ] Verify package builds: `python setup.py sdist bdist_wheel`
- [ ] Check for typos in documentation
- [ ] Update CHANGELOG.md

## Publishing

### To PyPI (when ready)

```bash
# Install build tools
pip install build twine

# Build the package
python -m build

# Upload to TestPyPI first
python -m twine upload --repository testpypi dist/*

# Test installation from TestPyPI
pip install --index-url https://test.pypi.org/simple/ hangman-game

# If all looks good, upload to PyPI
python -m twine upload dist/*
```

## Common Tasks

### Add a new difficulty level

1. Update `_get_max_incorrect_guesses()` in `game_logic.py`
2. Add words in `data/words.json`
3. Update UI to include new option
4. Add test cases

### Change the hangman art

Edit `hangman_game/ui/hangman_art.py`:
- Modify `HANGMAN_STAGES` for medium
- Modify `HANGMAN_STAGES_EASY` for easy
- Modify `HANGMAN_STAGES_HARD` for hard

### Add sound effects

1. Add sound files to `hangman_game/data/`
2. Update MANIFEST.in to include sound files
3. Add sound playing logic in GUI/CLI
4. Make it optional with a mute toggle

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests
5. Submit a pull request

## License

See LICENSE file for details.

## Questions?

Open an issue on GitHub or check the documentation!
