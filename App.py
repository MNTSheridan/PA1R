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
\nB. Demoman, you are responsible for opening vaults (Opening container vaults are faster with this class)
\nC. Robber, you are a responsible for collecting money (Money rewards are higher with this class)
\nD. Gunman, you are responsible for combating security and cops (Physical power is higher with this class)
\n\nChoice: '''

classChoiceDict = {
    "A":"Hijacker",
    "B":"Demoman",
    "C":"Robber",
    "D":"Gunman"
}

def menu():
    menuOption = input(menuMessage)
    if menuOption == None:
        print("You better pick an option!")
        menu()
    else:
        characterClass = classChoiceDict[menuOption]
        print(f"You chose {characterClass}! ")

menu()