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
answer	6655
6666	2 cow, 0 bull
5555	2 cow, 0 bull
6655	0 cow, 4 bull
6565	2 cow, 2 bull
"""
















