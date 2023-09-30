#link to GIT repository: https://github.com/MNTSheridan/PROGassignment1
'''
git config user.name "MNTSheridan"
git config user.email "tran172@sheridancollege.ca"
'''
menuMessage = '''
You are currently laid off from your job, you're due for an eviction in 2 weeks and the best thing 
for you to make ends meet now is to rob a bank. What job are you taking on?
\nA. Driver\nB. Planner\nC. Robber\nD. Gunner'''
def menu():
    menuOption = input(menuMessage)
    characterClass = "Driver" if menuOption == "A" else "Leader" if menuOption == "B" else "Robber" if menuOption =="C" else "Gunner" if menuOption == "D" else None
    if characterClass == None:
        print("You better pick an option!")
        menu()