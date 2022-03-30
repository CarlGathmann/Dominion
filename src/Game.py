class Game:
    def __init__(self):
        self.gameOver = False
        self.round = 0

    def nextRound(self):
        self.round += 1
