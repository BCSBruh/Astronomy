# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 16:48:10 2022

@author: Jerome
"""

import numpy as np

def quadratic():
    print("Input a, b, and c of your quadratic equation:\n")
    a = int(input('a = '))
    b = int(input('b = '))
    c = int(input('c = '))

    root = b**2 - (4*a*c)
    
    if (root > 0 and a != 0):
        x1 = (-b + np.sqrt(root)) / (2*a)
        x2 = (-b - np.sqrt(root)) / (2*a)
        print(x1, x2)
            
    elif (root == 0 and a != 0):
        x = (-b) / (2*a)
        print(x)

    elif (root < 0 and a != 0):
        print("No real solutions.")
        
    elif (a == 0):
        x = -(c/b)
        print(x)
        
    else:
        print("Invalid values. Try again...\n")
        quadratic()
        
quadratic()
        