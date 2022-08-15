# -*- coding: utf-8 -*-

"""
Spyder Editor

Creates a simple example of a plot.
No input parameters are required.
"""

# import matplotlib
import matplotlib.pyplot as plt
import numpy as np

print("Hello!")
print("π")


#--------------------------------------------
#---  Creates plot                        ---
#matplotlib.use('pdf')
fig, ax = plt.subplots(1,1)  # create plot object

#---  set plot parameters  ---
ax.axis([0, 2, -2, 2])  # axes limits 0 <=x<=1. -2<=y<= 2
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.set_title("Saw Function - Fourier Harmonics")

#---  plot square function  ---
x = np.linspace(0, 2, 500)   # array of 20 values between 0 and 5

#Creating the fourier functions
f1 = ((-2 / np.pi) * np.sin(2*np.pi*x))
f2 =((-1 / np.pi) * np.sin(4*np.pi*x))
f3 = ((-2 / (3 *np.pi)) * np.sin(6*np.pi*x))
f4 = ((-1 / (2 *np.pi)) * np.sin(8*np.pi*x))
f5 = ((-2 / (5 *np.pi)) * np.sin(10*np.pi*x))

y1 = f1
y2 = f1 + f2 + f3
y3 = f1 + f2 + f3 + f4 + f5

ax.plot(x, y1, label='1 Harmonic')   # plot line
ax.plot(x, y2, label='3 Harmonics')   # plot line
ax.plot(x, y3, label='5 Harmonics')   # plot line

ax.legend()   # add box with legends inside plotting area

plt.savefig('plot_Harmonics.pdf')   # save pdf file
plt.savefig('plot_Harmonics.png')   # save png file

#
