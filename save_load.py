import json

def save(player,locationTuple,lastLocation):
    save_player = {
        'name':player.name,
        'health':player.health,
        'max_health':player.max_health,
        'damage_coef':player.damage_coef,
        'diplo':player.diplo,
        'w_name':player.w_name,
        'w_damage':player.w_damage,
        'char_type':player.char_type,
        'special_event':player.special_event,
        'done_special_event':player.done_special_event,
        'money':player.money
    }
    
    save_castle = {
        'name':locationTuple[0].name,
        'tavern':locationTuple[0].tavern,
        'overlord':locationTuple[0].overlord
    }
    
    save_inventory={}
    for idi,item in enumerate(player.inventory.get_items()):
        saved_item = [item.clas,item.name,item.money,item.point,item.property,item.type,item.sellable]
        save_inventory[idi] = saved_item
    
    save_shop={}
    for idi,item in enumerate(locationTuple[0].shop.get_items()):
        saved_item = [item.clas,item.name,item.money,item.point,item.property,item.type,item.sellable]
        save_shop[idi] = saved_item
    

    with open('save\\save.json', 'w') as sf:
        json.dump([save_player,save_inventory,save_shop,lastLocation.name
                  ,save_castle], sf)
        print('saved')


def load():
    with open('save\\save.json', 'r') as sf:
        data = json.load(sf)
    
    return data

