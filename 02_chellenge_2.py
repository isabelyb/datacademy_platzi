"""Escribe un programa que reciba como parámetro “piedra”, “papel”, o “tijera” y 
determine si ganó el jugador 1 o el jugador 2.

Bonus: determina que el ganador sea el jugador que gane 2 de 3 encuentros.

ppt(“piedra”, “papel”) ➞ “El ganador es el jugador 2
"""
import random

play = ["stone", "paper", "scissors"]

player_1 = random.choice(play)
player_2 = random.choice(play)

def stone_paper_scissors(player_1, player_2):
    if player_1 == player_2:
        print ("The game is tied")
    elif ((player_1 == "stone" and player_2 == "scissors") or (player_1 == "scissors" and player_2 == "paper") or (player_1 == "paper" and player_2 == "stone")):
        print ("The  winner is player_1")
    else:
        print ("The  winner is player_2")


if __name__ == '__main__':
    stone_paper_scissors(player_1, player_2)
