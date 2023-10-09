"""
Gunner Role Logic Module

This module defines the attributes and game path for the Gunner role in the Wild West-themed train robbery game. The Gunner role has a specific set of attribute statistics and follows a predefined order of minigames to progress through the game.

Attributes:
    - Lethality: 4 (S Grade) - The Gunner excels in lethality, making them proficient at fending off security guards.
    - Endurance: 1 (C Grade) - The Gunner has low endurance, meaning they can't sustain as many failures or physical damage during missions.
    - Dexterity: 1 (C Grade) - The Gunner's dexterity is low, affecting their minimum probability of dice rolls.
    - Intelligence: 3 (B Grade) - The Gunner possesses decent intelligence, allowing them to attain a fair percentage of the money portion at the end of the game.

Game Path:
    The Gunner role follows a specific order of minigames as part of the train robbery:
    1. Security Minigame: The Gunner faces off against security guards.
    2. Door Unlocking Minigame: The Gunner attempts to unlock doors to access the vault.
    3. Money Grab Minigame: Inside the vault, the Gunner aims to steal as much money as possible within a limited number of turns.

This module provides the attribute statistics and game path information necessary for gameplay as the Gunner role.
"""

Attribute = [4, 1, 1, 3]
gamePath = ["securityMinigame", "doorUnlockMinigame", "moneyGrabMinigame"]