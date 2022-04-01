import unittest
from src.Actioncards.Cellar import Cellar
from src.Player import Player


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
