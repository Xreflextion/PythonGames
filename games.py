import argparse
from guess_the_number import guess_the_number
from rock_paper_scissors import rock_paper_scissors
from cows_n_bulls import cows_n_bulls
from tic_tac_toe import tic_tac_toe
from hangman import hangman

def choose_game(args):
    if args.game == 'guess_num':
        guess_the_number()
    elif args.game == 'hangman':
        hangman()
    elif args.game == 'rps':
        rock_paper_scissors()
    elif args.game == 'cows_n_bulls':
        cows_n_bulls()
    elif args.game == 'ttt':
        tic_tac_toe()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Project related to simple python games')
    parser.add_argument('--game', type=str, required=True, choices=['hangman', 'rps', 'guess_num', 'ttt', 'cows_n_bulls'], help='Choose which game play')
    args = parser.parse_args()

    choose_game(args)

