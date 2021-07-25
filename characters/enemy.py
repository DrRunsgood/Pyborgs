from .character import *
from items.container import *
from items.weapon import *
from items.armor import *

class Enemy(Character):
    def __init__(self, name, level, maxhp, str, apt, dex, exp, eweap, ehead, echest, earms, elegs, efeet):
        Character.__init__(self, name, level, maxhp, str, apt, dex, exp, eweap, ehead, echest, earms, elegs, efeet)

        self.inventory = Container("Inventory")
        self.effminDMG = eweap.minDMG + int(self.str/3)
        self.effmaxDMG = eweap.maxDMG + int(self.str/3)


enemy = [ 
    Enemy("IntBot", 1, 50, 5, 5, 5, 24, weapons[0], 0, 0, 0, 0, 0),
    Enemy("Troll", 1, 60, 6, 5, 5, 33, weapons[0], 0, 0, 0, 0, 0),
    Enemy("Bastard", 5, 100, 10, 8, 8, 65, weapons[1], armor[0], armor[1], armor[2], armor[3], armor[4])
]