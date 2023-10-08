#Logic file for Demolitioner role

import random
import Game

Attribute = [1, 4, 2, 4]
roundOne = random.choice([Game.doorUnlockMinigame]* 3 + [Game.railroadBombMinigame])
roundTwo = random.choice([Game.doorUnlockMinigame]* 3 + [Game.securityMinigame])
roundThree = [Game.moneyGrabMinigame]