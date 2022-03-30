from Actioncards.Market import Market
from Actioncards.Smithy import Smithy
from Actioncards.Village import Village
from Player import Player

if __name__ == '__main__':
    # INIT: create Players

    market = Market()
    smithy = Smithy()
    village = Village()
    playerOne = Player()
    playerTwo = Player()
    playerOne.hand.append(market)
    playerOne.hand.append(village)
    playerOne.hand.append(smithy)
    # playerOne.printDeck()
    playerOne.takeTurn()
    playerOne.printAttributes()

