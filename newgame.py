import random
import sys

def roll(sided, times):
    sum = 0
    for i in range(times):
        sum = sum + random.randint(1, sided)
    return sum


class Monster:
    def __init__(self, name, action, hits):
        self.name = name
        self.action = action
        self.hits = hits

class Player:
    def __init__(self, name, hits):
        self.name = name
        self.hits = hits



print("\n-------------------------------------------------------------------------------------------------\n")

name = input("What is your name? ")
if name == "tissuebox":
    print("That name is already taken.  Sorry!")
    sys.exit()
    
player = Player(name, 10)

monster1 = Monster("giant rat", "kill you!", 5)
monster2 = Monster("sheep", "baaaaa you!", 1)

if roll(2, 1) > 1:
    monster = monster1
else:
    monster = monster2

doyouwant = input(f"You see a {monster.name}!!!  It wants to {monster.action}!!! Fight (f) or run (r)? ")
if doyouwant[0] != "f":
    print("Last person to play this game's a rot13 egg!\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
else:
    mypoints = 10
    turn_number = 1

    while mypoints > 0 and monster.hits > 0:
        print("\n-------------------------------------------------------------------------------------------------\n")
        print(f"TURN #{turn_number}")

        input("your move.  press f to continue fighting. ")
        yourmove = roll(20, 1)
        if yourmove > 7:
            monster.hits = monster.hits - 1
            print(f"you hit the {monster.name}.  it has {monster.hits} left.")
        else:
            print(f"you missed the {monster.name}.  sorry!")

        bsodmove = roll(20, 1)
        if bsodmove > 11:
            mypoints = mypoints - 2
            print(f"the {monster.name} hit you.  you have {mypoints} left.")
        else:
            print(f"the {monster.name} missed you.  lucky!")
        
        turn_number = turn_number + 1

    if monster.hits <= 0 and mypoints < 0:
        print(f"YOU AND THE {monster.name} BOTH DIED")
    elif monster.hits <= 0:  # elif is short for "else if"
        print(f"The {monster.name} is DEAD")
    else:
        print("YOU ARE DEAD")
input("Press Enter to close this window...\n")
