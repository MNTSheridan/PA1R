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

classChoiceDict = {
    "A":("Hijacker", ("C", "B", "A")),
    "B":("Robber", ("B", "C", "A")),
    "C":("Gunner", ("A", "B", "C")),
    "D":("Demolitioner", ("S"))
}
lethalityA, healthA, dexterityA
def menu():
    menuOption = input(menuMessage)
    if menuOption == None:
        print("You better pick an option!")
        menu()
    else:
        characterClass = classChoiceDict[menuOption]
        print(f"You chose {characterClass}! ")

menu()