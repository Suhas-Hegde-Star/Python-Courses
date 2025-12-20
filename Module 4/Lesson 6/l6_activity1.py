board = {
    1: " ",
    2: " ",
    3: " ",
    4: " ",
    5: " ",
    6: " ",
    7: " ",
    8: " ",
    9: " "
}

board_keys = []
for key in board:
    board_keys.append(key)

def print_board(board):
    print(board[1] + "  | " + board[2] + " | " + board[3])
    print("---+---+---")
    print(board[4] + "  | " + board[5] + " | " + board[6])
    print("---+---+---")
    print(board[7] + "  | " + board[8] + " | " + board[9])
print_board(board)

def game():
    turn = "X"
    for i in range(10):
        print("Turn for " + turn + ". Move on which space?")
        move = int(input())
        if board[move] == " ":
            board[move] = turn
            print_board(board)
            if turn == "X":
                turn = "O"
            else:
                turn = "X"
        else:
            print("That space is already occupied. Try again.")
            continue

        if i >= 5:
            if  (board[1] == board[2] == board[3] != " ") or \
                (board[4] == board[5] == board[6] != " ") or \
                (board[7] == board[8] == board[9] != " ") or \
                (board[1] == board[4] == board[7] != " ") or \
                (board[2] == board[5] == board[8] != " ") or \
                (board[3] == board[6] == board[9] != " ") or \
                (board[1] == board[5] == board[9] != " ") or \
                (board[3] == board[5] == board[7] != " "):
                    print(" **** Game Over. " + turn + " wins! ****")
                    break
        
    if i == :
        print(" **** Game Over. It's a Tie! ****")

game()