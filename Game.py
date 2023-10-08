#Data & Logic
import Demolitioner, Gunner, Hijacker, Robber
import random

characterAttribute = None
characterGamePath = None
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
    "A":("Hijacker", Hijacker.Attribute, Hijacker.gamePath),     #8
    "B":("Robber", Robber.Attribute, Robber.gamePath),       #8
    "C":("Gunner", Gunner.Attribute, Gunner.gamePath),       #9
    "D":("Demolitioner", Demolitioner.Attribute, Demolitioner.gamePath)  #11
}

def menuSection():
    global characterAttribute
    global characterGamePath

    menuMessage = '''
    It is the year 1872, you are the wild west's most notorious criminal in the Arizona, \n
    you are running low on cash, and you're going join a band of cowboys for a train robbery... Choose your role! 
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
        characterGamePath = playerInfo(roleStatConfiguration[menuOption][2])

        statMessage = f'''"Your attribute grades are presented in the order of: \n
        Lethality, Endurance, Dexterity, and Intelligence: {characterAttribute.attributeGrade()} \n
        Those stats will increase/decrease according to how you play the game. 
        (S grade stat will be at max capacity and cannot be increased)"
        '''
        print(statMessage)
    

    else:
        print("You better pick an option!")
        menuSection()


def railroadBombMinigame():
    global characterAttribute
    global attemptNumber
    dynamiteAmount = 0

    minigameMessage = f'''
    You are going to a try to force the train to halt, you're going to need to set up 12Kg of dynamite on the tracks within \n
    3 turns. For each dice roll you do, you will get a kilogram per the value that you roll. If you fail to get sufficient amount \n
    of dynamite on the tracks within that timeframe, you will lose 2 points of your endurance attribute, and the game will move on. \n
    '''

    statusMessage = input(f'''
    (Press A to roll the dice), this is attempt #{attemptNumber}.
    \n\n
    Roll dice: 
    ''')


    print(minigameMessage) if attemptNumber == 1 else None
    print(statusMessage)

    gameInput = input()
    if gameInput == "A" and attemptNumber < 3 and dynamiteAmount < 12:
        diceOutcome = random.choice(range(characterAttribute._dexterity,6))
        dynamiteAmount += diceOutcome
        outcomeMessage = f''' You have set up {diceOutcome}Kg of dynamite to the railroad.\n
        You have {dynamiteAmount - 12}Kg of dynamite left to add.\n
        '''
        print(outcomeMessage)
        attemptNumber += 1
        railroadBombMinigame()
    elif attemptNumber >= 3:
        print("You have failed this task, you will lose 2 endurance points.")
        characterAttribute._endurance -= 2
    elif gameInput != "A":
        print("Try again.")
        railroadBombMinigame()
    elif dynamiteAmount >= 12:
        print("You have sucessfully loaded up the dyanmites.. The train was bombed and stopped in its tracks, you enter the train.")
        characterAttribute._intelligence += 1
        

def securityMinigame():
    global characterAttribute
    
    securityDefeated = 0
    turnNumber = 1
    hitForce = 0 # if attemptNumber == 1 else hitForce
    securityAmount = random.randint(2,3)

    minigameMessage = f'''
    Security has been notified about the train being halted, and are now exiting the train to elminate the threat. \n
    There could be 2-3 security guards entering out the train. If you fail to take down one of the security guards,  \n
    you will lose the game. To win against a guard, you must be able to get closer to the number 12 in all the rolled dice values than the guard. \n
    If the hitforce value of both you and the guard are the same, you will still defeat the guard.\n
    You will be given 3 turns to try to get your hit force as close to 12 as possible. \n
    If you exceed that force, you won't lose the minigame but you will lose accuracy and your chances of winning.\n
    (Press A to roll the dice, B to stop rolling the dice and end your turn), this is attempt #{attemptNumber}.
    \n\n
    Roll dice: '''

    print(minigameMessage) #if attemptNumber == 1 else None
    gameInput = input()

    while gameInput == "A" and securityDefeated < securityAmount:
        if turnNumber < 4:
            statusMessage = '''
            (Press A to roll the dice) this is attempt #{attemptNumber}.
            \n\n
            Roll dice: '''
            print(statusMessage)
            diceOutcome = random.choice(range(characterAttribute._lethality,6))
            hitForce += diceOutcome
            outcomeMessage = f''' You currently have added {diceOutcome} into your hit force..\n
            You have {hitForce} amount of hit force.
            '''
            print(outcomeMessage)
            gameInput = input()
        else:
            break
    if attemptNumber <= 4:
        print("You have failed this task, you failed the Heist.")
        characterAttribute._endurance -= 4
    elif gameInput == "B" or turnNumber >= 4:
        securityHitforce = random.randint(4,11)
        if abs(hitForce-12) > abs(securityHitforce-12):
            securityDefeated += 1
            print(f"You have defeated a guard, {securityAmount - securityDefeated} guards are left for you to complete this task.")
    elif securityDefeated >= securityAmount:
        print("You have defeated all security. Moving on to the next task.")
        characterAttribute._dexterity += 1
        characterAttribute._intelligence += 1
    elif minigameMessage != "A":
        print("Try again.")
        securityMinigame()


def doorUnlockMinigame():
    global characterAttribute
    minigameMessage = '''
    You are going to a set up explosives, you're going to need to set up 12Kg of dynamite on the tracks within, 
    3 turns. For each dice roll you do, you will get a kilogram per the value that you roll. If you fail to get 
    sufficient amount of dynamite on the tracks within that timeframe, you will die.'''
    print(minigameMessage)

def moneyGrabMinigame():
    global characterAttribute
    minigameMessage = '''
    You are going to a set up explosives, you're going to need to set up 12Kg of dynamite on the tracks within, 
    3 turns. For each dice roll you do, you will get a kilogram per the value that you roll. If you fail to get 
    sufficient amount of dynamite on the tracks within that timeframe, you will die.'''
    print(minigameMessage)

def minigameSection():
    global characterAttribute
    global characterGamePath
    gameStatus = "Neutral"

    for minigame in characterGamePath:
        if characterAttribute._endurance > 0:    
            global attemptNumber
            attemptNumber = 1
            informationMessage = '''You have:\n
        {characterAttribute._lethality} lethality.
        {characterAttribute._endurance} endurance.
        {characterAttribute._dexterity} dexterity.
        {characterAttribute._intelligence} intelligence. \n'''
            print(informationMessage)
            minigame(characterAttribute)
        elif characterAttribute._endurance <= 0:
            gameStatus = "Lost"
            break
        gameStatus = "Won"
    if gameStatus == "Won":
        winScenario()
    elif gameStatus == "Lost":
        loseScenario()

        
def winScenario():
    thing = "a"

def loseScenario():
    thing = "b"
