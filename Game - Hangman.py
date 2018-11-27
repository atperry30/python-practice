def word_generator():
    with open('Scrabble_Word_List_Copy.txt', 'r') as open_file:
        word_list_text = open_file.read()
        word_list = word_list_text.split()

    for x in word_list[:]:
        if len(x) <= 4:
            word_list.remove(x)

    return word_list

def pick_word():
    import random
    return random.choice(word_generator())

def hangman_image(wrong_guess_count):
    hangman = [['______       '],
               ['|    |       '],
               ['|    O       '],
               ['|   \|/      '],
               ['|  _/ \_     '],
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
    elif wrong_guess_count == 6:
        hangman[4] = ['|   / \     ']
    elif wrong_guess_count == 7:
        hangman[4] = ['|  _/ \      ']

    for x in hangman:
        print(''.join(x))

def hangman():
    correct_word = pick_word()

    correct_letters = list(correct_word)

    word_length = len(correct_word)

    letter_list = []
    for x in range(word_length):
        letter_list.append('_')

    print('Welcome to Hangman! Type "exit" to leave game. Type "letters" to see guessed letters.')
    print(' '.join(letter_list))

    guessed_letter_list = []

    wrong_guess_count = 0

    while letter_list != correct_letters and wrong_guess_count < 8:
        guess_letter = input('Please Guess a Letter: ')
        guess_letter = guess_letter.lower()

        if guess_letter == 'exit':
            break

        if guess_letter == 'letters':
            print(guessed_letter_list)
            continue

        if guess_letter in guessed_letter_list:
            print('You already guessed that letter, try again!')
            print(guessed_letter_list)
            continue

        guessed_letter_list.append(guess_letter)
        guessed_letter_list = sorted(guessed_letter_list)

        if guess_letter not in correct_letters:
            wrong_guess_count += 1
            hangman_image(wrong_guess_count)
            print('Incorrect Guess! You have %s guess(es) left.' % (8-wrong_guess_count))
            print(' '.join(letter_list))
            continue

        if guess_letter in correct_letters:
            for x in range(word_length):
                if guess_letter == correct_letters[x]:
                    letter_list[x] = guess_letter
            hangman_image(wrong_guess_count)

        print(' '.join(letter_list))

    if letter_list != correct_letters:
        print('Sorry, you lost!. The word was: %s.' % correct_word)
    else:
        print('You Won!')

hangman()