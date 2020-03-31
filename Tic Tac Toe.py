# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 18:59:24 2020

@author: Nanthakumaran
"""

import numpy

board=numpy.array([["-","-","-"],["-","-","-"],["-","-","-"]])
p1s="X"
p2s="O"

def check_row(symbol):
    for r in range(3):
        count=0
        for c in range(3):
            if board[r][c]==symbol:
                count +=1
        if count==3:
            print(symbol," won")
            return True
    return False

def check_column(symbol):
    for c in range(3):
        count=0
        for r in range(3):
            if board[r][c]==symbol:
                count +=1
        if count==3:
            print(symbol," won")
            return True
    return False

def check_diagonal(symbol):
    if board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[2][2]==board[0][0] and board[1][1]==symbol:
        print(symbol," won")
        return True
    if board[0][2]==board[1][1] and board[1][1]==board[2][0] and board[2][0]==board[0][2] and board[1][1]==symbol:
        print(symbol," won")
        return True
    return False

def won(symbol):
    return check_row(symbol) or check_column(symbol) or check_diagonal(symbol)

def place(symbol):
    while(1):
        print(numpy.matrix(board))
        row=int(input("Enter the row : "))
        col=int(input("Enter the column : "))
        if row>0 and row<4 and col>0 and col<4 and board[row-1][col-1]== "-":
            break
        else:
            print("Invalid place please try again")
    board[row-1][col-1]=symbol

def play():
    for turn in range(9):
        if turn%2==0:
            print("Player 1, You can play now")
            place(p1s)
            if won(p1s):
                break
        if turn%2!=0:
            print("Player 2, You can play now")
            place(p2s)
            if won(p2s):
                break
    if not won(p1s) and not won(p2s):
        print("It's a Draw")

play()