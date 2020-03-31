# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 20:11:04 2020

@author: Nanthakumaran
"""

def binary_search(l,x,start,end):
    
    if start==end:
        if l[start]==x:
            return start
        else:
            return -1
        
    else:
        mid=int((start+end)/2)
        if l[mid]==x:
            return mid
        elif x<mid:
            return binary_search(l,x,start,mid-1)
        elif x>mid:
            return binary_search(l,x,mid+1,end)
        
def main():
    n=int(input("Enter the number of elements in the list : "))
    list1=[]
    for i in range(n):
        ele=int(input("Enter the element : "))
        list1.append(ele)
    x=int(input("Enter the number to be searched : "))
    list1.sort()
    r=binary_search(list1,x,0,len(list1)-1)
    if r==-1:
        print("There is no such element")
    else:
        print("The element is found at the position ",r+1)
    
main()