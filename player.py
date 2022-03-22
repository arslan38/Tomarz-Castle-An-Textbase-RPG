from items import *

class Player:
    def __init__(self,name,max_health,health,damage_coef,diplo,w_name,w_damage,char_type,special_events={},done_special_events={},money=20):
        self.char_type = char_type
        self.name = name
        self.special_event = special_events
        self.done_special_event = done_special_events
        self.health = health
        self.max_health = max_health#to keep maximum health to regen
        self.damage_coef = damage_coef#damage_coef*damage_range of weapon is final damage
        self.diplo = diplo
        self.w_name = w_name#weapon name
        self.w_damage = w_damage#weapon damage
        self.weapon = Weapon(name=self.w_name,money=50,damage_range=self.w_damage)
        self.money = money
        self.inventory = Inventory() #inventory object

    def set_money(self,value):
        self.money += value

    def set_health(self,value):
        self.health += value
    
    def set_diplo(self,value):
        self.diplo += value
    
    def get_special_events(self): # to reach special events that player did
        return self.special_event
    
    def set_special_event(self,value,id):# set a special events that player did
        self.special_event[value] = id
    
    def del_special_event(self,value):# delete a special events that player did
        del self.special_event[value] 
        self.done_special_event[value] = 1
    

class Inventory:
    def __init__(self):
        self.items = {}
    
    def get_items(self):#to reach values
        return self.items
    
    def remove_items(self,value):#removes
        a = self.items.pop(value)
    
    def add_item(self,item):#adds
        self.items[item]=1
    
    def __str__(self):
        strf=''
        for ide,(element1,element2) in enumerate(self.items.items()): # easyly prints all elements in inventory
            strf += f'{ide+1}.{element1}({element2})\n'
        return strf
    
    


        