from src.Game import Game

ROUNDS = 1000

if __name__ == '__main__':
    # INIT: create Players
    game = Game()

    for _ in range(ROUNDS):
        game.nextRound()
        print(len(game.gameCards.keys()))
