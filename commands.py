from items.weapon import *
from items.armor import *
from random import randint
import time

#View Inventory
def inv(player, args):
    for name, item in player.inventory:
        print("{0} x{1}".format(item.name, item.quantity))
        if type(item) is Weapon:
            print(item.minDMG, item.maxDMG)
    print("Your total current defense is: {0}".format(player.defense))

# Equipping
def equip(player, args):
    
    for name, item in player.inventory:
        if type(item) is Weapon:
            print("{0} x{1}, dmg:{2} - {3}".format(item.name, item.quantity, item.minDMG, item.maxDMG))
        if type(item) is Armor:
            print("{0}, defense: {1}".format(item.name, item.defense))
    toequip = input("What would you like to equip?")

    #Weapon
    for name, item in list(player.inventory):
        if item.name.lower() == str(toequip).lower() and type(item) is Weapon:
            currweap = player.eweap
            toequip = item
            player.eweap = toequip
            player.updateWeap(player.eweap, currweap)
            print("You have equipped {0}".format(item.name))
            print("Your effective dmg is: {0} - {1}".format(player.effminDMG,player.effmaxDMG))

    #Armor
    for name, item in list(player.inventory):
        if item.name.lower() == str(toequip).lower() and type(item) is Armor: #Need to choose which armor slot
            toequip = item
            if toequip.slot == "head":
                currhead = player.ehead
                player.ehead = toequip
                player.updateArmor(player.ehead, currhead)
            elif toequip.slot == "chest":
                currchest = player.echest
                player.echest = toequip
                player.updateArmor(player.echest, currchest)
            elif toequip.slot == "arms":
                currarms = player.earms
                player.echest = toequip
                player.updateArmor(player.earms, currarms)
            elif toequip.slot == "legs":
                currlegs = player.elegs
                player.echest = toequip
                player.updateArmor(player.elegs, currlegs)
            elif toequip.slot == "feet":
                currfeet = player.efeet
                player.echest = toequip
                player.updateArmor(player.efeet, currfeet)
            print("You have equipped {0}".format(item.name))
            print("Your effective defense is: {0}".format(player.defense))




def weap(player, args):
    for name, item in player.inventory:
        if type(item) is Weapon:
            print("Your weapon(s) are {0}".format(item.name))
    print("Currently equipped weapon: {0}".format(player.eweap.name))
    print("Your equipped weapon does {0} - {1} damage".format(player.eweap.minDMG, player.eweap.maxDMG))


## ATTACK ##
def atk(player, args):

    #Test for higher aptitude level - they go first
    if player.apt > args.apt:
        p1 = player
        p2 = args
    else:
        p1 = args
        p2 = player

        p1.hp = p1.maxhp
        p2.hp = p2.maxhp

    print("\n\n\n\n\n\n\n\n\n\n\n")

    while p1.hp > 0 and p2.hp > 0:

        p1.dmg = randint(int(p1.effminDMG), int(p1.effmaxDMG))
        p2.dmg = randint(p2.effminDMG, p2.effmaxDMG)

        print("{0} attacked {1} for {2} damage!".format(p1.name, p2.name, p1.dmg))
        p2.hp = p2.hp - p1.dmg
        print("{0} hp remaining: {1}".format(p2.name, p2.hp))

        if p2.hp <= 0:
            print("{0} has won the battle!".format(p1.name))
            print("{0} has gained {1} experience points!".format(p1.name, p2.exp))
            break

        time.sleep(1.5)
        print("{0} attacked {1} for {2} damage!".format(p2.name, p1.name, p2.dmg))
        p1.hp = p1.hp - p2.dmg
        print("{0} hp remaining: {1}".format(p1.name, p1.hp))

        if p1.hp <= 0:
            print("{0} has won the battle!".format(p2.name))
            print("{0} has gained {1} experience points!".format(p2.name, p1.exp))
            break

        time.sleep(1.5)
        
    p1.hp = p1.maxhp
    p2.hp = p2.maxhp

    player.levelUp(args.exp) #Check for level up

### UPDATE PLAYER STATS ###
def updateStats(player, args):
    while player.statpts > 0:
        print("You have {} stat points to spend".format(player.statpts))
        print("Type 'hp', 'str', 'dex' or 'apt' to level up the stat or type exit to go back.")
        stat = input(">> ")
        if stat == 'hp':
            player.maxhp += 10
            player.hp = player.maxhp
            player.statpts -= 1
            print("Your Max HP is now: ", player.maxhp)
        elif stat == 'str':
            player.str += 1
            player.statpts -= 1
            player.updateDamage()
            print("Your Strength is now: ", player.str)
        elif stat == 'dex':
            player.dex += 1
            player.statpts -= 1
            print("Your Dexterity is now: ", player.dex)
        elif stat == 'apt':
            player.apt += 1
            player.statpts -= 1
            print("Your Aptitude is now: ", player.apt)
        elif stat == 'exit':
            break
    if player.statpts == 0:
        print("You have no stat points to spend.")

def me(player, args):
    print("Player Stats:")
    print("Level: ", player.level)
    print("HP: ", player.maxhp)
    print("Strength: ", player.str)
    print("Effective Dmg: ",player.effminDMG, player.effmaxDMG)

### SHOP ###
#Shop update counter
def counter():

    shop_timer = 1

    while shop_timer < 21:
        shop_timer = shop_timer - 1
        time.sleep(1)

        if shop_timer == 0:
            updateShop()
            shop_timer = 20

#Called to update the shop
def updateShop():
    global shopitems
    shopitems = []

    for item in weapons:
        if randint(1,1000) <= item.shopChance:
            shopitems.append(item)
        
    for item in armor:
        if randint(1,1000) <= item.shopChance:
            shopitems.append(item)

#Want to purchase something from the shop?
def shop(player, args):

    for item in shopitems:
        print(item.name)

    purchase = input("Type the name of the item you'd like to buy: ")
    for item in shopitems:
        if purchase == item.name:
            player.inventory.add(item)
            shopitems.remove(item)

            print("Remaining shop items: ")
            for item in shopitems:
                print(item.name)

#Exit command
def bye(player, args):
    print("Seeya")
    exit()