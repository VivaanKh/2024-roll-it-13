# checks users enter yes (y) or no (n)
def yes_no(question):
    while True:
        response = input(question).lower()

        # Checks users response, question.
        # Repeats if users don't enter yes / no.
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes / no.")


def instruction():
    print('''
    **** Instructions ****
    
    To begin, decide on a score goal (eg: The first one to get a score of 50 wins).
    
    For each round of the game, you win points by rolling dice.
    The winner of the round is the one who gets 13 (or slightly less).
    
    If you win the round, then your score will increase by
    the number of points that you earned.
    If your first roll of two dice is a double (eg: both dice show a three), then
    your score will be double the number of points.
    
    If you lose the round, then you don't get any points.
    
    If you and the computer tie (eg: you both get a score of 11),
    then you will have 11 points added to your score.
    
    Your goal is to try get to the target score before the
    computer.
    
    Good luck.
    
    ''')

# Main routine
print()
print("🎲🎲 Roll it 13 🎲🎲")
print()

#loop for testing purposes.

want_instructions = yes_no("Do you want to read the instructions? ")

# checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instruction()

print("program continues")
