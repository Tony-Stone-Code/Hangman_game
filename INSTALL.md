# Installation Guide for Hangman Game

## Quick Start

The easiest way to install and run Hangman Game:

```bash
# Install the package
pip install hangman-game

# Run the GUI version (requires Tkinter)
hangman

# Or run the CLI version (no GUI required)
hangman-cli
```

## Detailed Installation Instructions

### Prerequisites

- **Python 3.7 or higher** - Check your version:
  ```bash
  python --version
  # or
  python3 --version
  ```

- **Tkinter** (for GUI version only) - Usually comes with Python, but if needed:
  - **Ubuntu/Debian**: `sudo apt-get install python3-tk`
  - **Fedora**: `sudo dnf install python3-tkinter`
  - **macOS**: Included with Python from python.org
  - **Windows**: Included with official Python installer

### Installation Methods

#### Method 1: Install from PyPI (Recommended when published)

```bash
pip install hangman-game
```

#### Method 2: Install from GitHub

```bash
pip install git+https://github.com/Tony-Stone-Code/Hangman_game.git
```

#### Method 3: Install from Source

1. Clone the repository:
   ```bash
   git clone https://github.com/Tony-Stone-Code/Hangman_game.git
   cd Hangman_game
   ```

2. Install the package:
   ```bash
   pip install .
   ```

   For development (editable) mode:
   ```bash
   pip install -e .
   ```

#### Method 4: Run without Installation

If you prefer not to install the package:

```bash
# Clone the repository
git clone https://github.com/Tony-Stone-Code/Hangman_game.git
cd Hangman_game

# Run as a module
python -m hangman_game

# Or run the CLI version directly
python hangman_game/cli.py
```

### Verifying Installation

After installation, verify it works:

```bash
# Check if commands are available
which hangman
which hangman-cli

# Try importing the module
python -c "from hangman_game.core.game_logic import HangmanLogic; print('✓ Installation successful')"
```

## Usage

### GUI Version

The GUI version provides a beautiful graphical interface:

```bash
# Start the game
hangman

# Or as a Python module
python -m hangman_game

# Or from Python code
python -c "from hangman_game.ui.gui import main; main()"
```

**Features:**
- Click buttons or use keyboard to guess letters
- Three difficulty levels
- Visual hangman drawing
- Statistics tracking
- Hints for each word

### CLI Version

The CLI version works in any terminal without Tkinter:

```bash
# Start the CLI version
hangman-cli

# Or run directly
python -m hangman_game.cli
```

**Features:**
- Pure text-based interface
- ASCII art hangman
- Same gameplay and difficulty levels
- Statistics tracking
- Works on any system with Python

## Troubleshooting

### "No module named 'tkinter'" Error

If you get this error when running the GUI version:

1. **Try the CLI version instead**: `hangman-cli`
2. **Install Tkinter**:
   - Ubuntu/Debian: `sudo apt-get install python3-tk`
   - Fedora: `sudo dnf install python3-tkinter`
   - macOS: Reinstall Python from python.org
   - Windows: Reinstall Python and check "tcl/tk and IDLE" option

### Permission Denied

If you get permission errors during installation:

```bash
# Use --user flag to install in user directory
pip install --user hangman-game

# Or use a virtual environment
python -m venv hangman_env
source hangman_env/bin/activate  # On Windows: hangman_env\Scripts\activate
pip install hangman-game
```

### Command Not Found

If `hangman` or `hangman-cli` commands are not found:

1. Make sure pip's bin directory is in your PATH
2. Find where the commands are installed:
   ```bash
   pip show -f hangman-game | grep hangman
   ```
3. Run directly using Python:
   ```bash
   python -m hangman_game.ui.gui  # GUI version
   python -m hangman_game.cli     # CLI version
   ```

## Uninstallation

To remove the game:

```bash
pip uninstall hangman-game
```

Note: This will not remove your statistics file (`~/.hangman_stats.json`). You can manually delete it if desired.

## Updating

To update to the latest version:

```bash
# From PyPI
pip install --upgrade hangman-game

# From GitHub
pip install --upgrade git+https://github.com/Tony-Stone-Code/Hangman_game.git
```

## Platform-Specific Notes

### Windows

- Use `python` instead of `python3`
- Use backslashes in paths or forward slashes
- GUI version should work out of the box with official Python installer

### macOS

- Python 3 from python.org includes Tkinter
- Homebrew Python may need: `brew install python-tk`

### Linux

- Most distributions need separate Tkinter package
- CLI version is a good alternative if Tkinter installation is problematic

## Getting Help

If you encounter issues:

1. Check the [README.md](README.md) for general information
2. Look at [CHANGELOG.md](CHANGELOG.md) for recent changes
3. Open an issue on [GitHub](https://github.com/Tony-Stone-Code/Hangman_game/issues)

## Next Steps

After installation, check out:
- The main [README.md](README.md) for features and game rules
- [CHANGELOG.md](CHANGELOG.md) for version history
- The game's built-in statistics feature to track your progress!

Enjoy playing Hangman! 🎮
