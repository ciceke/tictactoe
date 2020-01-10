board=[0]*9
players=['X','W']
turn=0

def print_board(board):
    print(' {} | {} | {} '.format(board[6],board[7],board[8]))
    print('--------------')
    print(' {} | {} | {} '.format(board[3],board[4],board[5]))
    print('--------------')
    print(' {} | {} | {} '.format(board[0],board[1],board[2]))

print_board(board)
while True:
    
    pos=int(input('position :'))
    if pos>9:
        print('Enter number b/w 1-9')
    elif pos==0:
        break
    else:
        if board[pos-1]!=0:
            print('Burası dolu')
        else:
            board[pos-1]=players[turn]
            turn=abs(turn-1)
            print_board(board)
