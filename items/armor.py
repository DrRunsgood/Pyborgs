from .item import *
import random

class Armor(Item):
    def __init__(self, name, value, defense, slot, quantity, shopChance, req_str, req_dex):
        Item.__init__(self, name, value, quantity)
        
        self.name = str(name)
        self.req_str = req_str
        self.req_dex = req_dex
        self.defense = defense
        self.slot = slot
        self.shopChance = shopChance

armor = [
    #       Name, Cost, Def, Slot, Qty, ShopChance (X/1000), req str, req dex, stat augment?
    Armor("Head Armor", 25, 50, "head", 1, 500, 0, 0),
    Armor("Chestplate", 25, 50, "chest", 1, 500, 0, 0),
    Armor("Gauntlets", 25, 50, "arms", 1, 500, 0, 0),
    Armor("Pantalones", 25, 50, "legs", 1, 500, 0, 0),
    Armor("Boots", 25, 50, "feet", 1, 500, 0, 0),
    Armor("Sexplate", 25, 100, "chest", 1, 200, 16, 0)
]