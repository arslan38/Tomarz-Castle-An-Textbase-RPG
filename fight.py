from characters import *
import time
import random
from checkInput import *
from termcolor import colored
from alter_print import alter_print
import os
from items import *

def died(lose_money,player,locationTuple,text1):#when you lost a fight.
                    time.sleep(1)
                    alter_print(f'You fainted...') 
                    print(text1)
                    print(' ')
                    if player.money>4:
                        lose_money = random.randint(1,(player.money)//2) # gives random punishment
                        print(f'But they stole {lose_money} GOLD from your pocket. Now you have {player.money-lose_money} GOLD.')
                        player.set_money(-1*lose_money) #lose money
                        print('')
                    flag=False
                    player.health = player.max_health//2 # half health
                    input(colored('Press any key to continue...', 'yellow'))
                    locationTuple[0].go_room(player,locationTuple)


def fight(player,location=None,locationTuple=None,special=None):
    def while_loop(player,enemy_f,text_entry,location=None):
        temp = []
        f = open('data\\enemies.txt','r').readlines() #this file holds all enemies.
        for enemy in f:
            enemySplit = enemy.rstrip().split(',')
            if enemySplit[0]==enemy_f:temp.append(enemySplit) #enemy_f can be Robber,Monster etc. 
            """
            Example of one line in enemy file:

            Robber,Charismatic,5,10,2,2.5-5,30,50,10
            
            type = type of enemy like Robber or Monster etc.
            name = name of enemy like Charismatic or weak etc.
            damage_range_s = health range's start
            damage_range_e = health range's end
            damage_coef = damage coefficent like x1,x2,x1.5 etc.
            damage_str = for print out the damage range
            health_range_s = health range's start
            health_range_e =  health range's end
            req_diplo = reqirement diplomatic point to convince enemy not to fight
            """

        choice = random.choice(temp)
        enemy = Enemy(choice[0],choice[1],choice[2],choice[3],choice[4],choice[5],choice[6],choice[7],choice[8])
        enemy_name = enemy.type
        print('*'*a)
        print(effify(text_entry,player=player,enemy=enemy,enemy_name=enemy_name,location=location)) # entry text
        print('*'*a)
        time.sleep(2)

        flag = True
        while flag:
            os.system('cls')
            round_flag = True
            print(f'You are fighting with {enemy.name} {enemy_name}.')
            print(f'{enemy.name} {enemy_name} has {enemy.health} HP , ({enemy.damage}) DMG,') # fight information
            print(f'You have {player.health} HP')
            print(' ')
            time.sleep(1)
            
            #options for fight
            print(f'''1.Attack {enemy_name}
2.Heal yourself (15HP)
3.Convince enemy not to fight(Req. diplo is {enemy.req_diplo} DIPLO)
4.Open Inventory''')
            
            flag_pick = False
            while not flag_pick:
                move_input = input(colored('>>> ', 'yellow'))
                flag_pick = check(move_input,[1,4])
            print(' ')
            
            #attack option
            if move_input == '1':
                
                f = open('texts\\attack_texts.txt','r').readlines()#picks random text from attack_texts and print out
                attack_texts = [effify(i,player,enemy,enemy_name) for i in f]
                attack_text = random.choice(attack_texts)
                
                min_range,max_range = player.weapon.damage_range
                #%30 MISS chance
                if random.randint(0,100)>20:damage = random.randint(min_range,max_range)*player.damage_coef #randomly picks a integer between min and max range
                else:damage = 0
                enemy.health-=damage
                time.sleep(1)
                print(attack_text)
                if damage!=0:print(f'>You caused {damage} DMG to the {enemy_name}.')
                else:print(f'>MISSED. You caused {damage} DMG to the {enemy_name}.')
                print('')
                time.sleep(1)

            #heal option
            elif move_input == '2':
                player.set_health(15)
                time.sleep(1)
                print(f'You healed yourself. Now you have {player.health}HP')
                time.sleep(1)

            elif move_input == '3':
                if int(player.diplo)>=int(enemy.req_diplo):
                    flag = False
                    f = open('texts\\convince_texts.txt','r').readlines()
                    diplo_texts = [effify(i,player,enemy,enemy_name) for i in f]
                    diplo_text = random.choice(diplo_texts)
                    time.sleep(1)
                    print(diplo_text)
                    input(colored('Press any key to continue...', 'yellow'))
                else:
                    time.sleep(1)
                    print(f'You could not convince him and now it\'s his turn to attack. You have {player.diplo} DIPLO point.')
                    time.sleep(1)

            elif move_input == '4':
                time.sleep(1)
                print(f'Your inventory : ')
                print(player.inventory)
                flag_pick = False
                while not flag_pick:
                    move_input = input(colored('>>> Pick Item to sell(if you want to quit type 0):', 'yellow'))
                    flag_pick = check(move_input,[0,len(player.inventory.get_items())])
                if move_input=='0':
                    round_flag = False
                else:
                    name_list = [item for item in player.inventory.items]
                    item = name_list[int(move_input)-1]
                    if item.clas=='Interactive':
                        item.apply_property(player=player,enemy=enemy)
                        print('')
                        if item.property=='Health':print(f'You healed yourself. You gain {item.point} {item.property}.')
                        elif item.property=='Attack':print(f'You attacked {enemy.name}. You gave {item.point} {item.property}.')
                        player.inventory.remove_items(item)
                        round_flag = False
                        input(colored('Press any key to move on to the next round...', 'yellow'))
                        
                
            if enemy.health<=0:
                print(f'You killed {enemy_name}')  
                print('')
                moneyy = random.randint(player.money//10,player.money//6)
                player.set_money(moneyy)
                secim = olasılık(50)
                if secim:
                    file = open('data\\drop.txt','r').readlines()
                    item_choice = random.choice(file)
                    clas,name,money,point,property,type,sellable = item_choice.split(',')
                    if clas=='Clothing': item = Clothing(clas=clas,name=name,money=int(money),point=int(point),
                                                    property=property,type=type,sellable=int(sellable))
                    if clas=='Special': item= Special(clas=clas,name=name,money=int(money),point=int(point),
                                                    property=property,type=type,sellable=int(sellable))
                    if clas=='Interactive':item= Interactive(clas=clas,name=name,money=int(money),point=int(point),
                                                    property=property)                                   
                    player.inventory.add_item(item)
                    print(f'You dropped {name} item from {enemy_name} and you gain {moneyy} GOLD.')
                else:
                    print(f'You gain {moneyy} GOLD.')
                print('')
                input(colored('Press any key to continue...', 'yellow'))  
                flag=False                
            
            if round_flag and flag:
                min_range,max_range = enemy.damage_range
                if random.randint(0,100)>30:enemy_damage = random.randint(min_range,max_range)*enemy.damage_coef
                else:enemy_damage = 0

                player.set_health(-1*enemy_damage)
                time.sleep(1)
                if enemy_damage!=0:print(f'>{enemy_name} caused {enemy_damage} DMG to you.')
                else:print(f'>MISSED. {enemy_name} caused {enemy_damage} DMG to you.')
                print(' ')
                time.sleep(1)
                input(colored('Press any key to move on to the next round...', 'yellow'))
                 
            
            if player.health<=0:
                return False
             
    a,b = 40,20
    
    if special==None:
        loop = 1
        if location.name=='Forest':enemy_f = 'Bandit'
        elif location.name=='River':enemy_f = 'Robber'
        elif location.name=='Castle':enemy_f = 'Bandit'
        ret = while_loop(player=player,
                        enemy_f=enemy_f,text_entry='When you were going to the {location.name}, a {enemy.name} {enemy_name} blocked your way.',location=location)
        if ret==False:
                lose_money = random.randint(1,(player.money)//2)
                died(locationTuple = locationTuple,text1='When the villagers who found you, they saw that you are a guard, they carried you to the castle.',player = player,lose_money = lose_money)
                

    if special =='mission_tax':
            enemy_f = 'Peasant'
            loop = random.randint(2,4)
            for i in range(loop):
                ret = while_loop(player,enemy_f=enemy_f,text_entry = 'You faced with village peasants, a {enemy.name} {enemy_name} prepared to fight.')
                if ret==False:
                    lose_money = random.randint(1,(player.money)//2)
                    died(locationTuple = locationTuple,text1='The villagers who beat you up threw you out of the village. You rode on your horse to the castle, almost unconscious. They treated you right away and placed you in your room. ',player = player,lose_money = lose_money)
                    return False
            return True

    if special =='fight_red':
            enemy_f = 'Monster'
            loop = random.randint(2,4)
            for i in range(loop):
                ret = while_loop(player,enemy_f=enemy_f,text_entry = 'You faced with monsters, a {enemy.name} {enemy_name} prepared to fight with you.')
                if ret==False:
                    lose_money = random.randint(1,(player.money)//2)
                    died(locationTuple = locationTuple,text1='You rushed to where you entered the red forest, injured. You jumped on your horse, but you fell from your horse halfway and the merchant who found you brought you to the castle at the last moment.',player = player,lose_money = lose_money)
                    return False
            return True


    if special =='random_punks':#in random location events
            enemy_f = 'Punk'
            loop = random.randint(2,4)
            for i in range(loop):
                ret = while_loop(player,enemy_f=enemy_f,text_entry = 'You faced with punks, a {enemy.name} {enemy_name} prepared to fight with you.')
                if ret==False:
                    lose_money = random.randint(1,(player.money)//2)
                    died(locationTuple = locationTuple,text1='The punks beat you up and left you where you are. Your bodyguard friends on patrol found you and carried you home. ',player = player,lose_money = lose_money)
                    return False
            return True
    
    if special =='last_fight':
            enemy_f = 'Monster'
            
            if 'bomb' in player.special_event:loop = random.randint(5,10)#if trap event happens
            else:loop = random.randint(15,20)
            if 'bomb' in player.special_event:
                alter_print('You trapped them with bomb. And killed nearly all of them while they are trying to get their weapons from armory.')
            
            alter_print(f'You are fighting with {loop} enemy. This is the battle of your life ') 
            input(colored('Press any key to move on to the fight...', 'yellow'))   
                
            for i in range(loop):
                ret = while_loop(player,enemy_f=enemy_f,text_entry = 'You faced with angry monsters, a {enemy.name} {enemy_name} prepared to fight with you.')
                if ret==False:
                    os.system('cls')
                    alter_print('You lost the battle of your life. The rebels cut off your head and mailed it to the lord. Hearing this, none of the soldiers agreed to enter the red forest on Remo\'s orders. Over time, the number of rebels increased and they rose up with the villagers and stormed the castle. Remo\'s head suffered the same fate as you and the rebel commander. A head detached from its body... ')
                    input(colored('Press any key to move on to the next round...', 'yellow')) 
                    os.system('cls')
                    input(colored('THE END...', 'red'))
                    import sys
                    sys.exit()

            os.system('cls')
            alter_print('You won the battle of your life. You returned to the castle with the head of the rebel commander. Overlord remo rewarded you with the command. Now you were in charge of the castle you once patrolled and your friends. The girl in the tavern? You married him too. You killed a lot of rebel villagers, but now you\'re a commander and you have a beautiful wife. Here is the quirk of life. ')
            input(colored('Press any key to move on to the next round...', 'yellow')) 
            os.system('cls')
            input(colored('THE END...', 'red'))    
            import sys
            sys.exit()