from checkInput import *
from termcolor import colored
from save_load import *
from alter_print import alter_print
from items import *
import os 
from fight import fight
import random
import time
from fishing import fishing

def dialog(filepath,player,locationTuple):
    
    f = open(filepath,'r').readlines()
    
    flag = True
    active_text = f[0]#represents a line in file. We can think each line as a root if has options else it is a leaf. 
    
    while flag:
        os.system('cls')
        splitted_text = active_text.rstrip().split('-')
        
        #print(splitted_text)
        text_id,is_alter_print,is_root,req_event,is_special,action,aim_id,text =  splitted_text[:8]
        
        """
        Each line has information about these things for example:
            
            8-1-1-Overlord Mission,1-0-0-9->What did you do with the task I gave you?
            
            text_id = line number
            is_alter_print = normal print or flow print
            is_root = has options or not
            req_event = if there is a requirement event it contains it like war,0 or cloths,1. If there is not holds 0.
            is_special = if there is a special event to add player's special event list, it contains it like forest_tax,0 or Overlord Mission,99. If there is not holds 0.
            action = goes actions like fight,give money,mission done or mini games.
            aim_id = it holds when we are done with this line we will pass 
            text = text can be print or holds special informations for actions
        """
        
        try:aim_id,aimm = aim_id.split(',') # if there is 2 situations like win or lose text holds two aim and according to the result goes to one of them.
        except:pass
        try:req_event,req_id = req_event.split(',')#req_event is key of dictionary req_id is value of this key
        except:req_id=-1
        try:is_special,special_id = is_special.split(',')#is_special is key of dictionary special_id is value of this key
        except:special_id=-1
        
        if is_special!='0':
            player.set_special_event(is_special,int(special_id)) # appends special_event to player's dict

        try: options = [[i.split('&')[0],i.split('&')[1]] for i in splitted_text[8:]]
        except: pass
        
        if action!='0': # if there is a action given in text
            #actions comes from texts
            if action=='go_text': # goes another text file and prints random line 
                ff = open(text,'r').readlines()
                text = random.choice(ff)
                alter_print(text)
                input(colored('Press any key to continue...', 'yellow'))
                active_text = f[int(aim_id)]
            
            if action=='go_dialog':# goes another dialog file recursively
                dialog(text,player,locationTuple)
                active_text = f[int(aim_id)]
                        
            if action=='go_location':# goes another location dialog file recursively(go_dialog+random events)
                alter_print('You set out...')
                time.sleep(1)

                #location that player in
                location = locationTuple[0]
                if text == 'texts\\castle\\castle_main.txt':location = locationTuple[0]
                elif text == 'texts\\river\\river_main.txt':location = locationTuple[1]
                elif text == '.texts\\mountain\\mountain_main.txt':location = locationTuple[3]
                elif text == 'texts\\forest\\forest_main.txt':location = locationTuple[2]
                
                secim = olasılık(60)#random fight
                if secim:fight(player,location,locationTuple)#enemies changes with location
                
                random_ev = olasılık(65)#random location event
                if random_ev:
                    mission_list = [filenames for (dirpath, dirnames, filenames) in os.walk(f'texts\\random_events')][0]
                    mission_dir = random.choice(mission_list)
                    dialog(f'texts\\random_events\\{mission_dir}',player,locationTuple)#random location event file

                save(player,locationTuple,location)#save

                dialog(text,player,locationTuple)#travel
                active_text = f[int(aim_id)]
            
            if action=='health':
                time.sleep(2)
                print(f'{text}\n')
                player.health = player.max_health#give health when player sleeps
                input(colored('Press any key to continue...', 'yellow'))
                active_text = f[int(aim_id)]

            if action=='special_loc':#unique sub-locations in each location
                if text=='fishing':fishing(player,locationTuple)
                elif text=='hunting':active_text = f[int(aim_id)]
                elif text=='shephard':active_text = f[int(aim_id)]
                elif text=='tavern':dialog('texts\\castle\\castle_tavern.txt',player,locationTuple)
                elif text=='gambling':gambling(player,locationTuple)
                else:print('pup')
                active_text = f[int(aim_id)]

            if action == 'tavern_wine':#drink wine in tavern
                if player.money>1:
                    alter_print('You drinked hot wine and get warm.')
                    player.money-=1
                    print('')
                    input(colored('Press any key to continue...', 'yellow'))
                else:
                    print(f'The inkeeper said he did not pay on credit. You have no money.')
                    print('')
                    input(colored('Press any key to continue...', 'yellow'))
                active_text = f[int(aim_id)]

            if action=='check_inventory':
                name_list = [item.name for item in player.inventory.items]#names of items
                item_name,value = text.split(',')#given item's name and required  value (like if there are 3 Fish in player's inventory mission done)
                if sum(1 for i in name_list if i == item_name)>=int(value):
                    active_text = f[int(aim_id)]#done
                    check_val = int(value)
                    inven = player.inventory.get_items().copy()
                    for item in inven:
                        if item.name==item_name and check_val!=0:
                            check_val-=1
                            player.inventory.remove_items(item)


                else:active_text = f[int(aimm)]#havent done yet
                """
                Example text line: 6-1-1-0-0-check_inventory-9,8-Fish,5
                    ->check_inventory is action and Fish,5 is text. That mean check if there are 5 fish in the inventory, go to line 9, if not, go to 8. 
                """

            if action=='buy_shop':
                
                #location that player in
                if text=='forest':tupleLoc = locationTuple[2]
                elif text=='river':tupleLoc = locationTuple[1]
                elif text=='castle':tupleLoc = locationTuple[0]
                elif text=='mountain':tupleLoc = locationTuple[3]

                if len(tupleLoc.shop.items)>0:
                    print('ITEM LIST')
                    print(tupleLoc.shop)
                
                else:#if there is no item left
                    print('')
                    print('There is no item left. You bought all of them.')
                    input(colored('Press any key to continue...', 'yellow'))
                    active_text = f[int(aim_id)]


                #Input block code
                flag = False
                while not flag:
                    item_choice = input(colored('>>> Pick Item to buy(if you want to quit type 0):', 'yellow'))
                    flag = check(item_choice,[0,len(tupleLoc.shop.items)])
                print('')

                if item_choice=='0':#exit
                    active_text = f[int(aim_id)]
                
                else:
                    name_list = [item for item in tupleLoc.shop.items]
                    bought_item = name_list[int(item_choice)-1]#detects choosen item
                    
                    if player.money>= bought_item.money :#check money
                        if bought_item.name=='Talking Parrot':player.set_special_event('Main Mission',1)
                        tupleLoc.shop.remove_items(bought_item)#removed from inventory of shop
                        player.set_money(-1*bought_item.money)
                        player.inventory.add_item(bought_item)#add to inventory of player
                        
                        if bought_item.clas!='Special' and bought_item.clas!='Interactive':bought_item.apply_property(player)#Special and Interactive dont have permanent properties
                        #print('-'*10)
                        print(f'You bought {bought_item.name}. Added your inventory. Now you have {player.money} GOLD.')
                        time.sleep(1)
                        print(f'Your inventory : ')
                        print(player.inventory)
                        #print('')
                        input(colored('Press any key to continue...', 'yellow'))
                        active_text = f[int(aim_id)]#aim line
                    else:
                        print(f'You don\'t have enough money. You have {player.money} GOLD.')
                        input(colored('Press any key to continue...', 'yellow'))
                        active_text = f[int(aim_id)]#aim line

            if action=='sell_shop':
                if text=='forest':tupleLoc = locationTuple[2]
                elif text=='river':tupleLoc = locationTuple[1]
                elif text=='castle':tupleLoc = locationTuple[0]
                elif text=='mountain':tupleLoc = locationTuple[3]
                
                print(f'Your inventory : ')
                print(player.inventory) #prints inventory easily
                flag = False#these 5 line is block code for input
                while not flag:
                    item_choice = input(colored('>>> Pick Item to sell(if you want to quit type 0):', 'yellow'))
                    flag = check(item_choice,[0,len(player.inventory.get_items())])#input range
                print('')

                if item_choice=='0':#exit
                    active_text = f[int(aim_id)]#go aim line in text
                
                else:
                    name_list = [item for item in player.inventory.items]
                    selled_item = name_list[int(item_choice)-1]#detects choosen item
                    
                    if selled_item.sellable==1:
                        player.inventory.remove_items(selled_item)#removed from inventory of player
                        tupleLoc.shop.add_item(selled_item)#add to nventory of shop
                        
                        try:selled_item.delete_property(player)#if item has a property like +25 HP or +1 Diplo
                        except:pass
                        
                        gain_money = selled_item.money
                        player.set_money(gain_money)
                        #print('-'*10)
                        print(f'You selled {selled_item.name}. You gain {gain_money} GOLD. Now you have {player.money} GOLD.')
                        time.sleep(1)
                        print(f'Your inventory : ')
                        print(player.inventory)
                        #print('')
                        input(colored('Press any key to continue...', 'yellow'))
                        active_text = f[int(aim_id)]#aim line in text
                    
                    else:
                        print(f'You cannot sell {selled_item.name} item.')
                        input(colored('Press any key to continue...', 'yellow'))
                        active_text = f[int(aim_id)]#aim line in text

            if action=='overlord_mission':# starts a random overlord mission from overlord_missions file.
                alter_print('Let me think.')
                overlord_mission(player,locationTuple)
                active_text = f[int(aim_id)]
            
            if action=='collect_taxes':#starts collect_taxes mission and a random event that in collect_taxes file happens
                alter_print('Of course, sir.I will help you.')
                collect_taxes(text,player,locationTuple)#collect taxes function is down below.
                if aim_id == 'quit':
                    print('')
                    break
                active_text = f[int(aim_id)]
            
            if action=='fight':#starts a fight with given text input as a special input.(Check special cases in fight.These special cases creates different enemies
                #and results.)
                print('You are fighting.')
                bool = fight(player,locationTuple=locationTuple,special=text)#depending on the result goes to the target text  
                if bool:active_text = f[int(aim_id)]#win
                else:active_text = f[int(aimm)]#lose
            
            if action=='mission_del':#deletes mission when player fails
                deleted_mission,main_mission = text.split(',')
                player.del_special_event(deleted_mission)
                player.set_special_event(main_mission,99)
                active_text = f[int(aim_id)]

            if action=='mission_done':#marks mission as done
                done_mission,main_mission = text.split(',')
                player.del_special_event(done_mission)
                player.set_special_event(main_mission,1)
                active_text = f[int(aim_id)]
            
            if action=='overlord_done':#marks overlord mission as done when you say ı have done mission to overlord.
                rangeE = random.randint(40,55)
                player.set_money(rangeE)
                player.del_special_event("Overlord Mission")
                print(f'{rangeE} gold is your share. Nice job {player.name}. ')
                input(colored('Press any key to continue...', 'yellow'))
                active_text = f[int(aim_id)]
            
            if action=='main_del':
                player.del_special_event(text)
                active_text = f[int(aim_id)]
            
            if action=='alcohol_loot':#start alcohol loot event
                for i in range(random.randint(3,6)):
                    Item = Interactive(clas='Interactive',name = 'A Bottle of Flammable Alcohol',money=50,point=50,property='Attack')
                    player.inventory.add_item(Item)
                active_text = f[int(aim_id)]
                
            if action=='surprise_chest':#start surprise chest game
                bool = surprise_chest(player,locationTuple)
                if bool:active_text = f[int(aim_id)]
                else:active_text = f[int(aimm)]
            
            if action=='money_add':#adds money to players inventory
                moneyy = int(effify(text,player=player,enemy=None,enemy_name=None))
                player.set_money(moneyy)
                print(f'You gain {moneyy} GOLD.')
                input(colored('Press any key to continue...', 'yellow'))
                active_text = f[int(aim_id)]
            
            if action=='money_del':#deletes money to players inventory
                moneyy = int(effify(text,player=player,enemy=None,enemy_name=None))
                player.set_money(-1*moneyy)
                print(f'You lost {moneyy} GOLD.')
                input(colored('Press any key to continue...', 'yellow'))
                active_text = f[int(aim_id)]
            
            if action=='end':#end of the game
                os.system('cls')
                input(colored('THE END...', 'red'))
                import sys
                sys.exit()
        else:
            special_events = player.get_special_events()
            flagg=False
            if req_event in special_events: # if given requirement event in text is in player's special events list and has req_id value.
                if special_events[req_event]==int(req_id):
                    flagg=True

                
            if req_event=='0' or flagg:#if there is no requirement event
                
                if int(is_alter_print)==1:alter_print(effify(text,player=player,enemy=None,enemy_name=None))#for manupilate f-strings(you can checkInput.py to see effify function)
                else:print(effify(text,player=player,enemy=None,enemy_name=None))

                if aim_id == 'quit':#close file any get back previous file or function.
                    print('')
                    input(colored('Press any key to continue...', 'yellow'))
                    break
                
                if int(is_root)==1:#if this line is a root print options and detect which option player choosen.
                    for ido,option in enumerate(options):
                        print(f'{ido+1}.{option[0]}')
                    flag_input = False
                    while not flag_input:
                        decision_id = input(colored('>>> ', 'yellow'))
                        flag_input = check(decision_id,[1,len(options)])
                    print('')
                    decision = options[int(decision_id)-1][1]#each option has aim information with itself.(You can check texts.)
                    active_text = f[int(decision)]
                else:#if this line is a leaj just print text and go aim line.
                    active_text = f[int(aim_id)]
                    print('')
                    input(colored('Press any key to continue...', 'yellow'))
                
            else:
                active_text = f[int(aim_id)]

#This function picks random event in Overlord Missions.
def overlord_mission(player,locationTuple):
    mission_list = [filenames for (dirpath, dirnames, filenames) in os.walk('texts\\overlord-missions\\missions')][0]

    while 1:
        mission_dir = random.choice(mission_list)
        if mission_dir in player.done_special_event:flag_dia = False #if player done any mission
        else:
            flag_dia = True
            break
    if flag_dia:
        dialog(f'texts\\overlord-missions\\missions\\{mission_dir}',player,locationTuple)
    else:
        print(f'No I don\'t have any mission for you {player.name}')
        input(colored('Press any key to continue...', 'yellow'))
        player.del_special_event('Overlord Mission')
    
#This function picks random event in tax mission.
def collect_taxes(text,player,locationTuple):
    os.system('cls')
    alter_print('Village Elder collecting taxes...')
    time.sleep(2)
    mission_list = [filenames for (dirpath, dirnames, filenames) in os.walk(f'texts\\overlord-missions\\{text}')][0]

    mission_dir = random.choice(mission_list)
    dialog(f'texts\\overlord-missions\\{text}\\{mission_dir}',player,locationTuple)
    

#There is a mini-game that expects the player to correctly guess a random number between 1 and 5. 
def surprise_chest(player,locationTuple):
    print('You have 3 attempts. Each time the box generates a random number between 1 and 5. If you know in any of them the chest will open. ')
    input(colored('Press any key to continue...', 'yellow'))
    attempts = 3
    flag = False
    number = random.randint(1,5)
    while attempts>0:
        os.system('cls')
        print('Let\'s Try')
        print('')
        flag_input = False
        while not flag_input:
                    Input = int(input(colored('Give Number>> ', 'yellow')))
                    flag_input = check(Input,[1,5])

        if number==Input:
            flag = True 
            print('Bravo!')
            time.sleep(1)
            for i in range(random.randint(3,6)):
                    Item = Interactive(clas='Interactive',name = 'Flower Essence Mix',money=50,point=35,property='Health')
                    player.inventory.add_item(Item)
            break
        else:
            attempts-=1
            print('Keep Trying...')
            print('Remaining Attempts: ',attempts)
            input(colored('Press any key to continue...', 'yellow'))
    return flag
        
def gambling(player,locationTuple):
    if player.money>2:
            
        while True:
            os.system('cls')
            alter_print('What type of game do you want to play?')#options
            print('''1.One shot One number(Too Risky)  
2.One shot Multiple range(Risky)
3.Duel(Risky too)
4.Turn Back''')

            flag = False
            while not flag:
                direction = input(colored('>>> ', 'yellow'))
                flag = check(direction,[1,4])
            print('')
            
            if direction=='1':
                os.system('cls')
                dice = random.randint(1,6)#afatsum's roll
                #describtion of this code is just line down below
                alter_print('I will roll a dice. If you can throw the same, I\'ll give you 3 times your stake, if you can\'t, I\'ll take it all .\n')#describtion
                print('How much money are you putting out? ') #options
                print('''1.All in(Too Risky)
2.Half of my money(Risky)
3.1/3 of my money(Risky too)''')
                
                flag = False
                while not flag:
                    bet = input(colored('>>> ', 'yellow'))
                    flag = check(bet,[1,3])
                print('')
                
                alter_print(f'Afatsum rolled the dice and {dice} came. You should roll {dice} ')
                input(colored('Press any key to roll dice...', 'yellow'))
                alter_print(f'You rolled the dice.... ')
                
                if bet=='1':money = player.money#money that put in
                elif bet=='2':money = player.money//2
                elif bet=='3':money = player.money//3

                player_dice = random.randint(1,6)#players's roll
                if player_dice==dice:
                    alter_print(f'{player_dice} came out. You won 3 times the money you put in so {money*3} GOLD.')
                    player.set_money(money*3)
                    input(colored('Press any key to continue...', 'yellow'))
                    
                else:
                    alter_print(f'{player_dice} came out. You lost {money} GOLD.')
                    player.set_money(-1*money)
                    input(colored('Press any key to continue...', 'yellow'))
            
            elif direction=='2':
                os.system('cls')
                #describtion of this code is just line down below
                alter_print('You will roll a dice, if it gets bigger than 3, you double your money. If it gets smaller, I take your money. \n')
                print('How much money are you putting out? ')
                print('''1.All in(Too Risky) 
2.Half of my money(Risky)
3.1/3 of my money(Risky too)''')
                
                flag = False
                while not flag:
                    bet = input(colored('>>> ', 'yellow'))
                    flag = check(bet,[1,3])
                print('')
                
                alter_print(f'>Are you ready {player.name}?\n')
                input(colored('Press any key to roll dice...', 'yellow'))
                alter_print(f'You rolled the dice.... ')
                
                if bet=='1':money = player.money
                elif bet=='2':money = player.money//2
                elif bet=='3':money = player.money//3

                player_dice = random.randint(1,6)
                if player_dice>3:
                    alter_print(f'{player_dice} came out. You doubled your money so won {money} GOLD.')
                    player.set_money(money)
                    input(colored('Press any key to continue...', 'yellow'))
                else:
                    alter_print(f'{player_dice} came out. You lost {money} GOLD.')
                    player.set_money(-1*money)
                    input(colored('Press any key to continue...', 'yellow'))

            elif direction=='3':
                os.system('cls')
                #describtion of this code is just line down below
                alter_print('I will roll a dice and then you will roll a dice. The big scorer will get 1 point. Whoever gets 3 points gets golds. \n')
                print('How much money are you putting out? ')
                print('''1.All in(Too Risky) 
2.Half of my money(Risky)
3.1/3 of my money(Risky too)''')
                
                flag = False
                while not flag:
                    bet = input(colored('>>> ', 'yellow'))
                    flag = check(bet,[1,3])
                print('')
                                
                if bet=='1':money = player.money
                elif bet=='2':money = player.money//2
                elif bet=='3':money = player.money//3

                afatsum_score,player_score = 0,0
                is_won = False
                while not is_won:
                    os.system('cls')
                    afatsum_dice = random.randint(1,6)
                    alter_print(f'Afatsum rolled the dice and {afatsum_dice} came. You should roll bigger than {afatsum_dice} ')
                    alter_print(f'>Are you ready {player.name}?\n')
                    input(colored('Press any key to roll dice...', 'yellow'))
                    player_dice = random.randint(1,6)
                    alter_print(f'You rolled the dice.... And {player_dice} came out. ')
                    
                    if afatsum_dice>player_dice:
                        afatsum_score+=1
                        print(f'Afatsum got point. You have {player_score} points and Afatsum have {afatsum_score} points.')
                    elif afatsum_dice<player_dice:
                        player_score+=1
                        print(f'You got point. You have {player_score} points and Afatsum have {afatsum_score} points.')
                    else:print('Draw.Roll again.')
                    if player_score==3:
                        print(f'You won. And you get {money} GOLD.')
                        player.set_money(money)
                        input(colored('Press any key to continue...', 'yellow'))
                        break
                    elif afatsum_score==3:
                        print(f'You lost. And you lost {money} GOLD.')
                        player.set_money(-1*money)
                        input(colored('Press any key to continue...', 'yellow'))
                        break
                    input(colored('Press any key to continue to next round...', 'yellow'))

            elif direction=='4':   
                os.system('cls')
                alter_print('Good Bye.I hope you come again ')
                input(colored('Press any key to continue...', 'yellow'))
                break

    else:
        alter_print('If you don\'t have money, get off the gambling table. I will be waiting for you. ')