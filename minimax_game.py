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
    sticks = randrange(1, 5)
    initial_piles.append(sticks)
    state = (initial_piles, 1)

while True:
    current_game_state(state)
    
    if state[1] == 1:
        # Human Player
        piles = state[0]
        pile_pick = int(input("Which pile do you wish to pick from?"))
        pile_count = pile_pick - 1
        pile = piles [pile_count]
        pick_up_sticks = int(input("How many sticks do you wish to pick up?"))
        if pile >= pick_up_sticks:
            result = pile - pick_up_sticks
            if result != 0:
                new_pile = sorted (piles[:pile_count] + [result] + piles[pile_count + 1:])
            else:
                new_pile = sorted(piles[:pile_count] + piles[pile_count + 1:])
            state = (new_pile, 2)
    
    else:
        # Stephen Hawking's Turn
        print ("Jason Swan's Brain's Turn")
        successors_list = successors (state)
        number_states = len(successors_list)
        for next_state_index, next_state in enumerate(successors_list):
            utility_score = minimax_value_ab(next_state)
            if utility_score == -1:
                state = next_state
                break
            elif next_state_index == number_states - 1:
                state = next_state
                
    if state[0] == []:
        if state[1] == 1:
            winner = "Jason Swan"
        else:
            winner = "Jason Swan's Brain"
        print("The winner is {}".format(winner))
        break