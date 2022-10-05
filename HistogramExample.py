# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 16:09:25 2022

@author: jvillavargas
"""

import numpy as np
import matplotlib.pyplot as plt

#---------------------
#-- Read data       --
time = np.genfromtxt('project3.txt', skip_header= 11, delimiter=[12, 3], usecols=1)


#--Time bins
xmin = 0
xmax = 6.0
nbin = 15
width = (xmax-xmin)/nbin
xcenter = np.arange(xmin+0.5*width, xmax, width)


#-- calculate frequency
freqtime = np.histogram(time, bins=nbin, range=(0, 360))
print(freqtime)

#-- plot histogram
fig, ax = plt.subplots(1, 2, figsize=(9,3), constrained_layout=True)
ax[0].set_xlabel("Time")
ax[0].set_ylabel("Number of events")
ax[0].axis([xmin,xmax,0,40])
ax[0].bar(xcenter, freqtime[0], width=0.8*width)

plt.show()

#plt.savefig('HistogramExample.pdf')




