from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="hangman-game",
    version="1.0.0",
    author="Tony Stone",
    author_email="",
    description="A feature-rich Hangman word guessing game with GUI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Tony-Stone-Code/Hangman_game",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Games/Entertainment :: Puzzle Games",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        # No external dependencies - uses tkinter which comes with Python
    ],
    entry_points={
        "console_scripts": [
            "hangman=hangman_game.ui.gui:main",
            "hangman-cli=hangman_game.cli:main",
        ],
    },
    package_data={
        "hangman_game": [
            "data/*.json",
        ],
    },
    keywords="hangman game puzzle word-game tkinter gui",
    project_urls={
        "Bug Reports": "https://github.com/Tony-Stone-Code/Hangman_game/issues",
        "Source": "https://github.com/Tony-Stone-Code/Hangman_game",
    },
)
