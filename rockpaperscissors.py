# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)


def newgame():
    gameon = input("Would you like to start a game? Y/N \n")
    no = ["No", "N", "n", "no", "Quit"]
    if gameon not in no:
        result = run_game()
        if result == 0:
            print("Player 1 wins, congrats")
        else: print("Player 2 wins, congrats")
        endgame()
    else: endgame()

def run_game():
    winner = None
    while winner == None:
        throws = get_throws()
        winner = declare_winner(throws)
    return True

def get_throws():
    throws =[]
    throw1 = None
    throw2 = None
    while not validate(throw1):
        throw1 = input("P1, what would you like to throw? \n")
        print("P1, please type either rock, paper or scissors\n")
    throws.append(throw1)
    while not validate(throw2):
        throw2 = input("P2, what would you like to throw? \n")
        print("P2, please type either rock, paper or scissors\n")
    throws.append(throw2)
    return throws

def validate(throw_input):
    approved_inputs = ["rock", "paper", "scissors"]
    if throw_input in approved_inputs:
        return True
    else: return False

def declare_winner(throws):
    if throws[0] == throws[1]:
        print("You both threw " + throws[0])
        return None
    elif throws[0] == "rock":
        if throws[1] == "scissors":
            return 0
        else:
            return 1
    elif throws[0] == "paper":
        if throws[1] == "rock":
            return 0
        else:
            return 1
    else:
        if throws[1] == "paper":
            return 0
        else:
            return 1

def endgame():
    print("Thanks for playing!")
    newgame()


# Game on

print("Welcome to rock, paper, scissors.\n")

newgame()


# TODO Make it 2 out of 3