# Main game file
from characters.player import *
from characters.enemy import *
from commands import *
from items.item import *
from items.weapon import *
from items.armor import *
import threading

#name, level, maxhp, str, apt, dex, exp, gold, eweap, ehead, echest, earms, elegs, efeet

player = Player("Default", 1, 50, 10, 6, 5, 0, 10, weapons[0], armor[0], armor[1], armor[2], armor[3], armor[4])

#player.inventory.add(weapons[1])
player.inventory.add(weapons[2])
player.inventory.add(armor[5])

global counter_thread

# this is all just for menu communication
def help(player, args):
    for command in commands:
        print(command)

commands = {
    'help': help,
    'inv': inv,
    'exit': bye,
    'atk': atk,
    'weap': weap,
    'equip': equip,
    'stats': updateStats,
    'me': me,
    'shop': shop
}

def isValidCMD(cmd):
    if cmd in commands:
        return True
    return False

def runCMD(cmd, args, player):
    commands[cmd](player, args)


def main():

    counter_thread = threading.Thread(target = counter)
    counter_thread.daemon = True
    counter_thread.start()

    player.name = input("What is your name?")
    print("Hello " + str(player.name))
    print("Your equipped weapon is: " + str(player.eweap.name))

    while(not player.dead):

        print("Choose a command, " + player.name)
        line = input(">> ")
        data = line.split()
        data.append("EOI")

        if data[0] == 'atk':
            for index, enemies in enumerate(enemy):
                print(enemy[index].name)
                enemyname = str(enemy[index].name)
                if data[1] == enemyname.lower():
                    data[1] = enemy[index]


        if isValidCMD(data[0]):
            runCMD(data[0], data[1], player)


main()