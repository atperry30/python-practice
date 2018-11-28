import random
game_play = True
variable = 0

###Game Board####
def vertical(row,current_board):
    if row == 0:
        print('|'+current_board[0][0]+'|'+current_board[0][1]+'|'+current_board[0][2]+'|')
    if row == 1:
        print('|'+current_board[1][0]+'|'+current_board[1][1]+'|'+current_board[1][2]+'|')
    if row == 2:
        print('|'+current_board[2][0]+'|'+current_board[2][1]+'|'+current_board[2][2]+'|')

def game_board(board):
    for x in range(3):
        print(' ---'*3)
        vertical(x,board)
    print(' ---'*3)


###Who Goes Frist###
def goes_first():
    global variable
    variable = random.randint(1,2)
    if variable == 1:
        print('Computer goes first')
        return variable

    if variable == 2:
        print('You goes first')
        return variable



###Free Space###
def is_space_free(row,column,board):
    global space
    if board[row][column] == ' - ':
        space = 'free'
        return space
    else:
        space = 'taken'
        return space


###Player Move###
def player_move(board):
    player_space = input('Please enter your coordinate as Row,Col from 1 to 3: ' )
    player_list = player_space.split(',')
    row = int(player_list[0]) -1
    column = int(player_list[1]) -1
    if is_space_free(row,column,board) == 'taken':
        print('Spot Taken')
    else:
        board[row][column] = ' x '

###Computer Move###
def computer_move(board):
    value = True
    for x in range (0,3):
        for y in range(0,3):
            while value == True:
                if is_space_free(x,y,board) == 'free':
                    if game_winner(board) == 'False':
                        board[x][y] = ' o '
                        value = False
                        break
                    else:
                        board[x][y] = ' o '
                        value = False
                        break

###Winning Message###
def winning_message(x,y,board):
    if board[x][y] == ' x ':
        print('You are the Winner!')
    if board[x][y] == ' o ':
        print('The computer is the Winner!')


###Game Winner###
def game_winner(board):
    global game_play
    unplayable_spaces = []

    for x in range(3):
        if board[x][0] == board[x][1] == board[x][2] and board[x][0] != ' - ': #Row
            winning_message(x,0,board)
            game_play = False
            return game_play
            break

        elif board[0][x] == board[1][x] == board[2][x] and board[0][x] != ' - ': #Column
            winning_message(0,x,board)
            game_play = False
            return game_play
            break

        elif board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' - ': #Diagnal1
            winning_message(0,0,board)
            game_play = False
            return game_play
            break

        elif board[2][0] == board[1][1] == board[0][2] and board[2][0] != ' - ': #Diagnal2
            winning_message(2,0,board)
            game_play = False
            return game_play
            break

        elif board[x][0] != ' - ' and board[x][1] != ' - ' and board[x][2] != ' - ':
            unplayable_spaces.append(x)

    if unplayable_spaces == [0,1,2]:
            print('Game Over, No One Wins!')
            game_play = False
            return game_play


def tic_tac_toe():
    board = [[' - ',' - ',' - '],[' - ',' - ',' - '],[' - ',' - ',' - ']]
    goes_first()
    if variable == 1:
        while game_play == True:
            game_board(board)
            game_winner(board)
            computer_move(board)
            game_winner(board)
            player_move(board)
    if variable == 2:
        while game_play == True:
            game_board(board)
            game_winner(board)
            player_move(board)
            game_winner(board)
            computer_move(board)


tic_tac_toe()