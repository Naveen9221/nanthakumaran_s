# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 07:44:39 2020

@author: Nanthakumaran
"""

from random import randint as dice
import time

def time_delay():
    for n in range(5):
        print("Rolling....")
        time.sleep(1)

def thank(a,b):
    print("Thanks for paying this game")
    print("{0}, your score is {1}".format(a,b))
    print("Hope you enjoy this game :)")

def main():
    print("Welcome to this game")
    pp1=input("Enter your name : ")
    po=0
    while(1):
        print("Rolling a dice.....")
        time_delay()
        secret_number=int(dice(1,6))
        choise=int(input("What's your guess : "))
        if(secret_number==choise):
            print("Hurray you nailed it!")
            po += 1
        elif(secret_number>choise):
            print("You're too low!\nKeep Trying")
        elif(secret_number<choise):
            print("You're too high!\nKeep Trying")
            
        descision=input("Can we continue : Y/N : ")
        descision.lower()
        if(descision=='n'):
            break
    thank(pp1,po)

main()