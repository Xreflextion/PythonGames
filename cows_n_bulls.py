import random
import collections

def choose_difficulty(difficulty):
    computer = None
    if difficulty == 'easy':
        numbers = random.sample(range(10), 4)
        computer = str(''.join(map(str, numbers)))
    elif difficulty == 'hard':
        computer = str(random.randint(1000, 9999))
    return computer

def if_valid(player_choice):
    if player_choice.isalpha():
        return False
    elif player_choice.isdigit() and len(str(player_choice)) == 4:
        return True 
    return False

def cows_n_bulls():
    print("Let's play Cows and Bulls!")
    difficulty = None
    player_choice = None
    while player_choice != 'exit' or difficulty != 'exit':
        difficulty = (input('Choose a difficulty: easy or hard: '))
        computer = choose_difficulty(difficulty)
        if computer == None:
            print('Invalid input')
        else:
            player_choice = input("Guess a four digit number: ")
            guesses = 0
            while player_choice != 'exit':
                if not if_valid(player_choice):
                    print('Invalid guess')
                else:
                    cows = 0
                    bulls = 0
                    c = collections.defaultdict(int)
                    g = collections.defaultdict(int)
                    for i in range(len(player_choice)):
                        if player_choice[i] == computer[i]:
                            bulls += 1
                        else: 
                            g[player_choice[i]] += 1
                            c[computer[i]] += 1
                    for l in g:
                        if l in c:
                            while g[l] > 0 and c[l] > 0:
                                cows += 1
                                g[l] -= 1
                                c[l] -= 1
                    guesses += 1
                    print(f'{bulls} bull(s)')
                    print(f'{cows} cow(s)')
                    print(f'{10-guesses} guesses left')
                if player_choice == computer:
                    print(f'Congratulations (/^▽^)/! You got it in {guesses} guess(es)!')
                    print(f'The number was {computer}.')
                    restart = (input("Do you want to play again? (yes/no): "))
                    if restart == 'yes':
                        cows_n_bulls()
                    return
                elif guesses == 10:
                    print('GAME OVER')
                    print("You've run out of guesses T_T")
                    print(f'Number: {computer}')
                    restart = (input("Do you want to try again? (yes/no): "))
                    if restart == 'yes':
                        break
                    return
                else:
                    player_choice = input("Guess again: ")
            return

