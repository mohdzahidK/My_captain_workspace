# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 15:04:06 2021

@author: zahid
"""
def most_frequent(s):
    li1 = ["m","i","s","p"]

    for i in li1:
       
      # for j in li2:
         j = s.count(i)
         print(i ,"=",j)
         

st = "mississippi"
most_frequent(st)
