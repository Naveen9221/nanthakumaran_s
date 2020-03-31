# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 15:52:44 2020

@author: Nanthakumaran
"""

def count(a,b):
    count=0
    for c in a:
        if c==b:
            count += 1
    return count

def main():
    filename=input("Enter the file_name : ")
    with open(filename+".txt") as f:
        read=f.read()
    for i in "abcdefghijklmnopqrstuvwxyz":
        percentage=100*(count(read,i)/len(read))
        print("{0} : {1}%".format(i,round(percentage,2)))
        

main()