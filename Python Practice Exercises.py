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
def game():
    game_start = input('Do you want to play Rock Paper Scissors? (Y/N): ').upper()
    while game_start == 'Y':
        player_one = input('Player One, Enter Rock or Paper or Scissors: ').upper()
        if player_one not in ('ROCK','PAPER','SCISSORS'):
            print('Player One, invalid entry! Please pick: "Rock" or "Paper" or "Scissors"')
            continue
        player_two = input('Player Two, Enter Rock or Paper or Scissors: ').upper()
        if player_two not in ('ROCK','PAPER','SCISSORS'):
            print('Player Two, invalid entry! Please pick: "Rock" or "Paper" or "Scissors"')
            continue
        elif player_one == player_two:
            print('It\'s a tie!')
            if input('Do you want to play again? (Y/N): ').upper() == 'Y':
                continue
            else:
                print('Game Over')
                break
        elif (player_one == 'ROCK' and player_two == 'PAPER') or (player_one == 'PAPER' and player_two == 'SCISSORS') or (player_one == 'SCISSORS' and player_two == 'ROCK'):
            print ('Player Two Wins!')
            if input('Do you want to play again?(Y/N): ').upper() == 'Y':
                continue
            else:
                print('Game Over')
                break
        elif (player_two == 'ROCK' and player_one == 'PAPER') or (player_two == 'PAPER' and player_one == 'SCISSORS')  or (player_two == 'SCISSORS' and player_one == 'ROCK'):
            print ('Player One Wins!')
            if input('Do you want to play again? (Y/N): ').upper() == 'Y':
                continue
            else:
                print('Game Over')
                break
    else:
        print('Game Over')

game()




















