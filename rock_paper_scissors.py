import random

def rock_paper_scissors():
    rps = ["rock", "paper", "scissors"]
    print("Let's play 'Rock, Paper, Scissors!'")
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
        elif computer == player_choice:
            print ("It's a tie!")
        else: 
            print ("Congratulations! You won!")
        print("Do you want to play again?")
        yes_or_no = input("Yes or no: ").lower()
        if yes_or_no == "yes":
            print("*******************************")
            print("New game!")
        else:
            break