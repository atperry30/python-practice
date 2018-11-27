game_play = True

def game_board(board):
    for x in range(7):
        print(' ---'*7)
        print('|'+board[x][0]+'|'+board[x][1]+'|'+board[x][2]+'|'+board[x][3]+'|'+board[x][4]+'|'+board[x][5]+'|'+board[x][6]+'|')
    print(' ---'*7)

def space_lander(board,column,player):
    for x in range(6,-1,-1):
        if board[x][column] == ' - ' and player == 1:
            board[x][column] = ' X '
            break
        elif board[x][column] == ' - ' and player == 2:
            board[x][column] = ' O '
            break

def game_winner(board,player_number):
    global game_play

    #Row Check
    for row in range(7):
        for column in range(4):
            if board[row][column] == board[row][column+1] == board[row][column+2] == board[row][column+3] and board[row][column] != ' - ':
                print('Player %s is the Winner!' % player_number)
                game_play = False
                break

    #Column Check
    for row in range(4):
        for column in range(7):
            if board[row][column] == board[row+1][column] == board[row+2][column] == board[row+3][column] and board[row][column] != ' - ':
                print('Player %s is the Winner!' % player_number)
                game_play = False
                break

    #Downward Diagonal Check
    for row in range(4):
        for column in range(4):
            if board[row][column] == board[row+1][column+1] == board[row+2][column+2] == board[row+3][column+3] and board[row][column] != ' - ':
                print('Player %s is the Winner!' % player_number)
                game_play = False
                break

    #Upward Diagonal Check
    for row in range(4):
        for column in range(3,7):
            if board[row][column] == board[row+1][column-1] == board[row+2][column-2] == board[row+3][column-3] and board[row][column] != ' - ':
                print('Player %s is the Winner!' % player_number)
                game_play = False
                break

    empty_spaces = []
    for row in range(7):
        for column in range(7):
            if board[row][column] == ' - ':
                empty_spaces.append(row)

    if empty_spaces == []:
        print('Game Over')


def player_choice(board,player):
    if player % 2 != 0:
        player_number = 1
    else:
        player_number = 2

    player_column = int(input('Player %s: Please enter your column choice 1-7: ' % player_number))
    player_column -= 1

    space_lander(board,player_column,player_number)

    game_winner(board,player_number)

    game_board(board)


def connect_4():
    board = []
    for x in range(7):
        board.append([' - ',' - ',' - ',' - ',' - ',' - ',' - '])

    while game_play == True:
        for player in range (1,3):
            if game_play == False:
                break
            player_choice(board,player)

connect_4()
