#!/usr/bin/env python

# class Play:
#     def can_beat(self, play):
#         self.play
#
# class Scissors: Play:
#     def can_beat(self, play):
#         if play is Payer:
#             return true
#         elif:
#             return false
#
#
# player1Play.can_beat(player2_play)


def get_user_input():
    player = ''
    while player not in ('ROCK','PAPER','SCISSORS'):
        player = input('Player One, Enter Rock or Paper or Scissors: ').upper()

        if player not in ('ROCK','PAPER','SCISSORS'):
            print('Player One, invalid entry! Please pick: "Rock" or "Paper" or "Scissors"')

def decide_game(player_one, player_two):
    if player_one == player_two:
        print('It\'s a tie!')

    elif (player_one == 'ROCK' and player_two == 'PAPER') or (player_one == 'PAPER' and player_two == 'SCISSORS') or (player_one == 'SCISSORS' and player_two == 'ROCK'):
        print ('Player Two Wins!')

    elif (player_two == 'ROCK' and player_one == 'PAPER') or (player_two == 'PAPER' and player_one == 'SCISSORS')  or (player_two == 'SCISSORS' and player_one == 'ROCK'):
        print ('Player One Wins!')


###Exercise 8: Rock Paper Scissors
def game():
    game_start = input('Do you want to play Rock Paper Scissors? (Y/N): ').upper()

    while game_start == 'Y':

        player_one = get_user_input()
        player_two = get_user_input()

        decide_game(player_one, player_two)

        game_start = input('Do you want to play again? (Y/N): ').upper()

    print('Game Over')

game()



















