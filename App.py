import Game
import random
#link to GIT repository: https://github.com/MNTSheridan/PROGassignment1
#interactivity file
'''
git config user.name "MNTSheridan"
git config user.email "tran172@sheridancollege.ca"
'''
menuMessage = '''
It is the year 1872, you and your band of cowboys are the wild west's most notorious ciminal organization in the midwest, 
you and your pals plan for a train robbery... Choose your role!
\nA. Hijacker, you are responsible with hijacking doors (Unlocking doors are faster with this class)
\nB. Robber, you are a responsible for collecting money (Money rewards are higher with this class)
\nC. Gunner, you are responsible for fending off train security guards.
\nD. Demolitioner, you are responsible for unlocking vaults and you have enhanced endurance. 
\n\nChoice: '''

classStatConfiguration = {
    "A":("Hijacker", [1, 1, 4, 2]),     #8
    "B":("Robber", [1, 2, 4, 1]),       #8
    "C":("Gunner", [4, 1, 1, 3]),       #9
    "D":("Demolitioner", [1, 4, 2, 4])  #11
}

# self.allAttribute = attribute
# self.lethality = attribute[0]
# self.endurance = attribute[1]
# self.dexterity = attribute[2]
# self.intelligence = attribute[3]

global characterAttribute
characterAttribute = None

#This function initializes the menu, this is where the player chooses their character role and recieves their starter attribute statistics. 
def menuSection():
    global characterAttribute
    menuOption = input(menuMessage)
    if menuOption in ("A", "B", "C", "D"):
        #characterClass is variable that contains the attribute stats of the player
        characterClass = classStatConfiguration[menuOption][0]
        print(f"You chose {characterClass}!")
        characterAttribute = Game.playerInfo(classStatConfiguration[menuOption][1])
        print(characterAttribute._stat)
        print(f"Your attribute grades are presented in the order of: \nLethality, Endurance, Dexterity, and Intelligence: {characterAttribute.attributeGrade()} \nThose stats will increase/decrease according to how you play the game. (S grade stat will be at max capacity and cannot be increased)")
    

    else:
        print("You better pick an option!")
        menuSection()


def railroadBombMinigame(attributeInformation):
    endurance = attributeInformation._endurance
    dexterity = attributeInformation._dexterity

def securityMinigame(attributeInformation):
    endurance = attributeInformation._endurance
    lethality = attributeInformation._lethality

def doorUnlockMinigame(attributeInformation):
    endurance = attributeInformation._endurance
    dexterity = attributeInformation._dexterity

def moneyGrabMinigame(attributeInformation):
    endurance = attributeInformation._endurance
    dexterity = attributeInformation._dexterity


def minigameSection(attributeInformation):
    endurance = attributeInformation._endurance
    dexterity = attributeInformation._dexterity

    roundOne = random.choice([doorUnlockMinigame(attributeInformation)]* 3 + [railroadBombMinigame(attributeInformation)])
    roundTwo = random.choice([doorUnlockMinigame(attributeInformation)]* 3 + [securityMinigame(attributeInformation)])
    roundThree = moneyGrabMinigame(attributeInformation)
    minigameSelection = [roundOne, roundTwo, roundThree]
    for i in minigameSection:
        









menuSection()
print(characterAttribute._stat)


