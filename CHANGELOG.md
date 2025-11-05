# Changelog

All notable changes to the Hangman Game will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-10-27

### Added
- **Installable Python package** with proper setup.py and pyproject.toml
- **Three difficulty levels**: Easy (8 mistakes), Medium (6 mistakes), Hard (4 mistakes)
- **Statistics tracking system**:
  - Games played, won, and lost
  - Win rate calculation
  - Current and best winning streaks
  - Performance breakdown by difficulty level
- **Enhanced visual feedback**:
  - ASCII art hangman drawing that updates with each wrong guess
  - Color-coded letter buttons (blue → green/gray based on guess)
  - Status bar with real-time feedback
  - Emoji icons throughout the UI
- **Keyboard input support**: Type letters directly without clicking buttons
- **Expanded word database**: 60+ words across three difficulty levels
- **Modular code structure**:
  - Separated game logic from UI
  - Core game logic module
  - Statistics tracking module
  - UI components module
- **Professional packaging**:
  - Entry point for command-line execution (`hangman` command)
  - Module execution support (`python -m hangman_game`)
  - Proper package metadata and dependencies
  - MANIFEST.in for including data files
  - .gitignore for Python projects

### Changed
- Reorganized code from single file to modular package structure
- Improved UI layout and styling with better colors and spacing
- Enhanced button layout from 5 columns to 9 columns for better visibility
- Updated README with comprehensive installation and usage instructions

### Technical Improvements
- Separated concerns: game logic, UI, and data
- Added proper error handling
- Implemented statistics persistence
- Added configuration support through JSON files
- Better code documentation and comments

## [0.1.0] - Initial Release

### Features
- Basic Hangman game with Tkinter GUI
- Random word selection
- Letter guessing with button interface
- Basic hint system
- Game reset functionality
