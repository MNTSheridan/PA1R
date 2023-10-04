import Game
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
\n\nChoice: '''

characterAttribute = None

classChoiceDict = {
    "A":("Hijacker", ("B", "B", "S", "C")),
    "B":("Robber", ("C", "B", "A", "B")),
    "C":("Gunner", ("S", "C", "C", "S")),
    "D":("Demolitioner", ("C", "S", "B", "A"))
}
lethalityA, healthA, dexterityA, intelligenceA
def menu():
    menuOption = input(menuMessage)
    if menuOption == None:
        print("You better pick an option!")
        menu()
    else:
        characterClass = classChoiceDict[menuOption][0]
        print(f"You chose {characterClass}! ")
        characterAttribute = Game.playerInfo()
        
menu()