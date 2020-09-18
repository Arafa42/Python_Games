import numpy

def create_board():
    board =  numpy.zeros((6,7))
    return board

board = create_board()
game_over = False
turn = 0

while not game_over:
    if turn == 0:
        selection = int(input("Player 1, choose between (0-6)"))
    else:
        selection = int(input("Player 2, choose between (0-6)"))

    turn+=1
    turn = turn %2