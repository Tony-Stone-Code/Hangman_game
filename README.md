# 🎮 Hangman Game

A feature-rich and user-friendly Hangman word guessing game with a modern graphical user interface (GUI), built with Python's Tkinter library.

## ✨ Features

### Core Gameplay
- 🎯 Random word selection from an extensive word list
- 💡 Helpful hints for each word
- 🎨 Visual hangman ASCII art that updates with each wrong guess
- ⌨️ Keyboard and mouse input support
- 🔄 Easy game reset functionality

### Enhanced UX
- 🎚️ **Three Difficulty Levels**: Easy (8 mistakes), Medium (6 mistakes), Hard (4 mistakes)
- 📊 **Statistics Tracking**: Track your games played, won, lost, win rate, and streaks
- 🎭 **Visual Feedback**: Color-coded buttons and real-time status updates
- 📈 **Performance Analytics**: See your performance by difficulty level
- 🎨 **Modern UI**: Clean, intuitive interface with emoji icons
- 🎹 **Keyboard Support**: Type letters directly without clicking buttons

### Word Categories
- **Easy**: Common everyday words (20+ words)
- **Medium**: Programming and tech-related terms (20+ words)
- **Hard**: Advanced technical terminology (20+ words)

## 📋 Requirements

- Python 3.7 or higher
- Tkinter (usually included with Python installations)

## 🚀 Installation

### Method 1: Install from PyPI (Recommended)
Once published to PyPI, you can install with:
```bash
pip install hangman-game
```

### Method 2: Install from Source
1. **Clone the repository:**
   ```bash
   git clone https://github.com/Tony-Stone-Code/Hangman_game
   cd Hangman_game
   ```

2. **Install the package:**
   ```bash
   pip install .
   ```

   Or for development mode:
   ```bash
   pip install -e .
   ```

### Method 3: Install from GitHub directly
```bash
pip install git+https://github.com/Tony-Stone-Code/Hangman_game.git
```

## 🎮 How to Play

### Starting the Game

After installation, you can start the game in multiple ways:

1. **From command line (after installation):**
   ```bash
   hangman
   ```

2. **As a Python module:**
   ```bash
   python -m hangman_game
   ```

3. **From Python code:**
   ```python
   from hangman_game.ui.gui import main
   main()
   ```

### Game Rules

1. **Choose your difficulty**: Select Easy, Medium, or Hard before starting
2. **Guess letters**: Click on letter buttons or type on your keyboard
3. **Use the hint**: Read the hint to help you guess the word
4. **Watch the hangman**: The hangman drawing updates with each wrong guess
5. **Win condition**: Guess all letters before running out of attempts
6. **Track your progress**: View your statistics anytime

### Controls

- **Mouse**: Click letter buttons to make guesses
- **Keyboard**: Type any letter (a-z) to make a guess
- **New Game Button**: Start a fresh game
- **Statistics Button**: View your game statistics
- **Difficulty Selector**: Change difficulty level

## 📊 Statistics

The game automatically tracks:
- Total games played
- Games won and lost
- Win rate percentage
- Current winning streak
- Best winning streak
- Performance by difficulty level

Statistics are saved locally in your home directory (`~/.hangman_stats.json`).

## 🛠️ Development

### Project Structure
```
Hangman_game/
├── hangman_game/
│   ├── __init__.py
│   ├── __main__.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── game_logic.py    # Core game logic
│   │   └── statistics.py     # Statistics tracking
│   ├── ui/
│   │   ├── __init__.py
│   │   ├── gui.py            # GUI implementation
│   │   └── hangman_art.py    # ASCII art
│   └── data/
│       ├── __init__.py
│       └── words.json         # Word database
├── setup.py
├── pyproject.toml
├── MANIFEST.in
├── README.md
└── LICENSE
```

### Running Tests
```bash
# Run the game in development mode
python -m hangman_game

# Or directly
python hangman_game/ui/gui.py
```

### Adding Custom Words

You can add your own words by editing the `hangman_game/data/words.json` file:

```json
{
  "medium": {
    "yourword": "Your hint for this word.",
    ...
  }
}
```

## 🤝 Contributing

Contributions are welcome! Here are some ways you can contribute:

1. Report bugs
2. Suggest new features
3. Add more words to the word database
4. Improve documentation
5. Submit pull requests

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🎯 Future Enhancements

Potential features for future versions:
- Sound effects (with mute option)
- Multiplayer mode
- Custom word lists
- Themes and skins
- Timed mode
- Score system
- Online leaderboards

## 👨‍💻 Author

**Tony Stone**

## 🙏 Acknowledgments

- Built with Python and Tkinter
- Inspired by the classic Hangman word game

---

**Enjoy playing Hangman! 🎮**

If you like this game, please give it a ⭐ on GitHub!
