#Logic file for Gunner role

import random
import Game

Attribute = [4, 1, 1, 3]
roundOne = random.choice([Game.doorUnlockMinigame]* 3 + [Game.railroadBombMinigame])
roundTwo = random.choice([Game.doorUnlockMinigame]* 3 + [Game.securityMinigame])
roundThree = [Game.moneyGrabMinigame]