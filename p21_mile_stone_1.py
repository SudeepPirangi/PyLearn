"""
Tic-Tac-Toe game
"""

print("\nTic - Tac - Toe")

board = [" " for char in range(0, 9)]
x = "X"
o = "O"

def display_board(b = list(range(1, 10))):
    """Displays the board as a grid"""
    print(f"""
- - - - - - - - - -
|  {b[0]}  |  {b[1]}  |  {b[2]}  |
- - - - - - - - - -
|  {b[3]}  |  {b[4]}  |  {b[5]}  |
- - - - - - - - - -
|  {b[6]}  |  {b[7]}  |  {b[8]}  |
- - - - - - - - - -
""")

def marker_selection():
    """Prompts player to pick a marker"""
    marker_valid = False
    while not marker_valid:
        marker = input(f"Player-1: Please pick a marker {x} or {o} --> ")
        if marker.upper() == x or marker.upper() == o:
            marker_valid = True
            if marker.upper() == x:
                return (x, o)
            return (o, x)

def is_position_filled(b, position):
    """Checks if the position is already filled"""
    return b[position - 1] in [x, o]

def update_position(b, turn, player, position):
    """Updates the player selected position in the board"""
    if position.isdigit() and int(position) in range(1, 10):
        position = int(position)
        if not is_position_filled(b, position):
            b[position - 1] = player
            display_board(b)
            return (b, turn + 1, True)
        else:
            print(f"Position {position} is already filled. Try again!")
            return (b, turn, False)
    else:
        print(f"Position {position} doesn't exist. Try again!")
        return (b, turn, False)

def check_is_game_over(b):
    """Checks if the game is over"""
    return \
    b[0] == b[1] == b[2] and b[2] in [x, o] or \
    b[3] == b[4] == b[5] and b[5] in [x, o] or \
    b[6] == b[7] == b[8] and b[8] in [x, o] or \
    b[0] == b[3] == b[6] and b[6] in [x, o] or \
    b[1] == b[4] == b[7] and b[7] in [x, o] or \
    b[2] == b[5] == b[8] and b[8] in [x, o] or \
    b[0] == b[4] == b[8] and b[8] in [x, o] or \
    b[2] == b[4] == b[6] and b[6] in [x, o]

def gameon(b):
    """Runs the game"""
    is_game_over = False
    turn = 1
    position = 0
    winner = x
    while not is_game_over and turn <= 9:
        is_turn_complete = False
        while not is_turn_complete:
            position = ""
            if turn % 2 == 1:
                position = input(f"Player {x}, please pick a position between 1 and 9 --> ")
                b, turn, is_turn_complete = update_position(b, turn, x, position)
                winner = x
            else:
                position = input(f"Player {o}, please pick a position between 1 and 9 --> ")
                b, turn, is_turn_complete = update_position(b, turn, o, position)
                winner = o
        is_game_over = check_is_game_over(b)
    return (b, winner, turn)

display_board()

player1, player2 = marker_selection()

print(f"Player-1 is now '{player1}'\nPlayer-2 is now '{player2}'")
print(f"\nPlayer {x}, start the game!")

board, winner, turns = gameon(board)

if turns == 9:
    print("Match is a draw, well played both of you!")
else:
    print(f"Congratulations player {winner}, You won the match!")

display_board(board)
