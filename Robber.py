"""
Robber Role Logic Module

This module defines the attributes and game path for the Robber role in the Wild West-themed train robbery game. The Robber role has a specific set of attribute statistics and follows a predefined order of minigames to progress through the game.

Attributes:
    - Lethality: 1 (C Grade) - The Robber has low lethality, making them less effective in fending off security guards.
    - Endurance: 2 (B Grade) - The Robber has moderate endurance, allowing them to sustain a few failures or physical damage during missions.
    - Dexterity: 4 (S Grade) - The Robber excels in dexterity, allowing them to perform tasks quickly and efficiently.
    - Intelligence: 1 (C Grade) - The Robber possesses low intelligence, making it challenging to attain a significant percentage of the money portion at the end of the game.

Game Path:
    The Robber role follows a specific order of minigames as part of the train robbery:
    1. Door Unlocking Minigame: The Robber specializes in unlocking doors to access the vault.
    2. Money Grab Minigame: Inside the vault, the Robber aims to steal as much money as possible within a limited number of turns. This minigame is repeated.

This module provides the attribute statistics and game path information necessary for gameplay as the Robber role.
"""


Attribute = [1, 2, 4, 1]
gamePath = ["doorUnlockMinigame", "moneyGrabMinigame", "moneyGrabMinigame"]