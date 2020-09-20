import numpy

ROW = 6
COL = 7


def create_board():
    board = numpy.zeros((ROW, COL))
    return board


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid_loc(board, col):
    return board[5][col] == 0


def next_available_row(board, col):
    for r in range(ROW):
        if board[r][col] == 0:
            return r

def reverse_print_board():
    print(numpy.flip(board,0))

def win_check(board,piece):
    for c in range(COL-3):
        for r in range(ROW):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
    for c in range(COL):
        for r in range(ROW-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    for c in range(COL-3):
        for r in range(ROW-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    for c in range(COL-3):
        for r in range(3,ROW):
            if board[r][c] == piece and board[r-11][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True






board = create_board()
print(board)
game_over = False
turn = 0

while not game_over:
    if turn == 0:
        colInput = int(input("Player 1, choose between (0-6)"))
        if(is_valid_loc(board,colInput)):
            row = next_available_row(board, colInput)
            drop_piece(board,row,colInput,1)

            if(win_check(board,1)):
                print("PLAYER 1 WINS !")
                game_over = True


    else:
        colInput = int(input("Player 2, choose between (0-6)"))
        if(is_valid_loc(board,colInput)):
            row = next_available_row(board,colInput)
            drop_piece(board,row,colInput,2)

            if(win_check(board,2)):
                print("PLAYER 2 WINS !")
                game_over = True

    reverse_print_board()


    turn += 1
    turn = turn % 2
