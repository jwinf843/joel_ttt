
def create_board():
    board = {}
    board['a1'] = '-'
    board['b1'] = '-'
    board['c1'] = '-'
    board['a2'] = '-'
    board['b2'] = '-'
    board['c2'] = '-'
    board['a3'] = '-'
    board['b3'] = '-'
    board['c3'] = '-'
    board['turn'] = 0
    board['board'] = '''
   a     b     c
      |     |     
1  {a1}  |  {b1}  |  {c1}  
 _____|_____|_____
      |     |     
2  {a2}  |  {b2}  |  {c2}  
 _____|_____|_____
      |     |     
3  {a3}  |  {b3}  |  {c3}  
      |     |'''
    return board

def display_board(board):
    print(board['board'].format(
        a1 = board['a1'],
        b1 = board['b1'],
        c1 = board['c1'], 
        a2 = board['a2'],
        b2 = board['b2'], 
        c2 = board['c2'], 
        a3 = board['a3'], 
        b3 = board['b3'],
        c3 = board['c3']
    ))

def make_move(board):
    turn = board['turn']
    marker = 'O'
    if turn % 2 == 0:
        marker = 'X'
    flag = True
    while flag:        
        square = input('Choose a Coordinate to place your {}: '.format(marker))
        print(square)
        if board[square] == '-':
            if square in board.keys():
                print('Okay!')
                board[square] = marker
                flag = False
            else:
                print('Please choose a proper coordinate')
        else:
            print('That square already has a mark!')

def check_board(board):
    pass


def tic_tac_toe():
    board = create_board()
    
    game_won = False
    
    while not game_won:
        display_board(board)
        make_move(board)
        board['turn'] += 1
    
    
tic_tac_toe()
# board = create_board()
# print(board.keys())

# if 'a1' in board.keys():
#     print('found')
