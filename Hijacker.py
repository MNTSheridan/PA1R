#Logic file for Hijacker role

import random
import Game

Attribute = [1, 1, 4, 2]
roundOne = random.choice([Game.doorUnlockMinigame]* 3 + [Game.railroadBombMinigame])
roundTwo = random.choice([Game.doorUnlockMinigame]* 3 + [Game.securityMinigame])
roundThree = [Game.moneyGrabMinigame]
gamePath = [roundOne, roundTwo, roundThree]