import random

def update_scores(scores, winner):
    if winner == 'c':
        scores['computer'] += 1
    else:
        scores['player'] += 1
    return 

def rock_paper_scissors():
    rps = ["rock", "paper", "scissors"]
    print("Let's play 'Rock, Paper, Scissors!'")
    scores = {'computer': 0, 'player': 0}
    while True:
        player_choice = input("Rock, paper, or scissors: ").lower()
        computer = random.sample(rps, 1)[0]
        while player_choice not in rps:
            print("Invalid.")
            player_choice = input("Please try again: ")
        print("Computer picked this: " + computer)
        if computer == "rock" and player_choice == "scissors" or \
            computer == "scissors" and player_choice == "paper" or \
            computer == "paper" and player_choice == "rock":
            print("Computer won!")
            update_scores(scores, 'c')
        elif computer == player_choice:
            print ("It's a tie!")
        else: 
            print ("Congratulations! You won!")
            update_scores(scores, 'p')
        print(f"Here are the scores: Computer = {scores['computer']}, Player = {scores['player']}")
        print("Do you want to play again?")
        yes_or_no = input("Yes or no: ").lower()
        if yes_or_no == "yes":
            print("*******************************")
            print("New game!")
        else:
            break