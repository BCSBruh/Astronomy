# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 16:46:08 2022

@author: Jerome
"""

import matplotlib.pyplot as plt
import numpy as np

#with open("asteroiddatabase.csv", newline='') as csvfile:
 #   adb = csv.reader("asteroiddatabase.csv", delimiter = ",")
    
infile = 'asteroiddatabase.csv'
det = np.genfromtxt(infile, skip_header=9, skip_footer=0, max_rows = 3000, delimiter=',')

"""column1 = name
column2 = eccentricity
column3 = semi-major axis
column4 = perihelion distance
column5 = inclination
column6 = diameter
column7 = period
column8 = classification"""

eccentricity = det[:,1]
semiMajor = det[:,2]
perihelion = det[:,3]
inclination = det[:,4]
diameter = det[:,5]
period = det[:,6]

sinOfInc = np.sin((inclination * np.pi) / 180)
height = [sinOfInc * semiMajor]

#Plot 0,0 is period v semiMajor
fig, ax = plt.subplots(2,2, constrained_layout=True)
ax[0][0].axis([0, 7, 0, 15])
ax[0][0].scatter(semiMajor, period, s=4, c='blue', marker='o')
ax[0][0].set_xlabel("a (AU)")
ax[0][0].set_ylabel("p (km)")

#plot 0,1 is height v semiMajor
ax[0][1].axis([2.0, 3.5, 0, 2])
ax[0][1].scatter(semiMajor, height, s=2, c='red', marker='x')
ax[0][1].set_xlabel("a (AU)")
ax[0][1].set_ylabel("Height (AU)")

#plot 1,0 is eccentricity v semiMajor
ax[1][0].axis([2.0, 3.5, 0, 0.5])
ax[1][0].scatter(semiMajor, eccentricity, s=1, c='black')
ax[1][0].set_xlabel("a (AU)")
ax[1][0].set_ylabel("Eccentricity")

#plot 1,1 is inclination v semiMajor
ax[1][1].axis([2.0, 3.5, 0, 20])
ax[1][1].scatter(semiMajor, inclination, s=2, c='green')
ax[1][1].set_xlabel("a (AU)")
ax[1][1].set_ylabel(r"$Inclination (^o)$")

plt.savefig('AsteroidDatabase.pdf')
