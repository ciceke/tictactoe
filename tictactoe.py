'''
TicTacToe Game
'''
board=['']*9
players=['X','O']
turn=0

def init_game():
    global board
    global turn
    
    for i in range(0,9):
        board[i]=''

    while True:
        first_player=input('Choose X or O').upper()
        if first_player=='X':
            turn=0
            break
        elif first_player=='O':
            turn=1
            break
        else:
            print('Enter either X or O')

def print_board(board):
    print(' {}  | {}  | {}'.format(board[6],board[7],board[8]))
    print('-------------')
    print(' {}  | {}  | {}'.format(board[3],board[4],board[5]))
    print('-------------')
    print(' {}  | {}  | {}'.format(board[0],board[1],board[2]))

def check_for_win(board):
    for i in range(0,9,3):
        if board[i]==board[i+1]==board[i+2]!='':return True
    for i in range(6,9):
        if board[i]==board[i-3]==board[i-6]!='':return True
    if board[6]==board[4]==board[2]!='':return True 
    if board[0]==board[4]==board[8]!='':return True
        
init_game()
print_board(board)

#main loop
while True:    
    pos=int(input('Choose between 1..9 from dialpad or press 0 for quit'))
    if pos==0:
        break
    if pos>0 and pos<10:
        if board[pos-1]=='':
            board[pos-1]=players[turn]
            if check_for_win(board):
                print_board(board)
                print('Player {} won ! '.format(players[turn]))
                res=input('Play Another ? Y/N')
                if res=='Y':
                    init_game()
                    print_board(board)
                else: break
            elif (9-len([item for item in board if item!='']))==0:
                print('Game Over. No Winner !') 
                res=input('Play Another ? Y/N').lower()
                if res=='y':
                    init_game()
                    print_board(board)
                else: break
            else:    
                turn=abs(turn-1)
                print(turn)
                print_board(board)
        else:
            print('That box is already full. Choose another !')
