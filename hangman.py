import random

with open('vocabulary.txt', 'r') as f:
    line = f.read().splitlines()
word = random.sample(line, 1)[0]

def check_the_letter(w, player, number_of_letters, placeholder, num_of_guesses):
    if player not in w:
        print('Incorrect')
        num_of_guesses -= 1
    else:
        for i in w:
            placeholder += 2
            if player == i:
                number_of_letters[placeholder] = i
    number_of_letters = ''.join(number_of_letters)
    print(number_of_letters)
    return num_of_guesses

def check_valid(player):
    if len(player) != 1:
        return False
    elif not player.isalpha():
        return False
    return True

def hangman():
    letter = '_ '
    num_of_letters = letter*len(word)
    modes = {'easy': 10, 'medium': 8, 'hard': 6}
    print("Let's play Hangman!")
    while True:
        difficulty = (input('Choose a difficulty: easy (10 guesses), medium (eight guesses), hard (6 guesses): ')).lower()
        if difficulty not in modes.keys():
            print('Invalid input')
        else:
            num_of_guesses = modes[difficulty]
            break
    print(num_of_letters)
    guesses = set()
    while '_' in num_of_letters:
        if num_of_guesses == 0:
            break
        player = input('Guess a letter: ').upper()
        while True:
            if player in guesses:
                player = input('You have already guessed this letter. Please try again: ').upper()
            elif not check_valid(player):
                player = input('Invalid guess. Please try again: ').upper()
            else:
                break
        if player == 'EXIT':
            break
        placeholder = -2
        num_of_letters = list(num_of_letters)
        num_of_guesses = check_the_letter(word, player, num_of_letters, placeholder, num_of_guesses)
        guesses.add(player)
        print(f'Guesses left: {num_of_guesses}')
        print('Your guesses are: ' + ' '.join(list(guesses)))
    if num_of_guesses == 0:
        print('\    /' + ' \    /' + '\n' + ' \  /' + '   \  /' + '\n' \
        + ' /  \ ' + '  /  \ '+  '\n' + '/    \ ' + '/    \ '\
            + '\n' + ' ___________ ' + '\n' + '     |     | \n'*2 + '     \     / \n' + '      \___/ \n' )
        print('GAME OVER')
        print('WORD: ' + word)
    elif '_' not in num_of_letters:
        print('Congratulations o(〃＾▽＾〃)o! The word was ' + word)
    else:
        return

