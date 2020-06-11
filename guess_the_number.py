import random 

def choose_difficulty(difficulty):
    numbers = None
    difficulty = difficulty.lower()
    if difficulty == 'easy':
        numbers = [random.randint(1, 9), 9]
    elif difficulty == 'medium':
        numbers = [random.randint(1, 50), 50]
    elif difficulty == 'hard':
        numbers = [random.randint(1, 100), 100]
    return numbers

def check_valid(player_choice, numbers):
    if player_choice.isalpha():
        return False
    elif player_choice.isdigit() and int(player_choice) <= int(numbers[1]):
        return True
    return False

def evaluate_guess(player_choice, number, num_of_guesses, numbers):
    player_choice = int(player_choice)
    if number > player_choice:
        print("You guessed too low!")
    elif number < player_choice:
        print("you guessed too high!")
    elif number == player_choice:
        print(f"Congratulations! You guessed it right! The number was {number}.")
        print(f"You guessed it in {num_of_guesses} guess(es)!")
        restart = (input('Do you want to play again? (yes/no) '))
        if restart.lower() == 'yes':
            return True
        else:
            return False
    return

def guess_the_number():
    print("Let's play a guessing game! Type exit anytime to quit.")
    player_choice = None
    while player_choice != 'exit':
        difficulty = (input("Choose a difficulty (easy, medium, hard): "))
        if difficulty == 'exit':
            break
        else:
            numbers = choose_difficulty(difficulty)
            if numbers == None:
                print('Invalid input')
            else:
                number = int(numbers[0])
                player_choice = (input(f"Guess a number between 1 and {numbers[1]}: "))
                num_of_guesses = 0
                while player_choice != 'exit': 
                    if check_valid(player_choice, numbers):
                        num_of_guesses += 1
                        play_again = evaluate_guess(player_choice, number, num_of_guesses, numbers)
                        if play_again:
                            break
                        elif play_again == False:
                            print('Thanks for playing!')
                            return 
                    else:
                        print('Invalid guess')
                    if player_choice != number:
                        player_choice = (input("Guess again: "))
                    
