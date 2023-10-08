#Data & Logic
import Demolitioner, Gunner, Hijacker, Robber
import random

characterAttribute = None
characterGamePath = None
moneyStolen = None
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
X Grade Dexterity increases the minimum propability of a dice roll by Y.
S - 0
A - 1
B - 2 
C - 3 For example the probability of dice roll is increased by 3 so the player
can only roll (4-6)

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
    \nD. Demolitioner, you are have an advantage for bombing railways since this role has enhanced endurance. 
    \n\nChoice: 
    '''
    print(menuMessage)
    menuOption = input()
    if menuOption in ("A", "B", "C", "D"):
        #characterClass is variable that contains the attribute stats of the player
        characterClass = roleStatConfiguration[menuOption][0]
        print(f"You chose {characterClass}!")
        characterAttribute = playerInfo(roleStatConfiguration[menuOption][1])
        characterGamePath = roleStatConfiguration[menuOption][2]

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
    5 turns. For each dice roll you do, you will get a kilogram per the value that you roll. If you fail to get sufficient amount \n
    of dynamite on the tracks within that timeframe, you will lose 2 endurance, and 1 intelligence attribute. \n
    If that happens, you will move on to the 2nd minigame.
    '''

    print(minigameMessage)

    while attemptNumber <= 5 and dynamiteAmount < 12:
        statusMessage = f'''
        (Press A to roll the dice to determine dynamite amount placed on train tracks), this is attempt #{attemptNumber}.
        \n\n
        Roll dice: 
        '''
        print(statusMessage)
        gameInput = input()
        if gameInput == "A":
            diceOutcome = random.choice(range(characterAttribute._dexterity,6))
            dynamiteAmount += diceOutcome
            outcomeMessage = f''' You have set up {diceOutcome}Kg of dynamite to the railroad.\n
            You have {12 - dynamiteAmount}Kg of dynamite left to add.\n
            '''
            print(outcomeMessage)
            attemptNumber += 1
        else:
            print("Try again.")
        
    if dynamiteAmount < 12:
        print(f"You were short on {12 - dynamiteAmount} Kilograms, the train has passed the bombsite, you have failed this task, you will lose 2 endurance points. Your teammate has suceeded in bombing the train rails, you enter the train.")
        characterAttribute._endurance -= 2
        characterAttribute._intelligence -= 1
    
    elif dynamiteAmount >= 12:
        print("You have sucessfully loaded up the dynamites.. The train was bombed and stopped in its tracks, you enter the train.")
        characterAttribute._intelligence += 1
        

def securityMinigame():
    global characterAttribute
    global attemptNumber
    securityDefeated = 0
    securityAmount = random.randint(2,3)
    hitForce = 0 

    minigameMessage = f'''
    Security has been notified about the train being halted, and are now exiting the train to elminate the threat. \n
    There could be 2-3 security guards entering out the train, in this case you are fighting {securityAmount} Guards. \n
    To defeat a guard, you must be able to get closer to the number 12 in all the rolled dice values than the guard. \n
    If the hitforce value of both you and the guard are the same, you will still defeat the guard.\n
    You will be given unlimited times to try to get your hit force as close to 12 as possible. \n
    If you exceed that force, you won't lose the minigame but you will lose accuracy and your chances of winning.\n
    The amount of attempts that you have is equivalent to the number of guards you will have to defeat, you will only need to defeat one guard. '''

    print(minigameMessage)

    while attemptNumber <= securityAmount and securityDefeated <= 0:
        statusMessage = f'''
        (Press A to roll the dice, B to stop rolling the dice and attack the Guard) you are fighting guard #{attemptNumber}.
        \n\n
        Roll dice: '''
        print(statusMessage)
        gameInput = input()
        if gameInput == "A":
            diceOutcome = random.choice(range(characterAttribute._lethality,6))
            hitForce += diceOutcome
            hitForceMessage = f''' You currently have added {diceOutcome} into your hit force..\n
            You have {hitForce} amount of hit force.
            '''
            print(hitForceMessage)
        elif gameInput == "B":
            securityHitforce = random.randint(4,11)
            if hitForce <= 0:
                print("Didn't even try to add any hit force to your attack!")
            elif hitForce > 0:
                if (abs(hitForce-12) < abs(securityHitforce-12)):
                    outcomeMessage = f'''
                    You have used {hitForce} force while the security guard has used {securityHitforce} force. \n
                    The accuracy of your attack is {abs(securityHitforce-12)- abs(hitForce-12)} more accurate than the guard. You have defeated a guard.
                    '''
                    print(outcomeMessage)
                    securityDefeated += 1
                elif (abs(hitForce-12) > abs(securityHitforce-12)):
                    outcomeMessage = f'''
                    You have used {hitForce} force while the security guard has used {securityHitforce} force. \n
                    The accuracy of your attack is {abs(hitForce-12) - abs(securityHitforce-12)} worse than the guard.\n
                    The Guard has beaten you, but your teammates had your back and defeated the guard, you still have to pull your own weight, kill at least one guard.\n
                    '''
                    print(outcomeMessage)
                    hitForce = 0
                attemptNumber += 1
        else:
            print("Try again")
    if attemptNumber > securityAmount:
        print("You have failed this task.")
        characterAttribute._endurance -= 4
    elif securityDefeated >= 1:
        print("You have completed the minimum requirement to win. Moving on to the next task.")
        characterAttribute._dexterity += 1
        characterAttribute._intelligence += 1


def doorUnlockMinigame():
    global characterAttribute
    global attemptNumber
    doorsLocked = random.randint(1,3)
    doorPass = random.randint(1,6)
    doorsUnlocked = 0
    minigameMessage = f'''
    You need to unlock {doorsLocked} doors to get into the vault, guess the correct digit for each door to win, you get three tries per door but if you fail to open them, you will lose one intelligence attribute point and the game will move on.
    '''
    print(minigameMessage)
    while attemptNumber <= 3 and doorsUnlocked < doorsLocked:
        statusMessage = f'''
        You are trying to unlock door no.{doorsUnlocked+1}, try to guess the one digit password! (1-6)
        '''
        print(statusMessage)
        gameInput = int(input())
        if gameInput == doorPass:
            print("You have unlocked the door!, onto the next one.")
            doorsUnlocked+=1
            attemptNumber == 1
            doorPass = random.randint(1,6)
        elif gameInput < doorPass:
            print("While trying to unlock the door you feel that your guess is lower than the door's password.")
            attemptNumber += 1
        elif gameInput > doorPass:
            print("While trying to unlock the door you feel that your guess is higher then the door's password.")
            attemptNumber += 1
    if doorsUnlocked > doorsLocked:
        print("You have unlocked all the doors!")
        characterAttribute._intelligence += 1
    elif attemptNumber > 3:
        print(f"The Lock password was {doorPass}, but since you have attempted 3 times the lock has stopped working, you failed to complete this task, your teammates sigh and does the job for you, you have lost 1 intelligence point.")
        characterAttribute._intelligence -= 1
        characterAttribute._endurance -= 1


def moneyGrabMinigame():
    global characterAttribute
    global attemptNumber
    global moneyStolen
    moneyHeld = 0 
    
    minigameMessage = f'''
    You have entered a vault. You have {characterAttribute._dexterity} turns to take as much money as you can in the vault.
    '''

    print(minigameMessage)
    while attemptNumber >= characterAttribute._dexterity:
        statusMessage = f'''
        Press A to rob money, you have {abs(characterAttribute._dexterity-attemptNumber)} turns left.
        '''
        print(statusMessage)
        gameInput = input()
        if gameInput == "A":
            moneyGain = random.randint(1000,1500)
            moneyHeld += moneyGain
            print(f"You have stolen ${moneyGain}!")
        elif gameInput != "A":
            print("Try again.")
    moneyStolen = moneyHeld
    print(f"You have stolen about ${moneyHeld}!!!")
    

    

def gamePathConfiguration(miniGame):
    if miniGame == "railroadBombMinigame":
        railroadBombMinigame()
    elif miniGame == "securityMinigame":
        securityMinigame()
    elif miniGame == "doorUnlockMinigame":
        doorUnlockMinigame()
    elif miniGame == "doorUnlockMinigame":
        doorUnlockMinigame()

def minigameSection():
    global characterAttribute
    global characterGamePath
    gameStatus = "Neutral"

    for miniGame in characterGamePath:
        if characterAttribute._endurance > 0:    
            global attemptNumber
            global moneyStolen
            moneyStolen = moneyStolen
            attemptNumber = 1
            informationMessage = f'''Your attribute information:\n
        {characterAttribute._lethality} lethality.
        {characterAttribute._endurance} endurance.
        {characterAttribute._dexterity} dexterity.
        {characterAttribute._intelligence} intelligence. \n'''
            print(informationMessage)
            print(f"Minigame stage: {miniGame}")
            gamePathConfiguration(miniGame)
        elif characterAttribute._endurance <= 0:
            gameStatus = "Lost"
            break
    else:
        gameStatus = "Won"
    if gameStatus == "Won":
        winScenario()
    elif gameStatus == "Lost":
        loseScenario()

        
def winScenario():
    crewMoney = random.randint(3000,5000)
    print(f"You have had a SUCESSFUL HEIST!, you have contributed ${moneyStolen} in the pot money for the heist.")
    print(f"which contains a total of ${crewMoney+moneyStolen} !!")
    finalEarnings = (crewMoney+moneyStolen)*characterAttribute._intelligence/10
    print(f"Since you have {characterAttribute._stat.attributeGrade()[3]} level intelligence, you have won {characterAttribute*10}% of the earnings!")
    print(f"Which is ${finalEarnings}!!!!!! Congratulations!! Restart the program to play again.")

def loseScenario():
    print("Unfortunately you have failed the heist due to making numerous mistakes, leading your teammembers to kick you out of the event. Restart the program to play again.")
