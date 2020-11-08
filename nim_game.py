import random

def initial_board():
    board = [random.randrange(2, 5) for i in range(random.randint(1, 10))]
    return board

def choose_first():
    player = []
    flip = random.randint(0,1)
    if flip == 0:
        player = "Human"
    else:
        player = "Computer"
    return player

def pile_choice():
    pile = int(input("Which pile do you wish to take from?"))
    # inputted choice must be valid, between 1 and length number of piles
    if pile >= 1 and pile <= len(board):
        return pile
    else:
        return "Please make a valid choice."
            
def remove_sticks():
    sticks = int(input("How many sticks do you wish to pick up?"))
    # inputted choice must be valid, between 1 and 3 (if number of sticks >= 3)
    if sticks >= 1 and sticks <= 3:
        return sticks
    else:
        return "Please choose a number between 1 and 3."

while True:
    print(initial_board())
    
   # if player == "Human":
      #  pass