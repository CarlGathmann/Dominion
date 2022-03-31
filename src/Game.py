class Game:

    def __init__(self, players: list):
        self.gameOver = False
        self.players = players
        self.round = 0

    def nextTurn(self):
        for player in self.players:
            for i in range(10):
                print("\n PLAYER", player.name)
                player.takeTurn()
