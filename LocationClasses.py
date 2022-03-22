import random
from checkInput import check
import time 
from fight import fight
from items import *
from player import *
from dialog import dialog

"""
    Each location class has functions to reach any sub-location in this location. Program can reach in anywhere to locationTuple.
    They also have shop information. Reads this locations shop txt and creates items then append them in their inventory object.
"""

class Castle:
    def __init__(self,name = 'Castle',tavern = ['Nakres','Afatsum'],overlord = ['Mission']):
        self.name =name
        self.tavern = tavern
        self.overlord = overlord
        
        file = open('data\\shop.txt','r').readlines()#shop txt
        self.shop = Inventory()
        for line in file:#creates items in file
            clas,name,money,point,property,type,sellable = line.split(',')
            if clas=='Clothing': item = Clothing(clas=clas,name=name,money=int(money),point=int(point),
                                        property=property,type=type,sellable=int(sellable))
            if clas=='Special': item= Special(clas=clas,name=name,money=int(money),point=int(point),
                                        property=property,type=type,sellable=int(sellable))
            if clas=='Interactive':item= Interactive(clas=clas,name=name,money=int(money),point=int(point),
                                        property=property)                                   
            self.shop.add_item(item)

    def remove(self,choice):
        if choice == 'tavern':
            self.tavern.remove(choice)
        elif choice == 'overlord':
            self.overlord.remove(choice)
        elif choice == 'shop':
            self.shop.remove(choice)
    
    def del_shop(self):
        self.shop = Inventory()
    
    def go_room(self,player,locationTuple):
            dialog('texts\\castle\\castle_main.txt',player,locationTuple)

class River:
    def __init__(self):
        self.name = 'River'
        file = open('data\\river_shop.txt','r').readlines()#shop txt
        self.shop = Inventory()

        for line in file:#creates items in file
            clas,name,money,point,property,type,sellable = line.split(',')
            if clas=='Clothing': item = Clothing(clas=clas,name=name,money=int(money),point=int(point),
                                        property=property,type=type,sellable=int(sellable))
            if clas=='Special': item= Special(clas=clas,name=name,money=int(money),point=int(point),
                                        property=property,type=type,sellable=int(sellable))
            if clas=='Interactive':item= Interactive(clas=clas,name=name,money=int(money),point=int(point),
                                        property=property)                                   
            self.shop.add_item(item)
    
    def go_room(self,player,locationTuple):
        dialog('texts\\river\\river_main.txt',player,locationTuple)

    def del_shop(self):
        self.shop = Inventory()

class Forest:
    def __init__(self):
        self.name = 'Forest'
        file = open('data\\forest_shop.txt','r').readlines()#shop txt
        self.shop = Inventory()

        for line in file:#creates items in file
            clas,name,money,point,property,type,sellable = line.split(',')
            if clas=='Clothing': item = Clothing(clas=clas,name=name,money=int(money),point=int(point),
                                        property=property,type=type,sellable=int(sellable))
            if clas=='Special': item= Special(clas=clas,name=name,money=int(money),point=int(point),
                                        property=property,type=type,sellable=int(sellable))
            if clas=='Interactive':item= Interactive(clas=clas,name=name,money=int(money),point=int(point),
                                        property=property)                                   
            self.shop.add_item(item)
    def del_shop(self):
        self.shop = Inventory()

class Mountain:
    def __init__(self):
        self.name = 'Mountain'
        file = open('data\\mountain_shop.txt','r').readlines()#shop txt
        self.shop = Inventory()

        for line in file:#creates items in file
            clas,name,money,point,property,type,sellable = line.split(',')
            if clas=='Clothing': item = Clothing(clas=clas,name=name,money=int(money),point=int(point),
                                        property=property,type=type,sellable=int(sellable))
            if clas=='Special': item= Special(clas=clas,name=name,money=int(money),point=int(point),
                                        property=property,type=type,sellable=int(sellable))
            if clas=='Interactive':item= Interactive(clas=clas,name=name,money=int(money),point=int(point),
                                        property=property)                                   
            self.shop.add_item(item)
    def del_shop(self):
        self.shop = Inventory()


class RedForest:
    def __init__(self):
        pass
