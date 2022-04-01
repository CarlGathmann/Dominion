import random

from src.Game import Game
from src.Player import Player

ROUNDS = 50

if __name__ == '__main__':
    # INIT: create Players
    game = Game()

    for _ in range(ROUNDS):
        game.nextRound()
