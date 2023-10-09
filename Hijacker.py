"""
Hijacker Role Logic Module

This module defines the attributes and game path for the Hijacker role in the Wild West-themed train robbery game. The Hijacker role has a specific set of attribute statistics and follows a predefined order of minigames to progress through the game.

Attributes:
    - Lethality: 1 (C Grade) - The Hijacker has low lethality, making them less effective in fending off security guards.
    - Endurance: 1 (C Grade) - The Hijacker has low endurance, meaning they can't sustain many failures or physical damage during missions.
    - Dexterity: 4 (S Grade) - The Hijacker excels in dexterity, allowing them to perform tasks quickly and efficiently.
    - Intelligence: 2 (B Grade) - The Hijacker possesses decent intelligence, allowing them to attain a fair percentage of the money portion at the end of the game.

Game Path:
    The Hijacker role follows a specific order of minigames as part of the train robbery:
    1. Railroad Bomb Minigame: The Hijacker attempts to set up dynamite on the train tracks to force the train to halt.
    2. Door Unlocking Minigame: The Hijacker tries to unlock doors to access the vault.
    3. Money Grab Minigame: Inside the vault, the Hijacker aims to steal as much money as possible within a limited number of turns.

This module provides the attribute statistics and game path information necessary for gameplay as the Hijacker role.
"""

Attribute = [1, 1, 4, 2]
gamePath = ["railroadBombMinigame", "doorUnlockMinigame", "moneyGrabMinigame"]