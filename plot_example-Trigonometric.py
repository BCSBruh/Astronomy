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
ax.axis([0, 2.0*np.pi, -2, 2])  # axes limits 0 <=x<=1. -2<=y<= 2
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.set_title("Trigonometric Functions")

#---  plot square function  ---
x = np.linspace(0, 2.0*np.pi, 500)   # array of 20 values between 0 and 5

y1 = np.sin(x) 
y2 = np.cos(x) 
y3 = np.sin(x) * np.cos(x) 

ax.plot(x, y1, label='sine')   # plot line
ax.plot(x, y2, label='cosine')   # plot line
ax.plot(x, y3, label='sine * cosine')   # plot line

ax.legend()   # add box with legends inside plotting area

plt.savefig('plot_Trigonometric.pdf')   # save pdf file
plt.savefig('plot_Trigonometric.png')   # save png file

#
