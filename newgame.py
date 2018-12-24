import random

def roll(sided, times):
    sum = 0
    for i in range(times):
        sum = sum + random.randint(1, sided)
    return sum



print("\n-------------------------------------------------------------------------------------------------\n")

doyouwant = input("You see a BSOD.  It wants to kill your computer!!! Fight (f) or run (r)? ")
if doyouwant[0] != "f":
    print("ok, bye")
else:
    mypoints = 10
    bsodpoints = 5
    turn_number = 1

    while mypoints > 0 and bsodpoints > 0:
        print("\n-------------------------------------------------------------------------------------------------\n")
        print(f"TURN #{turn_number}")

        input("your move.  press f to continue fighting. ")
        yourmove = roll(20, 1)
        if yourmove > 7:
            bsodpoints = bsodpoints - 1
            print(f"you hit the BSOD.  it has {bsodpoints} left.")
        else:
            print("you missed the BSOD.  sorry!")

        bsodmove = roll(20, 1)
        if bsodmove > 11:
            mypoints = mypoints - 2
            print(f"the BSOD hit you.  you have {mypoints} left.")
        else:
            print("the bsod missed you.  lucky!")
        
        turn_number = turn_number + 1

    if bsodpoints <= 0 and mypoints < 0:
        print("YOU AND THE BSOD BOTH DIED")
    elif bsodpoints <= 0:  # elif is short for "else if"
        print("BSOD is DEAD")
    else:
        print("YOU ARE DEAD")
