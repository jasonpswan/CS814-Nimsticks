
def play_nimsticks():

    # Load in your initial board_state here.

    board_state = "Some board state."
    # Here we set up switches to swap the players.

    ply1 = True
    ply2 = False

    # Next we have a while loop until the board_state is equal to [].

    while board_state:

        # Check for terminal board state and if so return the winner.


            if ply1:

                # All your player one code.

                # Choose piles.

                # Choose number of sticks.

                # Update game state.

                # Move on to player 2

            else:

                # Call minimax which should return the next best move

                # Assign this move to the board_state



            # Finally we switch the players to ensure the game continues throughout the while loop

            if ply1:
                ply1 = False
                ply2 = True
            else:
                ply1 = True
                ply2 = False

    # When a null state is reached the game has been won, and depnding on the current

    # player a winning or loss message is displayed.

    if ply1:
        print("=============================\n")
        print("\nWell Done Player 1! You Won!\n")
    else:
        print("=============================\n")
        print("\nUnlucky, the Agent beat you! Better luck next time!\n")

    print("\nThanks for playing!")


def main():


    play_nimsticks()

main()