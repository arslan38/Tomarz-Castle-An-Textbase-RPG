from player import Player
from checkInput import *
import os
import time
from LocationClasses import *
import sys
from termcolor import colored
from save_load import *
from items import *
from alter_print import alter_print
from dialog import dialog
from fishing import start_music

sleepCoef = 0.5
sleepGUI = 0.5
def intro():
    os.system('mode con: cols=100 lines=20')#58-17
    os.system("title Tomarz Castle RPG")
    os.system('cls')
    os.system('color 7')
    a,b=80,40
    time.sleep(sleepGUI)
    print('#' * 48)
    print('#      Welcome to this text-based RPG for      #')
    print("#   H.Burak Arslan's YZV-102E Final Project!   #")
    print('#' * 48)
    print("               .: 1. New Game :.                  ")
    print("               .: 2.   Load   :.                  ")
    print("               .: 3.   Help   :.                  ")
    print("               .: 4.   Quit   :.                  ")
    
    flag = False
    while not flag:
        start_type = input(colored('>>> ', 'yellow'))
        flag = check(start_type,[1,4])
    print('')
    
    #new game
    if start_type=='1':
        print('Would you like to play with the music?(1-Yes 2-No)')      
        flag = False
        while not flag:
            w_music = input(colored('>>> ', 'yellow'))
            flag = check(w_music,[1,2])
        print('')
        if w_music=='1':start_music()
        os.system('cls')
        alter_print('Once upon a time in Tomarz Castle... ')
        time.sleep(sleepGUI)
        alter_print('There lives a guard his name is: ')
        char_name = input(colored('>>> ', 'yellow'))
        print('')

        alter_print('And he is a: ')
        alter_print('1.Warrior (Heavy Armor,Axe) (50 HP - x2 DMG - 0 DIPLO)')
        time.sleep(sleepCoef)
        alter_print('2.Runner (Light Armor,Dagger) (35 HP - x1 DMG - 5 DIPLO)')
        time.sleep(sleepCoef)
        alter_print('3.Diplomat (Light Armor,Bow) (25 HP - x1.5 DMG - 10 DIPLO)')
        time.sleep(sleepCoef)
        
        
        flag = False
        while not flag:
            char_type = input(colored('>>> ', 'yellow'))
            flag = check(char_type,[1,3])
        print('')

        #generates character with given input
        if char_type=='1':
            player = Player(name = char_name,max_health=50,health=50,damage_coef=2,diplo=0,char_type='Warrior',
                            w_name = 'Axe',w_damage=[7,12])
        elif char_type=='2':
            player = Player(name = char_name,max_health=35,health=35,damage_coef=1,diplo=5,char_type='Runner',
                            w_name = 'Dagger',w_damage=[7,12])
        elif char_type=='3':
            player = Player(name = char_name,max_health=25,health=25,damage_coef=1.5,diplo=10,char_type='Diplomat',
                            w_name = 'Baton',w_damage=[7,12])

        ########################################################################
        os.system('cls')
        alter_print('YOUR STORY')
        f = open('texts\\your_story.txt','r').readlines()
        for line in f:alter_print(effify(non_f_str=line,player=player))

        input(colored('Press any key to continue...', 'yellow'))

        #creates location tuple to reach all functions and informations off locations from anywhere
        locationTuple = (Castle(),River(),Forest(),Mountain(),RedForest())
        #starts on castle
        dialog('texts\castle\castle_main.txt',player,locationTuple)
    
    
    elif start_type=='2':
        print('Would you like to play with the music?(1-Yes 2-No)')      
        flag = False
        while not flag:
            w_music = input(colored('>>> ', 'yellow'))
            flag = check(w_music,[1,2])
        print('')
        if w_music=='1':start_music()
        data = load() #loads data
        playerInfo = data[0] # 
        inventoryInfo = data[1]# holds items in inventory
        shopInfo = data[2] # holds items in shop
        lastLocation = data[3]
        castleInfo = data[4]
        
        #regenerate player
        player = Player(name = playerInfo['name'],health=playerInfo['health'],damage_coef=playerInfo['damage_coef'],diplo=playerInfo['diplo'],
                            char_type=playerInfo['char_type'],w_name =playerInfo['w_name'],w_damage=playerInfo['w_damage'],money=playerInfo['money']
                            ,special_events = playerInfo['special_event'],done_special_events = playerInfo['done_special_event'],max_health = playerInfo['max_health'] )

        #regenerate location classes
        castleClass = Castle(name=castleInfo['name'],tavern=castleInfo['tavern'],overlord=castleInfo['overlord'])
        forestClass = Forest()
        mountainClass = Mountain()
        riverClass = River()
        red_forestClass = RedForest()
        
        #regenerate inventory
        for item in inventoryInfo.values():
            clas,name,money,point,property,type,sellable = item
            if clas=='Clothing':
                item = Clothing(clas=clas,name=name,money=int(money),point=int(point),
                                        property=property,type=type,sellable=int(sellable))
            if clas=='Special': 
                item= Special(clas=clas,name=name,money=int(money),point=int(point),
                                        property=property,type=type,sellable=int(sellable))
            if clas=='Interactive': item = Interactive(clas=clas,name=name,money=int(money),point=int(point),
                                        property=property,type=type,sellable=int(sellable))
            player.inventory.add_item(item)

        #regenerates shop
        castleClass.del_shop()
        for item in shopInfo.values():
            clas,name,money,point,property,type,sellable = item
            if clas=='Clothing':item = Clothing(clas=clas,name=name,money=int(money),point=int(point),
                                        property=property,type=type,sellable=int(sellable))
            if clas=='Special': item= Special(clas=clas,name=name,money=int(money),point=int(point),
                                        property=property,type=type,sellable=int(sellable))
            if clas=='Interactive': item = Interactive(clas=clas,name=name,money=int(money),point=int(point),
                                        property=property,type=type,sellable=int(sellable))
            castleClass.shop.add_item(item)
        
        #regenerate location tuple
        locationTuple = (castleClass,riverClass,forestClass,mountainClass,red_forestClass)
        
        #starts in last location
        if lastLocation=='Castle':dialog('texts\\castle\\castle_main.txt',player,locationTuple)
        elif lastLocation=='Forest':dialog('texts\\forest\\forest_main.txt',player,locationTuple)
        elif lastLocation=='River':dialog('texts\\river\\river_main.txt',player,locationTuple)
        elif lastLocation=='Mountain':dialog('texts\\mountain\\mountain_main.txt',player,locationTuple)
        
    #help text
    elif start_type=='3':
            os.system('cls')
            f = open('texts\\help.txt','r').readlines()
            for line in f:print(line,end = '  ')
            print('')
            print('#############################################')
            print('')
            input(colored('Press any key to continue...', 'yellow'))
            intro()
    
    elif start_type=='4':
        sys.exit()

intro()