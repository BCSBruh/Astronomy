# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 16:34:21 2022

@author: jerom
"""

import numpy as np
import matplotlib.pyplot as plt

long = np.genfromtxt("project3.txt", skip_header=11, delimiter=[12, 3], usecols=1)
lat = np.genfromtxt("project3.txt", skip_header=11, delimiter=[18, 3], usecols=1)

color = np.genfromtxt("project3.txt", skip_header=11, delimiter=[24, 4], usecols=1)

for i in range(len(long)):
    if long[i] > 180:
        long[i] -= 360

index = np.nonzero(np.abs(long) < 90)

lat = lat[index]
color = color[index]

csclat = 1 / (np.sin(np.deg2rad(np.abs(lat))))

csclat = np.delete(csclat, 60)
color = np.delete(color, 60)

xones = np.ones([csclat.size])
a = np.vstack([csclat, xones])

a = a.T

m, c = np.linalg.lstsq(a, color, rcond=None)[0]
xdata = np.linspace(0, 20, 100)

plt.scatter(csclat, color, label='Data')
plt.xlabel(r'$csc(b)$')
plt.ylabel(r'$(B-V)_{obs}$')

plt.margins(x=0)
plt.plot(xdata, m*xdata + c, 'r', label='Fitted Line')
plt.legend()

#plt.savefig("ColorIndex.png", dpi=275)
plt.show()
