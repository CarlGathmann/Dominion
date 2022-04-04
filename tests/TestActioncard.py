import unittest
from src.Dominion.Actioncards.Cellar import Cellar
from src.Dominion.Player import Player


class TestCellar(unittest.TestCase):
    def setUp(self):
        self.actioncard = Cellar()
        self.player = Player()
        self.player.draw(4)

    def testCellar(self):
        self.player.playActioncard(self.actioncard)
        assert len(self.player.hand) == 4
        assert len(self.player.hand + self.player.discardingPile + self.player.drawingPile + self.player.played_cards) \
               == 10
