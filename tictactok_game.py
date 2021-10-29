# -----------------Global Variables-------------------

# Game board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-", ]
print(board[0])
# if game is still going
game_still_going = True

# who won? or tie?
winner = None

# who is turn is it
current_player = "x"


# display board
def display_board():
    print("\n" + board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+---")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+---")
    print(board[6] + " | " + board[7] + " | " + board[8])


# play a game of tic tac toe
def play_game():
    print("1" + " | " + "2" + " | " + "3")
    print("--+---+---")
    print("4" + " | " + "5" + " | " + "6")
    print("--+---+---")
    print("7" + " | " + "8" + " | " + "9")
    # displa initial board
    display_board()

    # while the game is  still going
    while game_still_going:
        # handle a single turn of an arbitrary player
        handle_turn(current_player)

        # check if the has ended
        check_if_game_over()

        # flip to the other player
        flip_player()

    # game has ended
    if winner == "x" or winner == "o":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")


# handle a single turn of an arbitrary player
def handle_turn(player):
    print(player + "'s turn")
    position = input("choose a position from 1-9: ")

    valid = False
    while not valid:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("invalid input , choose a position from 1-9: ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("you can't go there")

    board[position] = player

    display_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():
    # set up global variables
    global winner

    # check rows
    row_winner = check_rows()
    # check columns
    column_winner = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:

        winner = None
    return


def check_rows():
    # set up global variables
    global game_still_going
    # check if any of the rows have all the same value (and its not empty)
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    # if any row have a match , flag that there is a win
    if row_1 or row_2 or row_3:
       game_still_going = False
    # return the winner (x or o)
    if row_1:
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]
    return


def check_columns():
    # set up global variables
    global game_still_going
    # check if any of the column have al the same value (and its not empty)
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    # if any column have a match , flag that there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False
    # return the winner (x or o)
    if column_1:
        return board[0]
    if column_2:
        return board[1]
    if column_3:
        return board[2]
    return


def check_diagonals():
    # set up global variables
    global game_still_going
    # check if any of the diagonal have al the same value (and its not empty)
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[6] == board[4] == board[2] != "-"

    # if any diagonal have a match , flag that there is a win
    if diagonal_1 or diagonal_2:
        game_still_going = False

    # return the winner (x or o)
    if diagonal_1:
        return board[0]
    if diagonal_2:
        return board[6]

    return


def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False

        return

    return


def flip_player():
    # global variables we need
    global current_player
    # if current player was x , then change it to o
    if current_player == "x":
        current_player = "o"
    # if current player was o , then change it to x
    elif current_player == "o":
        current_player = "x"

    return


play_game()
# board
# display board
# play game
# handle turn
# check win
# check rows
# check columns
# check diagonals
# check tie
# winner
# flip player
# game_still_going
# check_if_game_over
# current_player
# player

# board in display board
# all in play game
# handle turn = winner, game_still_going, position, valid
# chek if game over = check win == check tie = 1 check rows == check columns == check diagonal = 2 game still going False
# flip player player x == player o
# use return and global and true and false not continue and break no whiletrueloop
# last function play game