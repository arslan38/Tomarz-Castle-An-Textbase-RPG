import random

class Items:
    def __init__(self,name,money):
        pass

#a item can be sellable or not.
#a weapon can be given damage in damage_range range randomly.
class Weapon(Items):
    def __init__(self,name,money,damage_range,sellable=1):
        self.name = name
        self.money = money
        self.damage_range = damage_range
        self.sellable = sellable


class Clothing(Items):
    def __init__(self,clas,name,money,point,property,type,sellable=1):
        self.clas = clas
        self.name = name
        self.money = money
        self.sellable = sellable
        self.point = point
        self.property = property
        self.type = type
    
    #if item has permanent propert like +15 Health +3 Diplo this function will apply or delete these properties that comes from items.
    def apply_property(self,player):
        if self.property =='Health':
            player.max_health+=self.point
        elif self.property =='Diplo':
            player.set_diplo(self.point)

    def delete_property(self,player):
        if self.property =='Health':
            player.max_health-=self.point
            player.health= player.max_health
        elif self.property =='Diplo':
            player.set_diplo(-1*self.point)    

    def __str__(self):
        return f'{self.name}[{self.money} GOLD][{self.type} item][+{self.point} {self.property}]'
    

class Special(Items):
    def __init__(self,clas,name,money,point,property,type,sellable):
        self.clas = clas
        self.name = name#item name
        self.money = money#value
        self.point = point
        self.property = property
        self.sellable = False
        self.type = 'Special'
    def __str__(self):
        return f'{self.name}[{self.money} GOLD][{self.type} item]'


class Interactive (Items):
    def __init__(self,clas,name,money,point,property,type=None,sellable=1):
        self.clas = clas#Interactive
        self.name = name#item name
        self.money = money#value
        self.point = point#Point of property like 15. Defined for apply property
        self.property = property# Like health or damage. Defined for apply property
        self.sellable = sellable
        self.type = 0
    
    #if item has instant propert like +15 Health +20 Attack this function will apply or delete these properties that comes with items.
    def apply_property(self,player,enemy=None):
        if self.property =='Health':
            if player.health +self.point>player.max_health:#if property+health is bigger than max then health should be equal to max.
                player.health=player.max_health
            else:
                player.health += self.point
        elif self.property =='Attack':
            enemy.health -= self.point

    def __str__(self):
        return f'{self.name}[{self.money} GOLD][+{self.point} {self.property}]'
    
