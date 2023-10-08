#Logic file for Demolitioner role

import random

Attribute = [1, 4, 2, 4]
roundOne = random.choice(["doorUnlockMinigame"]* 3 + ["railroadBombMinigame"])
roundTwo = random.choice(["doorUnlockMinigame"]* 3 + ["securityMinigame"])
roundThree = ["moneyGrabMinigame"]
gamePath = [roundOne, roundTwo, roundThree]