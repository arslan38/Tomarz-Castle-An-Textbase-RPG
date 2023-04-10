import random
def check(Input,range):
    try:
        intInput = int(Input)
        if range[0]<=intInput<=range[1]:
            return True
        else:
            return False
    except:
        return False

def olasılık(boundary):
    if random.randint(0,100)>=boundary: return True
    else: return False

    
def effify(non_f_str: str,player,enemy=None,enemy_name=None,location=None):
    return eval(f'f"""{non_f_str}"""')