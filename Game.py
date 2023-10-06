#Data & Logic
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