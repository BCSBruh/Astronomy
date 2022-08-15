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


#--------------------------------------------
#---  Creates plot                        ---
#matplotlib.use('pdf')
fig, ax = plt.subplots(1,1)  # create plot object

#---  set plot parameters  ---
ax.axis([0, 5, 0, 10])
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.set_title("f(x) vs x")

#---  plot scatter points  ---
x1 = np.array([1, 2, 3, 4])   # x-values array
y1 = np.array([1, 4, 2, 8])   # y-values array
ax.plot(x1, y1, label='data points', linestyle='none', marker='x')  # plot points

#---  plot square function  ---
x2 = np.linspace(0, 5, 20)   # x-values array
y2 = 0.40 * x2**2 + 1.0      # y-values array from function
ax.plot(x2, y2, label='squared')   # plot line

#---  plot cubic function  ---
x = np.linspace(0, 5, 20)    # x-values array
ax.plot(x, 0.40*x**3, label='cubic')    # plot line, compute y values on the go 

ax.legend()   # add box with legends inside plotting area

plt.savefig('plot_example1.pdf')   # save pdf file
plt.savefig('plot_example1.png')   # save png file


