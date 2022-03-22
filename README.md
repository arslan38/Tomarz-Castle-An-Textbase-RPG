# Tomarz-Castle-An-Textbase-RPG

This repository contains a textbase prg game engine that coded with python.

#### İmportant Note: A lot of things in this project can be changed without coding. Simply attempt to embrace the point and make the changes.

--- 

### Requirements:

```
Python 3.6+
pip install -r requirements.txt
```

--- 

### How It Works:

```
py storyline.py
```

#### Algorithm in Python

##### Main Dialogs and Connections 
- The text files include all of the dialogs and connections (can be found in texts folder). This structure may be seen as a graph. A location, sub-location, or npc is represented by each text file. Text files can be linked together and have sub-trees.

<img width="820" alt="Adsız" src="https://user-images.githubusercontent.com/49092119/159474682-55ddd1c6-0bb3-4122-ade8-c6cda305c56c.png">

##### Enemies
- 

<img width="282" alt="enemy" src="https://user-images.githubusercontent.com/49092119/159475337-43078b81-b2ac-44f7-a716-fd254221ee09.png">


##### Shop
- 

<img width="443" alt="shop" src="https://user-images.githubusercontent.com/49092119/159475378-b555bb45-5425-47dc-8ede-c04dd9459e50.png">

##### List of Actions

<img width="167" alt="actions" src="https://user-images.githubusercontent.com/49092119/159476117-3820c912-07bb-4bfe-a3d6-520508391595.png">

##### Map and Storyline
- There are multiple ends in the main storyline.
- This is a game that takes place in an open world. The player is allowed to travel wherever he/she wants and engage with whoever he/she wants!

<img width="942" alt="Resim1" src="https://user-images.githubusercontent.com/49092119/159476342-3fb87639-9aff-4541-a80f-03c89c427e10.png">

##### Save File
- If the player changes their location, the game saves.
- You can find the example of save.json below.
```
[{"name": "mert", "health": 25, "max_health": 25, "damage_coef": 1.5, "diplo": 10, "w_name": "Baton", "w_damage": [7, 12], "char_type": "Diplomat", "special_event": {"Nakres Mission": 0}, "done_special_event": {}, "money": 985}, {"0": ["Interactive", "Apple", 15, 15, "Health", 0, 1]}, {"0": ["Clothing", "Simple Belt", 20, 1, "Diplo", "waist", 1], "1": ["Clothing", "Embroidered  Belt", 100, 4, "Diplo", "waits", 1], "2": ["Clothing", "Caftan", 100, 4, "Diplo", "body", 1], "3": ["Clothing", "Old Boots", 10, 5, "Health", "foot", 1], "4": ["Clothing", "Guard Boots", 50, 15, "Health", "foot", 1], "5": ["Special", "Talking Parrot", 400, 0, "0", "Special", false], "6": ["Interactive", "Bird Heart", 20, 20, "Health", 0, 1], "7": ["Interactive", "A Bottle of Flammable Alcohol", 50, 50, "Attack", 0, 1], "8": ["Interactive", "Throwable Axe", 30, 25, "Attack", 0, 1], "9": ["Interactive", "a Big Stone ", 10, 10, "Attack", 0, 1], "10": ["Interactive", "Flower Essence Mix ", 50, 35, "Health", 0, 1]}, "Castle", {"name": "Castle", "tavern": ["Nakres", "Afatsum"], "overlord": ["Mission"]}]
```
--- 








 

