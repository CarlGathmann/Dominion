from src.Dominion.Game import Game

if __name__ == '__main__':
    # INIT: create Game
    game = Game()

    while not game.game_over:
        game.next_round()

    game.print_results()
