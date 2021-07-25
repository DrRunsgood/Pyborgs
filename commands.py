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
        
    toequip = input("\nWhat would you like to equip?")

    for name, item in player.inventory:
        if item.name.lower() == str(toequip).lower():
            #Weapon
            if type(item) is Weapon:
                if  player.str >= item.req_str and player.dex >= item.req_dex:
                    currweap = player.eweap
                    toequip = item
                    player.eweap = toequip
                    player.updateWeap(player.eweap, currweap)
                    print("\nYou have equipped {0}".format(item.name))
                    print("Your effective dmg is: {0} - {1}".format(player.effminDMG,player.effmaxDMG))
                elif player.str < item.req_str:
                    print("\nYou are not strong enough to wield the " + item.name + "!\n")
                    break
                elif player.dex < item.req_dex:
                    print("\nYou dexterity isn't enough to wield the " + item.name + "!\n")
                    break

            #Armor
            if type(item) is Armor:
                if item.name.lower() == str(toequip).lower() and player.str >= item.req_str and player.dex >= item.req_dex: #Need to choose which armor slot
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
                    print("\nYou have equipped {0}".format(item.name))
                    print("Your effective defense is: {0}".format(player.defense))
                elif player.str < item.req_str:
                    print("\nYou are not strong enough to wield the " + item.name + "!\n")
                    break
                elif player.dex < item.req_dex:
                    print("\nYou dexterity isn't enough to wield the " + item.name + "!\n")
                    break
        else:
            print("not found!")

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

        atk_str = "{0} attacked {1} for {2} damage!".format(p1.name, p2.name, p1.dmg)
        print(atk_str.rjust(100))
        p2.hp = p2.hp - p1.dmg
        hp_str = "{0} hp remaining: {1}".format(p2.name, p2.hp)
        print(hp_str.rjust(100))

        if p2.hp <= 0:
                        #If player wins
            if p1 == player:
                #calc gold gain
                lowgold = int(p2.gold*0.5)
                highgold = int(p2.gold*1.5)
                gold_gained = randint(lowgold, highgold)
                p1.gold += gold_gained
                #calc exp gain
                lowexp = int(p2.exp*0.8)
                highexp = int(p2.exp*1.4)
                exp_gained = randint(lowexp, highexp)
                p1.exp += exp_gained
                print("{0} has won the battle!".format(p1.name))
                print("{0} has gained {1} experience points!".format(p1.name, exp_gained))
                print("{0} has earned {1} gold!".format(p1.name, gold_gained))
                print("\n")
            #If player loses
            elif p2 == player:
                #calc gold gain
                lowgold = int(p1.gold*0.1)
                highgold = int(p1.gold*0.5)
                gold_gained = randint(lowgold, highgold)
                p2.gold += gold_gained
                #calc exp gain
                lowexp = int(p1.exp*0.2)
                highexp = int(p1.exp*0.4)
                exp_gained = randint(lowexp, highexp)
                p2.exp += exp_gained
                print("{0} has won the battle!".format(p1.name))
                print("{0} has gained {1} experience points!".format(p2.name, exp_gained))
                print("{0} has earned {1} gold!".format(p2.name, gold_gained))
                print("\n")
            break

        time.sleep(1.5)
        print("{0} attacked {1} for {2} damage!".format(p2.name, p1.name, p2.dmg))
        p1.hp = p1.hp - p2.dmg
        print("{0} hp remaining: {1}".format(p1.name, p1.hp))

        if p1.hp <= 0:
            print("{0} has won the battle!".format(p2.name))
            print("{0} has gained {1} experience points!".format(p2.name, p1.exp))
            print("{0} has earned {1} gold!".format(p2.name, p1.gold))
            print("\n")
            #If player loses
            if p1 == player:
                lowgold = int(p2.gold*0.1)
                highgold = int(p2.gold*0.5)
                gold_gained = randint(lowgold, highgold)
                p1.gold += gold_gained
                #calc exp gain
                lowexp = int(p2.exp*0.2)
                highexp = int(p2.exp*0.4)
                exp_gained = randint(lowexp, highexp)
                p1.exp += exp_gained
                print("{0} has won the battle!".format(p2.name))
                print("{0} has gained {1} experience points!".format(p1.name, exp_gained))
                print("{0} has earned {1} gold!".format(p1.name, gold_gained))
                print("\n")
            #If player wins
            elif p2 == player:
                lowgold = int(p1.gold*0.5)
                highgold = int(p1.gold*1.5)
                gold_gained = randint(lowgold, highgold)
                p2.gold += gold_gained
                #calc exp gain
                lowexp = int(p1.exp*0.8)
                highexp = int(p1.exp*1.4)
                exp_gained = randint(lowexp, highexp)
                p2.exp += exp_gained
                print("{0} has won the battle!".format(p2.name))
                print("{0} has gained {1} experience points!".format(p2.name, exp_gained))
                print("{0} has earned {1} gold!".format(p2.name, gold_gained))
                print("\n")
            break

        time.sleep(1.5)
        
    p1.hp = p1.maxhp
    p2.hp = p2.maxhp

    player.levelUp(exp_gained) #Check for level up

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

#View player info
def me(player, args):
    print("Player Stats:")
    print("Level: ", player.level)
    print("Gold: ", player.gold)
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
        print(item.name + ", " + str(item.value))

    purchase = input("Type the name of the item you'd like to buy (or 'exit' to leave shop): ")

    for item in shopitems:
        if purchase == 'exit':
            break
        if purchase == item.name:
            if player.gold >= item.value:
                player.gold -= item.value
                player.inventory.add(item)
                shopitems.remove(item)
                print(item.name + " has been purchased and added to your inventory!")
            elif player.gold < item.value:
                print("You don't have enough gold you broke bitch!")
                break

#Exit command
def bye(player, args):
    print("Seeya")
    exit()