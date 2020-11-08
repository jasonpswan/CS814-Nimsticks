import random
from random import randrange

def current_game_state(state):
    if state[1] == 1:
        player = 'Human'
    else:
        player = 'Computer'
    for pile_count, sticks in enumerate(state[0]):
        print("\tPile {} - {} sticks".format(pile_count + 1, sticks))
      
initial_piles = []
for pile in range (0, 5):
    sticks = randrange(1, 10)
    initial_piles.append(sticks)
    state = (initial_piles, 1)

