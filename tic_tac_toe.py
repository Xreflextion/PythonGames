def board_tic_tac_toe(board1, board2, game):
    print(board1*3 + '\n' + board2 + str(game[0][0]) + ' ' \
        + board2 + str(game[0][1]) + ' ' + board2 + str(game[0][2]) + ' ' \
        + board2 + '\n' + board1*3 + '\n' + board2 + str(game[1][0]) + ' ' \
        + board2 + str(game[1][1]) + ' ' + board2 + str(game[1][2]) + ' ' \
        + board2 + '\n' + board1*3 + '\n' + board2 + str(game[2][0]) + ' ' \
        + board2 + str(game[2][1]) + ' ' + board2 + str(game[2][2]) + ' ' \
        + board2 + '\n' + board1*3 )

def keep_score(num, scores):
    scores[int(num)] += 1
    return scores

def check_tic_tac_toe(check, num, scores):
    if check[0][0] == check[0][1] and check[0][1] == check[0][2] and check[0][0] != 0:
        print(f'Player {num} is the winner!')
    elif check[1][0] == check[1][1] and check[1][1] == check[1][2] and check[1][0] != 0:
        print(f'Player {num} is the winner!')
    elif check[2][0] == check[2][1] and check[2][1] == check[2][2] and check[2][0] != 0:
        print(f'Player {num} is the winner!')
    elif check[0][0] == check[1][0] and check[1][0] == check[2][0] and check[0][0] != 0:
        print(f'Player {num} is the winner!')
    elif check [0][1] == check[1][1] and check[1][1] == check[2][1] and check[0][1] != 0:
        print(f'Player {num} is the winner!')
    elif check [0][2] == check[1][2] and check[1][2] == check[2][2] and check[0][2] != 0:
        print(f'Player {num} is the winner!')
    elif check [0][0] == check[1][1] and check[1][1] == check[2][2] and check[0][0] != 0:
        print(f'Player {num} is the winner!')
    elif check [0][2] == check[1][1] and check[1][1] == check[2][0] and check[1][1] != 0:
        print(f'Player {num} is the winner!')
    elif 0 in check[0] or 0 in check[1] or 0 in check[2]:
        return False
    else:
        print('There is no winner')
        return True
    keep_score(num, scores)
    return True

def check_if_valid(game, move):
    if move.isalpha():
        return False
    if len(move) != 3 or len(move.split(',')) != 2:
        return False
    move = move.split(',')
    if not move[0].isdigit() or not move[1].isdigit():
        return False
    if int(move[0]) not in [1, 2, 3] or int(move[1]) not in [1, 2, 3]:
        return False
    if game[int(move[0]) - 1][int(move[1]) - 1] != 0:
        return False
    return True

def play_the_game(game, player, symbol, board1, board2):
    game[player[0] - 1][player[1] - 1] = symbol
    return board_tic_tac_toe(board1, board2, game)

def player_choice(player_num, game, board1, board2, symbol, scores):
    while True:
        player = input(f'Player {player_num}: where do you want your move to be? ')
        if player.lower() == 'exit':
            return
        if check_if_valid(game, player):
            break
        else:
            print('Invalid move. Please try again')
    player = player.split(',')
    player[0] = int(player[0])
    player[1] = int(player[1])
    play_the_game(game, player, symbol, board1, board2)
    if check_tic_tac_toe(game, player_num, scores):
        return True
    return player

def main():
    scores = {1: 0, 2: 0}
    while True:
        game = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]
        board1 = ' ---'
        board2 = '| '
        while 0 in game[0] or 0 in game[1] or 0 in game[2]:
            player1 = player_choice(1, game, board1, board2, 'X', scores)
            if player1 == True:
                print(f'Scores: Player 1: {scores[1]}, Player 2: {scores[2]}')
                restart = (input('Do you want to play again? (yes/no) '))
                if restart == 'yes':
                    break
            if player1 == None or player1 == True:
                print('Thanks for playing!')
                return
            player2 = player_choice(2, game, board1, board2, 'O', scores)
            if player2 == True:
                print(f'Scores: Player 1: {scores[1]}, Player 2: {scores[2]}')
                restart = (input('Do you want to play again? (yes/no) '))
                if restart == 'yes':
                    break
            if player2 == None or player2 == True:
                print('Thanks for playing!')
                return

main()

