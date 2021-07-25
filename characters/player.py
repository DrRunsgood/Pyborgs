from .character import *
from items.container import *
from items.weapon import *

class Player(Character):
    def __init__(self, name, level, maxhp, str, apt, dex, exp, gold, eweap, ehead, echest, earms, elegs, efeet):
        Character.__init__(self, name, level, maxhp, str, apt, dex, exp, eweap, ehead, echest, earms, elegs, efeet)

        self.gold = gold

        #Exp needed to level up - this value is updated in levelUp method
        self.lvlNext = 25
        self.statpts = 0
        
        self.inventory = Container("Inventory")  #Generate Inventory Object

        #Initialize initial damage
        self.effminDMG = eweap.minDMG + int(self.str/3)
        self.effmaxDMG = eweap.maxDMG + int(self.str/3)

        #Initialize initial defense
        self.defense = ehead.defense + echest.defense + earms.defense + elegs.defense + efeet.defense

    #Updating inventory and stats based on equipping
    def updateWeap(self, new, old):
        self.inventory.add(old)
        self.inventory.remove(new)
        self.effminDMG = new.minDMG + int(self.str/3)
        self.effmaxDMG = new.maxDMG  + int(self.str/3)

    def updateArmor(self, new, old):
        self.inventory.add(old)
        self.inventory.remove(new)
        self.defense -= old.defense
        self.defense += new.defense

    #Update damage based on str stat changes
    def updateDamage(self):
        self.effminDMG = self.eweap.minDMG + int(self.str/3)
        self.effmaxDMG = self.eweap.maxDMG  + int(self.str/3)

    def updateDefense(self):
        pass

    #If you die   
    def die(self, message="Game Over!"):
        print(message)
        self.hp = 0
        self.dead = True
        input()


    def levelUp(self, reward):
        #self.exp += reward

        while self.exp >= self.lvlNext:
            self.level += 1
            self.statpts += 4
            self.exp = self.exp - self.lvlNext
            self.lvlNext = round(self.lvlNext * 1.5)
            print("You leveled up! You are now level ", self.level)

        print("Exp: ", self.exp)
        print("Exp needed for next level: ", self.lvlNext)
        print("To level: {}%".format(int((self.exp/self.lvlNext)*100)))
        print("You have {} stat points to use".format(self.statpts))

    def updateGold(self, reward):
        pass
