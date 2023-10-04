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
\nC. Gunner, you are responsible for fending off train security guards.
\nD. Demolitioner, you are responsible for unlocking vaults and you have enhanced endurance. 
\n\nChoice: '''

classChoiceDict = {
    "A":("Hijacker", ("B", "B", "S", "C")),
    "B":("Robber", ("C", "B", "A", "B")),
    "C":("Gunner", ("S", "C", "C", "S")),
    "D":("Demolitioner", ("C", "S", "B", "A"))
}


def menu():
    menuOption = input(menuMessage)
    if menuOption in ("A", "B", "C", "D"):
        characterClass = classChoiceDict[menuOption][0]
        print(f"You chose {characterClass}!")
        characterAttribute = Game.playerInfo(classChoiceDict[menuOption][1])
        print(f"Your attribute grades are presented in the order of: \nLethality, Endurance, Dexterity, and Intelligence: {characterAttribute.all}")
    else:
        print("You better pick an option!")
        menu()
        
menu()