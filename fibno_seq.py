# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 14:06:46 2021

@author: zahid
"""
def recu_fibno(x):
    if x < 1:
        return x
    else:
        return(recu_fibno(x-1) + recu_fibno(x-2))
    
num = int(input("enter how many number Fibonacci sequence?"))
if num <= 0:
    print("enter a postive number")
else:
    print("Fibonacci sequence")
    for i in range(num):
        print(-recu_fibno(i))

     