from src.Cardtypes.Victorycard import Victorycard
from src.Game import Game

if __name__ == '__main__':
    # INIT: create Game
    game = Game()

    while not game.gameOver:
        game.nextRound()

    game.printResults()
