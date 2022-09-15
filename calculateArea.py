# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 16:07:08 2022

@author: Jerome
"""

import numpy as np
import quadraticEquation as qe

def calculation():
    print("What shape do you want the area of?\n\t(1) Triangle\n\t(2) Rectangle\n\t(3) Circle\n\t(4) Quit")

    shape = int(input())
    if (shape == 1):
        base = int(input("Input base: "))
        height = int(input("Input height: "))
        area = 0.5 * base * height
        print(area, "\n")
            
    elif (shape == 2):
        length = int(input("Input length: "))
        height = int(input("Input height: "))
        area = 2 * length + 2 * height
        print(area, "\n")

    elif (shape == 3):
        radius = int(input("Input radius of the circle: "))
        area = np.pi * radius**2
        print(area, "\n")
        
    elif (shape == 4):
        print("Goodbye")
            
    else:
        print('Invalid option')
        calculation()

    if (shape != 4):
        calculation()

calculation()

qe.quadratic()