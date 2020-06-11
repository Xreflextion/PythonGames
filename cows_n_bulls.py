import random

def if_valid(player_choice):
    if player_choice.isalpha():
        return False
    elif player_choice.isdigit() and len(str(player_choice)) == 4:
        return True 
    return False

def cows_n_bulls():
    computer = str(random.randint(1000, 9999))
    print("Lets play Cows and Bulls!")
    print('Type exit to leave the game')
    player_choice = input("Guess a four digit number: ")
    guesses = 0
    while player_choice != 'exit':
        if not if_valid(player_choice):
            print('Invalid guess')
        else:
            cows = 0
            bulls = 0
            c = {}
            g = {}
            for i in range(len(player_choice)):
                if player_choice[i] == computer[i]:
                    bulls += 1
                else: 
                    if player_choice[i] not in g:
                        g[player_choice[i]] = 1
                    else: 
                        g[player_choice[i]] += 1
                    if computer[i] not in c:
                        c[computer[i]] = 1
                    else:
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
            print('You"ve run out of guesses T_T')
            restart = (input("Do you want to try again? (yes/no): "))
            if restart == 'yes':
                cows_n_bulls()
            return
        else:
            player_choice = input("Guess again: ")
    return
