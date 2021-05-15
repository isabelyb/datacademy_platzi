"""Bonus: determina que el ganador sea el jugador que gane 2 de 3 encuentros.
"""

import random


play = ["stone", "paper", "scissors"]
player_1 = ""
player_2 = ""


def main():
    game = 1
    winner = []

    while game < 4:
        win = stone_paper_scissors(player_1, player_2)
        print(f"Win play {game}: {win}")
        winner.append(win)
        game += 1
    winner_1 = winner.count("Player_1")
    winner_2 = winner.count("Player_2")
    
    if winner_1 >= 2:
        great_winner = "Player_1"
    elif winner_2 >= 2:
        great_winner = "Player_2"
    else:
        great_winner = "There aren't winner"
    print(f"The great winner is: {great_winner} ")    


def stone_paper_scissors(player_1, player_2):
    player_1 = random.choice(play)
    player_2 = random.choice(play)
    win = ""
    if player_1 == player_2:
        win = "The game is tied"
    elif ((player_1 == "stone" and player_2 == "scissors") or (player_1 == "scissors" and player_2 == "paper") or (player_1 == "paper" and player_2 == "stone")):
        win = "Player_1"
    else:
        win = "Player_2"
    return win


if __name__ == '__main__':
    main()
