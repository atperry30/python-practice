game_play = True

def game_winner(board,player_number):
    global game_play
    unplayable_spaces = []

    for x in range(3):
        if board[x][0] == board[x][1] == board[x][2] and board[x][0] != ' - ': #Row
            print('Player %s is the Winner!' % player_number)
            game_play = False
            return game_play
            break
        elif board[0][x] == board[1][x] == board[2][x] and board[0][x] != ' - ': #Column
            print('Player %s is the Winner!' % player_number)
            game_play = False
            return game_play
            break
        elif board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' - ': #Diagnal1
            print('Player %s is the Winner!' % player_number)
            game_play = False
            return game_play
            break
        elif board[2][0] == board[1][1] == board[0][2] and board[1][1] != ' - ': #Diagnal2
            print('Player %s is the Winner!' % player_number)
            game_play = False
            return game_play
            break
        elif board[x][0] != ' - ' and board[x][1] != ' - ' and board[x][2] != ' - ':
            unplayable_spaces.append(x)

    if unplayable_spaces == [0,1,2]:
            print('Game Over, No One Wins!')
            game_play = False
            return game_play

def horizontal():
    print(' ---'*3)

def vertical(row,current_board):
    if row == 0:
        print('|'+current_board[0][0]+'|'+current_board[0][1]+'|'+current_board[0][2]+'|')
    if row == 1:
        print('|'+current_board[1][0]+'|'+current_board[1][1]+'|'+current_board[1][2]+'|')
    if row == 2:
        print('|'+current_board[2][0]+'|'+current_board[2][1]+'|'+current_board[2][2]+'|')

def game_board(board):
    for x in range(3):
        horizontal()
        vertical(x,board)
    horizontal()

def player_choice(board,player):
    if player % 2 != 0:
        player_number = 1
    else:
        player_number = 2

    player_space = input('Player %s: Please enter your coordinate as Row,Col from 1 to 3: ' % player_number)
    player_list = player_space.split(',')
    row = int(player_list[0]) -1
    column = int(player_list[1]) -1

    if board[row][column] == ' o ' or board[row][column] == ' x ':
        print('Spot Taken')

    else:
        if player_number == 1:
            board[row][column] = ' x '
        else:
            board[row][column] = ' o '
    game_board(board)

    game_winner(board,player_number)

def tic_tac_toe():
    board = [[' - ',' - ',' - '],[' - ',' - ',' - '],[' - ',' - ',' - ']]
    while game_play == True:
        for player in range (1,3):
            if game_play == False:
                break
            player_choice(board,player)

tic_tac_toe()
