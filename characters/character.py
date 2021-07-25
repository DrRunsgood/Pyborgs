
class Character(object):
    def __init__(self, name, level, maxhp, str, apt, dex, exp, eweap, ehead, echest, earms, elegs, efeet):
        self.level = level
        self.name = name
        self.maxhp = maxhp
        self.str = str
        self.apt = apt
        self.dex = dex
        self.exp = exp
        self.eweap = eweap
        self.ehead = ehead
        self.echest = echest
        self.earms = earms
        self.elegs = elegs
        self.efeet = efeet

        self.hp = maxhp

        self.dead = False

    def attack(self, other):
        pass

    def update(self):
        if self.hp <= 0:
            self.dead = True
            self.hp = 0