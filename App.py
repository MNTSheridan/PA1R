"""
Train Robbery Game Main Module

This module serves as the main entry point for the train robbery game. It interacts with the Game module to provide gameplay functionality.
Players can choose their character role and experience a sequence of minigames as they attempt a train heist in the Wild West.

GitHub Repository:
   - Repository Link: https://github.com/MNTSheridan/PROGassignment1

Usage:
   - Ensure that your Git username and email are configured using the provided commands.
   - Run the game by executing this module.
   - Players will select their character role and progress through various minigames.

Functions:
   - menuSection(): Initializes the menu, allowing players to choose their character role and receive their starter attribute statistics.
   - minigameSection(): Progresses through the selected character's game path, including multiple minigames.

This module connects to the Game module to provide an interactive train robbery experience for players.
"""

import Game

# Initialize the menu and start the game
Game.menuSection()
Game.minigameSection()