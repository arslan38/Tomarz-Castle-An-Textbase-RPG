import os
import sys
import trace
import threading
import time
import random
from LocationClasses import *
from items import *
from termcolor import colored
"""
  In fishing game a started two threads one of them waits input from user other one prints a list continuously.
  Player is controlling a fishing rod and fish try to escape. Player should start pointer reverse of escape way of fish.
  There is also a weight matrix holds propability of catch fish.([0,0,0,0,0,25,50,75,100] for left).
  There is a range contains possible number of moves to catch fish, program picks random value in this range in each fishing session. 
"""

class thread_with_trace(threading.Thread):
  def __init__(self, *args, **keywords):
    threading.Thread.__init__(self, *args, **keywords)
    self.killed = False
  
  def start(self):
    self.__run_backup = self.run
    self.run = self.__run      
    threading.Thread.start(self)
  
  def __run(self):
    sys.settrace(self.globaltrace)
    self.__run_backup()
    self.run = self.__run_backup
  
  def globaltrace(self, frame, event, arg):
    if event == 'call':
      return self.localtrace
    else:
      return None
  
  def localtrace(self, frame, event, arg):
    if self.killed:
      if event == 'line':
        raise SystemExit()
    return self.localtrace
  
  def kill(self):
    self.killed = True
  
i = 0
global flag
flag = True

def func(choice):
    i=8
    k = 1
    while True:
            global list1
            list1 = [0,0,0,0,0,0,0,0,0]
            if i==len(list1)-1:k=1
            if i==0:k=-1
            list1[i] = '-'
            i-=k*1
            if choice=='R': print('Fish escaping to the left!') 
            elif choice=='L': print('Fish escaping to the right!') 
            print(list1)

            time.sleep(0.041)
            os.system('cls')
            #Input = input()

def start(choice):
    t1 = thread_with_trace(target = func,args = (choice,))
    t1.start()
    input()
    t1.kill()
    t1.join()
    os.system('cls')
    print(list1)
    distance = len(list1)//2 - list1.index('-')
    return list1.index('-'),distance

def fishing(player,locationTuple):
    listwL = [100,75,50,25,0,0,0,0,0]#weight matrices
    listwR = [0,0,0,0,0,25,50,75,100]#weight matrices

    print('You control the fishing rod. You have to turn your fishing rod in the opposite direction of the fish maneuvering. The farther you stop the moving sign, the more chance you have of holding it.!')
    input(colored('Press any key to continue...', 'yellow'))

    rangeRL = random.randint(3,5)#range catch
    i = 0
    for i in range(rangeRL):
        choice = random.choice(['R','L']) # the direction the fish is trying to escape(right or left)
        index,dist = start(choice)
        
        if choice=='R':
            if random.randint(0,100)<listwR[index]:#propability
                i +=1
                input('The move is successful !')
            else:
                print('Fish escaped !')
                input(colored('Press any key to continue...', 'yellow'))
                locationTuple[1].go_river_koy(player,locationTuple)
        if choice=='L':
            if random.randint(0,100)<listwL[index]:#propability
                
                i+=1
                input('The move is successful !')
            else:
                print('Fish escaped !')
                input(colored('Press any key to continue...', 'yellow'))
                

    if i==rangeRL:
        os.system('cls')
        print('You caught the fish!')
        item= Interactive(clas='Interactive',name='Fish',money=20,point=10,
                                        property='Health')   
        player.inventory.add_item(item)#adds fish item

        input(colored('Press any key to continue...', 'yellow'))

def music():
    from playsound import playsound
    playsound('data\\music2.mp3')

def start_music():
    t1 = thread_with_trace(target = music)
    t1.start()



