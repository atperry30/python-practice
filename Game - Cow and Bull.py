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