from Actioncards.Cellar import Cellar
from Actioncards.Chapel import Chapel
from Actioncards.Festival import Festival
from Actioncards.Market import Market
from Actioncards.Smithy import Smithy
from Actioncards.Village import Village
from Moneycards.Copper import Copper
from Moneycards.Gold import Gold
from Moneycards.Silver import Silver
from Victorycards.Curse import Curse

cardlist = {
        0: [Copper(), Curse()],
        1: [],
        2: [Chapel(), Cellar()],
        3: [Village(), Silver()],
        4: [Smithy()],
        5: [Market(), Festival()],
        6: [Gold()]
}
