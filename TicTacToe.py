# This program was a project from the Python institute under the PCEP course. Here is my solution to the Tic Tac Toe problem.
# Please keep in mind that this program isn't smart at all. It randomises its moves. The objective was to demonstrate good coding knowledge and skills.

from random import randrange


board = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

def display_board(board):
    draw_move(board)

def enter_move(board):
    
    display_board(board)
    
    while True:  # Keep asking for user input until a valid move is made
        new_move = int(input("Input your move: "))
        free_list = make_list_of_free_fields(board)

        # Make sure move is in the free list and not played already
        if new_move in [board[i][j] for i, j in free_list]:
            for i in range(3):
                for j in range(3):
                    if board[i][j] == new_move:
                        board[i][j] = 'O'
            break
        else:
            print("Invalid move. Please choose an available square.")

    display_board(board)
    return board

def make_list_of_free_fields(board):
    free_field = []

    # Check and count moves to play by using the type of values in the board
    for i in range(3):
        for j in range(3):
            if type(board[i][j]) == int:
                free_field.append([i, j])

    return free_field

def victory_for(board):
    # Check rows and columns for 'O'
    for i in range(3):
        if (board[i][0] == 'O' and board[i][1] == 'O' and board[i][2] == 'O') or \
           (board[0][i] == 'O' and board[1][i] == 'O' and board[2][i] == 'O'):
            return "User (O) won the Game!"

    # Check diagonals for 'O'
    if (board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O') or \
       (board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O'):
        return "User (O) won the Game!"

    # Check rows and columns for 'X'
    for i in range(3):
        if (board[i][0] == 'X' and board[i][1] == 'X' and board[i][2] == 'X') or \
           (board[0][i] == 'X' and board[1][i] == 'X' and board[2][i] == 'X'):
            return "User (X) won the Game!"

    # Check diagonals for 'X'
    if (board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X') or \
       (board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X'):
        return "User (X) won the Game!"

    return "No Winner yet"

def draw_move(board):
    # Draw the board and update accordingly
    for i in range(3):
        if i > 0:
            print("+--------+---------+--------+")
        for j in range(3):
            if j > 0:
                print("|", end=" ")
            print(f"|   {board[i][j]}   ", end="")
        print("|")
    print("+--------+---------+--------+")

input("Welcome to the game of TicTacToe. Press any key to Start!")

print("I will Play First")
board[1][1] = 'X'


# Main game loop
while True:
    result = victory_for(board)
    if result != "No Winner yet":
        print(result)
        break
    else:
   
        enter_move(board)
        result = victory_for(board)
        if result != "No Winner yet":
            print(result)
            break
            
        print("My Turn :)")
        
        
        # Computer's move
        free_list = make_list_of_free_fields(board)
        rand_len = randrange(len(free_list))
        board[free_list[rand_len][0]][free_list[rand_len][1]] = 'X'
        #display_board(board)
        