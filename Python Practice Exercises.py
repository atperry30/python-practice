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

import random

def guessing_game():

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















