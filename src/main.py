from Game import Game
from Player import Player

if __name__ == '__main__':
    # INIT: create Players
    playerOne = Player()
    game = Game([playerOne])

    game.nextTurn()
