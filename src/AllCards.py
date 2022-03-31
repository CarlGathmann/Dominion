from Actioncards.Cellar import Cellar
from Actioncards.Chapel import Chapel
from Actioncards.Festival import Festival
from Actioncards.Harbinger import Harbinger
from Actioncards.Market import Market
from Actioncards.Merchant import Merchant
from Actioncards.Moneylender import Moneylender
from Actioncards.Smithy import Smithy
from Actioncards.Vassal import Vassal
from Actioncards.Village import Village
from Actioncards.Workshop import Workshop
from Moneycards.Copper import Copper
from Moneycards.Gold import Gold
from Moneycards.Silver import Silver
from Victorycards.Curse import Curse

cardlist = {
    0: [Copper(), Curse()],
    2: [Chapel(), Cellar()],
    3: [Village(), Silver(), Merchant(), Workshop(), Vassal(), Harbinger()],
    4: [Smithy(), Moneylender()],
    5: [Market(), Festival()],
    6: [Gold()]
}
