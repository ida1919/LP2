
board = [' ' for _ in range(9)]


# Print board
def print_board():

    print("\nCurrent Board:\n")

    for i in range(0, 9, 3):

        print(board[i], "|", board[i+1], "|", board[i+2])

        if i < 6:
            print("--+---+--")

    print()


# Check winner
def check(player):

    win = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for x in win:

        if board[x[0]] == board[x[1]] == board[x[2]] == player:
            return True

    return False


# Computer move
def computer_move():

    # Try winning move
    for i in range(9):

        if board[i] == ' ':

            board[i] = 'O'

            if check('O'):

                print(f"Computer selected position {i}")
                return

            board[i] = ' '

    # Block player move
    for i in range(9):

        if board[i] == ' ':

            board[i] = 'X'

            if check('X'):

                board[i] = 'O'

                print(f"Computer selected position {i}")
                return

            board[i] = ' '

    # Otherwise choose first empty
    for i in range(9):

        if board[i] == ' ':

            board[i] = 'O'

            print(f"Computer selected position {i}")
            return


# Main Game
print("\n========== TIC TAC TOE USING A* SEARCH ==========")

print("\nPlayer Symbol   : X")
print("Computer Symbol : O")

print("\nBoard Positions:\n")

print("0 | 1 | 2")
print("--+---+--")
print("3 | 4 | 5")
print("--+---+--")
print("6 | 7 | 8")


while True:

    print_board()

    move = int(input("Enter your position (0-8): "))

    # Invalid move check
    if move < 0 or move > 8:

        print("Invalid Position! Enter value between 0 and 8.")
        continue

    if board[move] != ' ':

        print("Position already occupied! Try another.")
        continue

    # Player move
    board[move] = 'X'

    if check('X'):

        print_board()

        print("Congratulations! You Win!")
        break

    if ' ' not in board:

        print_board()

        print("Match Draw!")
        break

    # Computer move
    computer_move()

    if check('O'):

        print_board()

        print("Computer Wins!")
        break

    if ' ' not in board:

        print_board()

        print("Match Draw!")
        break
