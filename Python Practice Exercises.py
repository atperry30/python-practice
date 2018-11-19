# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 16:10:37 2018

@author: peral6e
"""


###Exercise 1: Character Input
"""
from datetime import datetime

name = input('What is your name? ')
age = input('What is your age? ')
repeat = int(input('State a number between 1-10 '))

year =  str(100-int(age)+datetime.now().year)

for x in range (0,repeat):
    print('Hello %s! Your current age is %s, which means you will be 100 in the year %s' % (name, age, year))
"""

###Exercise 2: Odd Or Even
"""
number = int(input('Please enter number: '))

if number % 2 == 0:
    print('Number was even')
else:
    print('Number was odd')
"""

###Exercise 3: List Less Than Ten
"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
def fun(series):
    for x in series:
        if x < 5:
            b.append(x)
    return b

print(fun(a))
"""

###Exercise 4: Divisors
"""
num = int(input('Please enter number: '))
def divisors(number):
    list_num = []
    for x in range(1,number+1):
        if number % x == 0:
            list_num.append(x)
    return list_num

print(divisors(num))
"""

###Exercise 5:List Overlap
"""
import random
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = sorted(random.sample(range(1, 100), 20))
d = sorted(random.sample(range(1, 100), 10))

def list_comp(list1,list2):
    list3 = []
    for x in list1:
        if x in list2 and x not in list3:
            list3.append(x)
    return sorted(list3)

print(c)
print(d)
print(list_comp(c,d))
"""

###Exercise 6: String Lists
"""
string = input('Enter String: ')

def palindrome(string):
    if string[::] == string[::-1]:
        print('It\'s a palindrome!')
    else:
        print('It\'s not a palindrome!')

palindrome(string)
"""

###Exercise 7:List Comprehensions
"""
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = [x for x in a if x % 2 == 0]
print(b)
"""

###Exercise 8: Rock Paper Scissors
"""
def get_user_input():
    player = ''
    while player not in ('ROCK','PAPER','SCISSORS'):
        player = input('Enter Rock or Paper or Scissors: ').upper()

        if player not in ('ROCK','PAPER','SCISSORS'):
            print('Invalid Entry! Please Pick: "Rock" or "Paper" or "Scissors"')

def decide_game(player_one, player_two):
    if player_one == player_two:
        print('It\'s a tie!')

    elif (player_one == 'ROCK' and player_two == 'PAPER') or (player_one == 'PAPER' and player_two == 'SCISSORS') or (player_one == 'SCISSORS' and player_two == 'ROCK'):
        print ('Player Two Wins!')

    elif (player_two == 'ROCK' and player_one == 'PAPER') or (player_two == 'PAPER' and player_one == 'SCISSORS')  or (player_two == 'SCISSORS' and player_one == 'ROCK'):
        print ('Player One Wins!')

def RockPaperScissors():
    game_start = input('Do you want to play Rock Paper Scissors? (Y/N): ').upper()

    while game_start == 'Y':

        player_one = get_user_input()
        player_two = get_user_input()

        decide_game(player_one, player_two)

        game_start = input('Do you want to play again? (Y/N): ').upper()

    print('Game Over')

RockPaperScissors()
"""

###Exercise 9:Guessing Game One
"""
def decide_game(guess,answer):

    if guess < answer:
        print('Too Low! Guess again or type "exit" to exit game!')

    elif guess > answer:
        print('Too High! Guess again or type "exit" to exit game!')

def guess_mechanism():
    guess = input('Guess a number between 1-9: ')
    if guess == 'exit':
        guess = 10
    guess = int(guess)
    return guess

def guessing_game():

    import random

    guess = guess_mechanism()
    answer = random.randint(1,10)
    count = 0

    while guess != answer:

        if guess > 9:
            print ('Game Over')
            break

        decide_game(guess,answer)

        guess = guess_mechanism()

        count += 1

    else:
        print('You guessed it! It took you %s guesse(s)' % count)

guessing_game()
"""

###Exercise 10: List Overlap Comprehensions
"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = [x for x in a if x in b]
d = []
for x in c:
    if x not in d:
        d.append(x)

print(d)
"""

###Exercise 11: Check Primality Functions
"""
def guess_input():
    return input('Please guess an interger or enter \'Exit\' to stop game: ')

def input_validation(guess):
    if guess.upper() == 'EXIT':
        return False

    else:
        return True

def prime_check(number):
    divisor_list =[x for x in range(2,number) if number % x == 0]

    if divisor_list == []:
        print('Number is prime.')

    else:
        print('Number is not prime.')

def prime_guess_game():
    guess = guess_input()

    while input_validation(guess):
        prime_check(int(guess))
        guess = guess_input()

    else:
        print('Game Over')

prime_guess_game()
"""

###Exercise 12: List Ends
"""
a = [5, 10, 15, 20, 25]

def list_ends(series):
    new_list = []
    new_list.append(series[0])
    new_list.append(series[len(series)-1])
    return new_list

print(list_ends(a))
"""

###Exercise 13:Fibonacci
"""
def Fibonacci():
    number = int(input('How many Fibonacci numbers do you want? '))
    series = []
    if number == 1:
        series.append(1)
    if number == 2:
        series = [1,1]
    if number >= 3:
        series = [1,1]
        for x in range(number-2):
            series.append(series[x]+series[x+1])
    return series

print(Fibonacci())
"""

###Exercise 14: List Remove Duplicates
"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def list_overlap(a,b):
    c = [x for x in a if x in b]
    c = set(c)
    c = sorted(list(c))
    return(c)

print(list_overlap(a,b))
"""

###Exercise 15: Reverse Word Order
"""
s = 'this is a test'
def reverse(s):
    s = s.split()
    s = s[::-1]
    s = " ".join(s)
    return s

print(reverse(s))
"""

###Exercise 16: Password Generator
"""
def password_generator(length):
    import random
    import string
    letters = string.ascii_letters
    letters = list(letters)
    numbers = [x for x in range(0,10)]
    symbols = string.punctuation
    symbols = list(symbols)
    source = letters+numbers+symbols
    password = []
    for x in range(1,length):
        password.append(str(random.choice(source)))
    password = ''.join(password)
    return password

print(password_generator(25))
"""



###Exercise 18: Cows And Bulls
"""
def guessing_mechanism(guess,number,guess_count):
    cow = 0
    bull = 0

    guess = list(guess)
    number = list(number)

    if guess == number:
        print('You Won! It took you %s guesses!' % (guess_count))

    else:
        for x in range(4):
            if guess[x] == number[x]:
                cow += 1
                guess[x] = 'guess_removed'
                number[x] = 'answer_removed'

        for x in range(4):
            if guess[x] in number:
                bull += 1
                number.remove(guess[x])

        guess = ''.join(guess)
        number = ''.join(number)
        print('%s cow(s), %s bull(s)' % (cow,bull))

def cows_and_bulls():
    import random
    number = []
    for x in range(4):
        number.append(str(random.randint(0,9)))
    number = ''.join(number)
    print('Welcome to the Cows and Bulls Game!')
    #print(number)
    guess_count = 1
    guess = ''
    if guess != number:
        while guess != number:
            guess = str(input('Please Guess a 4 Digit Number '))
            guessing_mechanism(guess,number,guess_count)
            guess_count +=1

cows_and_bulls()
"""


###Exercise 20: Element Search
"""
a = [x for x in range(0,3000) if x % 3 != 0]

def middle_index_calc(series):
    if len(series) % 2 == 0:
        return int(len(series)/2)

    else:
        return int((len(series)-1)/2)

def binary_search(series):
    number = int(input('Enter number to find in list: '))

    while len(series) >= 1:

        start_index = 0
        end_index = len(series)-1
        middle_index = middle_index_calc(series)

        start_value = series[start_index]
        end_value = series[end_index]
        middle_value= series[middle_index]

        if number == middle_value:
            #print(series)
            #print(start_value)
            #print(middle_value)
            #print(end_value)
            print('In List')
            break

        elif number < start_value or number > end_value:
            #print(series)
            #print(start_value)
            #print(middle_value)
            #print(end_value)
            print('Not In List')
            break

        elif number >= start_value and number < middle_value:
            #print(series)
            #print(start_value)
            #print(middle_value)
            #print(end_value)
            series = series[:middle_index]

        elif number <= end_value and number > middle_value:
            series = series[middle_index:]
            #print(series)
            #print(start_value)
            #print(middle_value)
            #print(end_value)

binary_search(a)
"""

###Exercise 21/22: Write To A File/Read from File
"""
def password_generator(length):
    import random
    import string
    letters = string.ascii_letters
    letters = list(letters)
    numbers = [x for x in range(0,10)]
    symbols = string.punctuation
    symbols = list(symbols)
    source = letters+numbers+symbols
    password = []
    for x in range(1,length):
        password.append(str(random.choice(source)))
    password = ''.join(password)
    return password

#file_name = str(input('What would you like to name you password file? '))
file_name = 'Test_Password_List'

password_list = []
for x in range(0,20):
    password_counter = 'Password #'+str(x)+':'
    password_list.append(password_counter)
    password_list.append(password_generator(25))
password_string = '\n'.join(password_list)

with open(file_name+'.txt', 'w') as open_file:
    open_file.write(password_string)

with open('Test_Password_List.txt', 'r') as open_file:
    password = open_file.read()
    print(password)
"""

###Exercise 23: File Overlap:
"""
prime_number = open('primenumbers.txt','r')
prime_number_string = prime_number.read()
happy_number = open('happynumbers.txt','r')
happy_number_string = happy_number.read()

prime_number_list = prime_number_string.split()
happy_number_list = happy_number_string.split()

overlap_list = [x for x in prime_number_list if x in happy_number_list]

print(overlap_list)
"""

#Exercise 24: Draw a Game Board
"""
def horizontal(size):
    print(' ---'*size)

def vertical(size):
    print('|   '*(size+1))

def game_board():
    #size = int(input('What size grid are you intrested in? '))
    size = 3

    for x in range(size):
        horizontal(size)
        vertical(size)

    horizontal(size)

game_board()
"""


#Exercise 25: Guessing Game Two
"""
def middle_index_calc(series):
    if len(series) == 1:
        return 0
    if len(series) % 2 == 0:
        return int(len(series)/2)
    else:
        return int((len(series)-1)/2)


def computer_guess_mechanism(guess_range):
    computer_guess = guess_range[middle_index_calc(guess_range)]
    return computer_guess

def guessing_game():
    answer_pool = [x for x in range(0,1001)]
    correct_answer = int(input('What number do you want to computer to guess between 0 and 1,000? '))
    computer_guess = computer_guess_mechanism(answer_pool)
    guess_count = 1

    if correct_answer < 0 or correct_answer >= 1001:
        print('Answer outside of range')

    while computer_guess != correct_answer:

        if correct_answer > computer_guess:
            answer_pool = answer_pool[middle_index_calc(answer_pool):]
            computer_guess = computer_guess_mechanism(answer_pool)
            guess_count += 1

        elif correct_answer < computer_guess:
            answer_pool = answer_pool[:middle_index_calc(answer_pool)]
            computer_guess = computer_guess_mechanism(answer_pool)
            guess_count += 1

    else:
        print('I guessed it! The value is %s. It took me %s guess(es)' % (computer_guess,guess_count))


guessing_game()
"""

#Exercise 26/27/29: Tic Tac Toe Draw/Game

"""
def winner_message(player_number,x,y):
    game_play = True
    if x == 4 and y == 4:
        print('No Winner!')
    else:
        print('Player %s is the Winner!' % player_number)
        game_play == False
"""
"""
def game_winner(board,player_number):
    game_play = True
    for x in range(3):
        if board[x][0] == board[x][1] == board[x][2] and board[x][0] != ' - ': #Row
            print('Player %s is the Winner!' % player_number)
            game_play == False
            break
        elif board[0][x] == board[1][x] == board[2][x] and board[0][x] != ' - ': #Column
            print('Player %s is the Winner!' % player_number)
            game_play == False
            break
        elif board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' - ': #Diagnal1
            print('Player %s is the Winner!' % player_number)
            game_play == False
            break
        elif board[2][0] == board[1][1] == board[0][2] and board[1][1] != ' - ': #Diagnal2
            print('Player %s is the Winner!' % player_number)
            game_play == False
            break

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

    game_winner(board,player_number)

    if board[row][column] == ' o ' or board[row][column] == ' x ':
        print('Spot Taken')

    else:
        if player_number == 1:
            board[row][column] = ' x '
        else:
            board[row][column] = ' o '
    game_board(board)

def tic_tac_toe():
    board = [[' - ',' - ',' - '],[' - ',' - ',' - '],[' - ',' - ',' - ']]
    game_play = True
    while game_play == True:
        for player in range (1,10):
            player_choice(board,player)
    else:
        print('Game Over!')

tic_tac_toe()
"""

#Exercise 28: Max of Three
"""
def max_game():
    three_string = input('Provide 3 numbers in this format 1,2,3 and I will return the largest: ')
    three_list = three_string.split(',')
    three_int_list = list(map(int, three_list))
    three_list_sorted = sorted(three_int_list)
    print(three_list_sorted[len(three_list_sorted)-1])

max_game()

"""
#Exercise 30/31/32: Pick Word/Guess Letters/Hangman
with open('Scrabble_Word_List.txt', 'r') as open_file:
    word_list_text = open_file.read()
    word_list = word_list_text.split()

def pick_word():
    import random
    return random.choice(word_list)

def hangman_image(wrong_guess_count):
    hangman = [['______       '],
               ['|    |       '],
               ['|    O       '],
               ['|   \|/      '],
               ['|   / \      '],
               ['|            '],
               ['|            ']]

    if wrong_guess_count == 0:
        hangman[2] = ['|            ']
        hangman[3] = ['|            ']
        hangman[4] = ['|            ']
    if wrong_guess_count == 1:
        hangman[3] = ['|            ']
        hangman[4] = ['|            ']
    elif wrong_guess_count == 2:
        hangman[3] = ['|    |       ']
        hangman[4] = ['|            ']
    elif wrong_guess_count == 3:
        hangman[3] = ['|   \|       ']
        hangman[4] = ['|            ']
    elif wrong_guess_count == 4:
        hangman[4] = ['|            ']
    elif wrong_guess_count == 5:
        hangman[4] = ['|   /        ']

    for x in hangman:
        print(''.join(x))

def hangman():
    correct_word = pick_word()
    #correct_word = 'EVAPORATE'
    correct_letters = list(correct_word)

    word_length = len(correct_word)

    letter_list = []
    for x in range(word_length):
        letter_list.append('_')

    print('Welcome to Hangman!')
    print(' '.join(letter_list))

    guessed_letter_list = []

    wrong_guess_count = 0

    while letter_list != correct_letters and wrong_guess_count < 6:
        guess_letter = input('Please Guess a Letter: ')
        guess_letter = guess_letter.upper()

        if guess_letter == 'EXIT':
            break

        if guess_letter in guessed_letter_list:
            print('You already guessed that letter, try again!')
            continue

        guessed_letter_list.append(guess_letter)

        if guess_letter not in correct_letters:
            wrong_guess_count += 1
            hangman_image(wrong_guess_count)
            print('Incorrect Guess! You have %s guess(es) left.' % (6-wrong_guess_count))
            continue

        if guess_letter in correct_letters:
            for x in range(word_length):
                if guess_letter == correct_letters[x]:
                    letter_list[x] = guess_letter
            hangman_image(wrong_guess_count)

        print(' '.join(letter_list))

    if letter_list != correct_letters:
        print('Sorry, you lost!')
    else:
        print('You Won!')

hangman()

