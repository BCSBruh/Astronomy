# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 01:27:54 2022
@author: Jerome
"""
#Imports
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

#Function to solve for inclination and declination depending on data and curve-fit
def theFunction(x, i, asc):
    return np.tan(i) * np.sin(x - asc)  #Return the function


#Initial parameter guess for inclination and right ascension
guess = [62, 280]

#Open the file and skip to the correct lines
data = np.genfromtxt('project2.txt', skip_header = 61, skip_footer = 1, delimiter = (10,11))

#Create arrays for right ascension and declination
ra = np.deg2rad(data[:,0])
declination = np.deg2rad(data[:,1])

#Here is the curve fit to solve for inclination and right ascension
#param will give us an array with 2 values that are i, and asc from theFunction
#coval will give us the covariance of the parameters
param, covar = curve_fit(theFunction, ra, np.tan(declination), p0 = guess)

#Creating inclination and right ascension values based on parameters found in curve_fit
inclination = param[0]          #inclination = 61.9801
rightAscension = param[1]       #rightAscension = 278.075

#Standard error of both of the fitted parameters
standardError = np.sqrt(np.diag(covar))
seIncl = standardError[0]       #seIncl = +- 2' 21.920"
seRA = standardError[1]         #seRA = +- 4' 37.558"

#Plotting the celestial equator
x = np.linspace(0, 360, 1000)
y = 0 * x

#Creating the lines to plot the function from the curve fit
xGalaxy = np.linspace(0, 360, 1000)
yGalaxy = theFunction(np.deg2rad(xGalaxy), np.deg2rad(inclination), np.deg2rad(rightAscension))

#Plotting the data
plt.axis([0, 360, -4, 3])       #Creates the axes of the plot. Y is in radians and X is in degrees
plt.figure(figsize=(11, 6))
plt.scatter(np.rad2deg(ra), np.tan(declination), label = 'GCVS4.2 Data')    #Plot the data in a scatter plot
plt.plot(x, y, '--r', label='Celestial Equator')        #Plot the celestial equator

#Plotting the curve with the parameters from the curve fit
plt.plot(xGalaxy, yGalaxy, color='black', lw = 3, label='Galactic Equator')

#Add labels and legend to plot
plt.margins(x=0)
plt.xlabel("Right Ascension (°)")
plt.ylabel(r'$tan(\delta_e)$')
plt.title("Classical Cepheid Stars on Galactic Plane")
plt.legend(loc='upper right')

plt.show()