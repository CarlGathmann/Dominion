import random

from src.Game import Game
from src.Player import Player

if __name__ == '__main__':
    # INIT: create Players
    game = Game()

    for _ in range(5):
        game.nextRound()
