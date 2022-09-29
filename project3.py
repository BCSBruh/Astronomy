# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 16:20:39 2022

@author: jerom
"""

import numpy as np
import matplotlib.pyplot as plt

long = np.genfromtxt("project3.txt", skip_header=11, delimiter=[12, 3], usecols=1)
lat = np.genfromtxt("project3.txt", skip_header=11, delimiter=[18, 3], usecols=1)

for i in range(len(long)):
    if long[i] > 180:
        long[i] -= 360

index = np.nonzero(np.abs(long) < 90)

xmin = -180
xmax = 180
nbin = 36
width = (xmax - xmin) / nbin

xcenter = np.arange(xmin + 0.5 * width, xmax, width)

freqlong = np.histogram(long, bins=nbin, range=(xmin, xmax))

fig, ax = plt.subplots(1, 3, figsize=(18, 6), constrained_layout=True)

ax[0].set_xlabel("Longitude")
ax[0].set_ylabel("Number of events")
ax[0].axis([xmin, xmax, 0, 40])
ax[0].bar(xcenter, freqlong[0], width=0.8 * width)

xmin = -85
xmax = 85
nbin = 17
width = (xmax - xmin) / nbin

xcenter = np.arange(xmin + 0.5 * width, xmax, width)

freqlat = np.histogram(lat[index], bins=nbin, range=(xmin, xmax))

ax[1].set_xlabel("Latitude")
ax[1].set_ylabel("Number of events")
ax[1].axis([xmin, xmax, 0, 40])
ax[1].bar(xcenter, freqlat[0], width=0.8 * width)

density = np.zeros([len(freqlat[0])])

for i in range(len(freqlat[0])):
    sinb1 = np.rad2deg(np.sin(np.deg2rad(freqlat[1][i])))
    sinb2 = np.rad2deg(np.sin(np.deg2rad(freqlat[1][i+1])))
    area = np.pi * (sinb2 - sinb1)
    density[i] = freqlat[0][i] / area

ax[2].set_xlabel("Latitude")
ax[2].set_ylabel("Density of Clusters")
ax[2].axis([xmin, xmax, 0, 1])
ax[2].bar(xcenter, density, width=0.8 * width)

plt.show()

# plt.savefig("Test.png")