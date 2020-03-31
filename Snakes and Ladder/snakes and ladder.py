# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 10:46:18 2020

@author: Nanthakumaran
"""

from PIL import Image
import random
import time

end=100

def show_board():
    img= Image.open("snakes_and_ladder.jpg")
    img.show()
    
def check_ladder(points):
    if points==1:
        print("Ladder")
        return 38
    elif points==4:
        print("Ladder")
        return 14
    elif points==9:
        print("Ladder")
        return 31
    elif points==21:
        print("Ladder")
        return 42
    elif points==28:
        print("Ladder")
        return 84
    elif points==51:
        print("Ladder")
        return 67
    elif points==72:
        print("Ladder")
        return 91
    elif points==80:
        print("Ladder")
        return 99
    else:
        return points
    
def check_snake(points):
    if points==17:
        print("Snake")
        return 7
    elif points==54:
        print("Snake")
        return 34
    elif points==62:
        print("Snake")
        return 19
    elif points==64:
        print("Snake")
        return 60
    elif points==87:
        print("Snake")
        return 36
    elif points==93:
        print("Snake")
        return 73
    elif points==95:
        print("Snake")
        return 75
    elif points==98:
        print("Snake")
        return 79
    else:
        return points
        
def reached(points): 
    if points==end:
        return True
    else:
        return False

def play():
    pp1=input("Player 1, Enter your name : ")
    pp2=input("Player 2, Enter your name : ")
    po1=0
    po2=0
    turn=0
    while(1):
        if turn %2 ==0:
            print("It's ",pp1 ," turn")
            c=input("If you want to quit this game : Y/N : ")
            c.lower()
            if c=='n':
                print("Thanks for playing this game")
                print(pp1, "'s point is : ",po1)
                print(pp2, "'s point is : ",po2)
                break
            dice=random.randint(1,6)
            time.sleep(1)
            print("The dice number is : ",dice)
            po1=po1+dice
            
            po1=check_ladder(po1)
            po1=check_snake(po1)
            
            if po1>end:
                po1=end
            
            print("Your position is : ",po1)
            
            if reached(po1):
                print(pp1," You won it !")
                break
            
        else:
            print("It's ",pp2 ," turn")
            c=input("If you want to quit this game : Y/N : ")
            c.lower()
            if c=='n':
                print("Thanks for playing this game")
                print(pp1, "'s point is : ",po1)
                print(pp2, "'s point is : ",po2)
                break
            dice=random.randint(1,6)
            time.sleep(1)
            print("The dice number is : ",dice)
            po2=po2+dice
            
            po2=check_ladder(po2)
            po2=check_snake(po2)
            
            if po2>end:
                po2=end
            
            print("Your position is : ",po2)
            
            if reached(po2):
                print(pp2," You won it !")
                break
        
        if dice==6:
            continue
        else:
            turn=turn +1
            
        print("\n")

show_board()
play()
