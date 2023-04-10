import sys
import time

#flowing text
def alter_print(text1):
    for character in text1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.04)#0.04
    print('')