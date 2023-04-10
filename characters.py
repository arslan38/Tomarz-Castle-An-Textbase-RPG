import random
import time

#req_diplo is required diplomatic point to convince enemy not to fight.
#each enemy can give damage in damage_coef*(damage_range) range.
class Enemy:
    def __init__(self,type,name,damage_range_s,damage_range_e,damage_coef,damage_str,health_range_s,health_range_e,req_diplo):
        self.type = type
        self.damage_coef = float(damage_coef)
        self.damage = damage_str
        self.health = random.randint(int(health_range_s),int(health_range_e))
        self.req_diplo = int(req_diplo)
        self.damage_range = [int(damage_range_s),int(damage_range_e)]
        self.name = name

class NPC:
    def __init__(self,type,name,damage_range_s,damage_range_e,damage_coef,damage_str,health_range_s,health_range_e):
        pass


