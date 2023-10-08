#Logic file for robber role

import random
import Game

Attribute = [1, 2, 4, 1]
roundOne = random.choice([Game.doorUnlockMinigame]* 3 + [Game.railroadBombMinigame])
roundTwo = random.choice([Game.doorUnlockMinigame]* 3 + [Game.securityMinigame])
roundThree = [Game.moneyGrabMinigame]