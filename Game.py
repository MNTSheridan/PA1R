#Data & Logic
import Demolitioner, Gunner, Hijacker, Robber
import random

characterAttribute = None
attemptNumber = 1


class playerInfo:
    def __init__(self, attribute):    
        self._stat = attribute    
        self._lethality = attribute[0]
        self._endurance = attribute[1]
        self._dexterity = attribute[2]
        self._intelligence = attribute[3]
    

    #This method takes in a datastructure which it would want to be a list so that it converts the player's attribute statistics to letter graded data.
    def attributeGrade(self):
        total = []
        if type(self._stat) == list:
            for i in self._stat:
                total.append("S" if i == 4 else "A" if i == 3 else "B" if i == 2 else "C")
            return total
        else:
            print("error")
            return "S" if i == 4 else "A" if i == 3 else "B" if i == 2 else "C"

            

'''
Lethality as an attribute contributes to how well a class is able to
fend of threats such as security.
X Grade Lethality allows the class to take down threats in Y turns
S - 1
A - 2
B - 2
C - 4

Endurance as an attribute contributes to how well a class is able to sustain
failures/mistakes/physical damage in mission.
X Grade Endurance allows the class to sustain failure in completing a task Y times
S - 4
A - 3
B - 2
C - 1

Dexterity as an attribute contributes how fast a class completes a task.
X Grade Dexterity allows the class to finish tasks in Y turns.
S - 1
A - 2
B - 3 turns
C - 4 turns

Intelligence as an attribute affects the ability of the player to attain their 
rewards percentage.
X grade Intelligence allows the class to get Y% of the money portion by 
the end of the game, which will determine their score to determine if they will win 
S - 40%
A - 30%
B - 20%
C - 10%

'''

roleStatConfiguration = {
    "A":("Hijacker", Hijacker.Attribute),     #8
    "B":("Robber", Robber.Attribute),       #8
    "C":("Gunner", Gunner.Attribute),       #9
    "D":("Demolitioner", Demolitioner.Attribute)  #11
}

def menuSection():
    global characterAttribute

    menuMessage = '''
    It is the year 1872, you are the wild west's most notorious criminal in the Arizona, \n
    you are running low on cash, and you're going to plan for a train robbery... Choose your role! 
    \nA. Hijacker, you are responsible with hijacking doors (Unlocking doors are faster with this role)
    \nB. Robber, you are a responsible for collecting money (Money rewards are higher with this role)
    \nC. Gunner, you have an advantage for fending off train security guards.
    \nD. Demolitioner, you are have an advantage for unlocking vaults since this role has enhanced endurance. 
    \n\nChoice: 
    '''

    menuOption = input(menuMessage)
    if menuOption in ("A", "B", "C", "D"):
        #characterClass is variable that contains the attribute stats of the player
        characterClass = roleStatConfiguration[menuOption][0]
        print(f"You chose {characterClass}!")
        characterAttribute = playerInfo(roleStatConfiguration[menuOption][1])

        statMessage = f'''"Your attribute grades are presented in the order of: \n
        Lethality, Endurance, Dexterity, and Intelligence: {characterAttribute.attributeGrade()} \n
        Those stats will increase/decrease according to how you play the game. 
        (S grade stat will be at max capacity and cannot be increased)"
        '''
        print(statMessage)
    

    else:
        print("You better pick an option!")
        menuSection()


def railroadBombMinigame(attributeInformation):
    global characterAttribute
    global attemptNumber
    attemptNumber += 1
    dynamiteAmount = 0
    minigameMessage = input(f'''
    You are going to a set up explosives, you're going to need to set up 12Kg of dynamite on the tracks within, \n
    3 turns. For each dice roll you do, you will get a kilogram per the value that you roll. If you fail to get sufficient amount \n
    of dynamite on the tracks within that timeframe, you will lose 2 points of your endurance attribute, and the game will move on. \n
    (Press A to roll the dice), this is attempt #{attemptNumber}.
    \n\n
    Roll dice: 

    ''')
    print(minigameMessage)
    if minigameMessage == "A" and attemptNumber > 4 and dynamiteAmount < 12:
        diceOutcome = random.choice(range(1,6))
        dynamiteAmount += diceOutcome
        outcomeMessage = f''' You have set up {diceOutcome}Kg of dynamite to the railroad.\n
        You have {dynamiteAmount - 12}Kg of dynamite left to add.
        '''
        print(outcomeMessage)
        railroadBombMinigame(characterAttribute)
    elif attemptNumber <= 4:
        print("You have failed this task, you will lose 2 endurance points.")
        characterAttribute._endurance -= 2

        
        

def securityMinigame(attributeInformation):
    endurance = attributeInformation._endurance
    lethality = attributeInformation._lethality
    minigameMessage = '''
    You are going to a set up explosives, you're going to need to set up 12Kg of dynamite on the tracks within, 
    3 turns. For each dice roll you do, you will get a kilogram per the value that you roll. If you fail to get 
    sufficient amount of dynamite on the tracks within that timeframe, you will die.

    '''
    print(minigameMessage)

def doorUnlockMinigame(attributeInformation):
    endurance = attributeInformation._endurance
    dexterity = attributeInformation._dexterity
    minigameMessage = '''
    You are going to a set up explosives, you're going to need to set up 12Kg of dynamite on the tracks within, 
    3 turns. For each dice roll you do, you will get a kilogram per the value that you roll. If you fail to get 
    sufficient amount of dynamite on the tracks within that timeframe, you will die.'''
    print(minigameMessage)

def moneyGrabMinigame(attributeInformation):
    endurance = attributeInformation._endurance
    dexterity = attributeInformation._dexterity
    minigameMessage = '''
    You are going to a set up explosives, you're going to need to set up 12Kg of dynamite on the tracks within, 
    3 turns. For each dice roll you do, you will get a kilogram per the value that you roll. If you fail to get 
    sufficient amount of dynamite on the tracks within that timeframe, you will die.'''
    print(minigameMessage)

def minigameSection(attributeInformation):
    endurance = attributeInformation._endurance
    dexterity = attributeInformation._dexterity

    roundOne = random.choice([doorUnlockMinigame(attributeInformation)]* 3 + [railroadBombMinigame(attributeInformation)])
    roundTwo = random.choice([doorUnlockMinigame(attributeInformation)]* 3 + [securityMinigame(attributeInformation)])
    roundThree = [moneyGrabMinigame(attributeInformation)]
    minigameSelection = [roundOne, roundTwo, roundThree]
    for minigame in minigameSelection:
        minigame(characterAttribute)

