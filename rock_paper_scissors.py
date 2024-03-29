import random

def update_scores(scores, winner):
    if winner == 'c':
        scores['computer'] += 1
    else:
        scores['player'] += 1
    return 

def rock_paper_scissors():
    rps = ["rock", "paper", "scissors"]
    ab = ['r', 'p', 's']
    abbrev = {'rock': 'r', 'paper': 'p', 'scissors': 's'}
    print("Let's play 'Rock, Paper, Scissors!'")
    scores = {'computer': 0, 'player': 0}
    player_choice = input("Rock(R), paper(P), or scissors(S): ").lower()
    while player_choice != 'exit':
        computer = random.sample(rps, 1)[0]
        while player_choice not in rps and player_choice not in ab:
            print("Invalid.")
            player_choice = input("Please try again: ")
            if player_choice == 'exit':
                return
        print("Computer picked this: " + computer)
        if computer == "rock" and (player_choice == "scissors" or player_choice == 's') or \
            computer == "scissors" and (player_choice == "paper" or player_choice == 'p') or \
            computer == "paper" and (player_choice == "rock" or player_choice == 'r'):
            print("Computer won!")
            update_scores(scores, 'c')
        elif computer == player_choice or abbrev[computer] == player_choice:
            print ("It's a tie!")
        else: 
            print ("Congratulations! You won (￣▽￣)ノ!")
            update_scores(scores, 'p')
        print(f"Here are the scores: Computer = {scores['computer']}, Player = {scores['player']}")
        print("Do you want to play again?")
        yes_or_no = input("Yes or no: ").lower()
        if yes_or_no == "yes":
            print("*******************************")
            print("New game!")
            player_choice = input("Rock, paper, or scissors: ").lower()
        else:
            print('Thanks for playing!')
            return