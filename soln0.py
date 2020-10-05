# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 20:37:51 2020

@author: aksha
"""

import numpy as np
x= int(input("enter first number"))
y = int(input("enter sencond number"))

def ps0(x,y):
    return x**y , np.log2(x)


ans1 , ans2 = ps0(x,y)
print(ans1 , ans2, sep = "and")