from .item import *
import random

class Armor(Item):
    def __init__(self, name, value, defense, slot, quantity, shopChance, req_str, req_dex, add_str=0, add_dex=0, add_hp=0, add_apt=0):
        Item.__init__(self, name, value, quantity)
        
        self.name = str(name)
        self.defense = defense
        self.slot = slot
        self.shopChance = shopChance
        self.req_str = req_str
        self.req_dex = req_dex
        self.add_str = add_str
        self.add_dex = add_dex
        self.add_hp = add_hp
        self.add_apt = add_apt

armor = [
    #       Name, Cost, Def, Slot, Qty, ShopChance (X/1000), req str, req dex, add_str, add_dex, add_hp, add_apt
    Armor("Head Armor", 25, 50, "head", 1, 500, 0, 0),
    Armor("Chestplate", 25, 50, "chest", 1, 500, 0, 0),
    Armor("Gauntlets", 25, 50, "arms", 1, 500, 0, 0),
    Armor("Pantalones", 25, 50, "legs", 1, 500, 0, 0),
    Armor("Boots", 25, 50, "feet", 1, 500, 0, 0),
    Armor("Sexplate", 25, 100, "chest", 1, 200, 10, 0, 300, 3, 3, 3)
]