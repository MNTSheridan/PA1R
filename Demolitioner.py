"""
Demolitioner Role Logic Module

This module defines the attributes and game path for the Demolitioner role in the Wild West-themed train robbery game. The Demolitioner role has a specific set of attribute statistics and follows a predefined order of minigames to progress through the game.

Attributes:
    - Lethality: 1 (C Grade) - The Demolitioner has low lethality, making them less effective in fending off security guards.
    - Endurance: 4 (S Grade) - The Demolitioner possesses high endurance, allowing them to sustain multiple failures, mistakes, or physical damage during missions.
    - Dexterity: 2 (B Grade) - The Demolitioner has moderate dexterity, which affects their speed in completing tasks.
    - Intelligence: 4 (S Grade) - The Demolitioner has high intelligence, enabling them to attain a significant percentage of the money portion at the end of the game.

Game Path:
    The Demolitioner role follows a specific order of minigames as part of the train robbery:
    1. Railroad Bombing Minigame: The Demolitioner excels in setting up dynamite on the train tracks to halt the train.
    2. Security Minigame: The Demolitioner encounters security guards and must defeat them.
    3. Money Grab Minigame: Inside the vault, the Demolitioner aims to steal as much money as possible.

This module provides the attribute statistics and game path information necessary for gameplay as the Demolitioner role.
"""

Attribute = [1, 4, 2, 4]
gamePath = ["railroadBombMinigame", "securityMinigame", "moneyGrabMinigame"]