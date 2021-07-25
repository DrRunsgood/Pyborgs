from .item import *
import random

class Weapon(Item):
    def __init__(self, name, value, damage, quantity, shopChance, req_str, req_dex):
        Item.__init__(self, name, value, quantity)

        self.name = str(name)
        self.req_str = req_str
        self.req_dex = req_dex

        #(self.minDMG, self.maxDMG) = damage
        self.minDMG = damage[0]
        self.maxDMG = damage[1]

        self.shopChance = shopChance

    def damage(self):
        return random.randint(self.minDMG, self.maxDMG)

#could also just pass both minDMG and maxDMG if weapons are damage RANGES ie Maul 25-50
#value here represents cost to purchase

weapons = [
    #      Name, Cost, (MinDMG, MaxDMG), Qty, shopChance (x/1000), req str, req dex, Stat Augment?
    Weapon("Dagger", 5, (2,3), 1, 1000, 0, 0),
    Weapon("Longsword", 25, (7,12), 1, 500, 12, 5),
    Weapon("Maul", 100, (25,50), 1, 100, 25, 10)
]