# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator)
from lightkurve import search_targetpixelfile


#---------------------------
#----   My second star  ----

#-- Prepare plotting axes
fig, axes = plt.subplots(3, 2, figsize=(12,9), constrained_layout=True)

#-- Download target pixel file
stardes = 'KIC 4282872'   # Kepler-818 b , quarter=8
tpf = search_targetpixelfile(stardes, author='Kepler', quarter=8).download()

#-- print some information from header
tpf_header = tpf.get_header()   # metadata header
star_rad = tpf.get_header()[54]   # stellar radius
star_teff = tpf.get_header()[49]   # stellar effective temperature
print('Stellar radius =', star_rad)
print('Stellar effective temperature =', star_teff)

#-------------------------------------------
#--  Cadence image
#-------------------------------------------
tpf.plot(ax=axes[0][0], frame=0)  # Plot first cadence

#-------------------------------------------
#--  light curve
#-------------------------------------------
#-- Extract light curve from pixel file
#-- An aperture mask is passed. Only pixels in the aperture are summed to
#-- create lightcurve.
#-- pipeline_mask calls the default pipeline aperture, which is a boolean numpy array
lc = tpf.to_lightcurve(aperture_mask=tpf.pipeline_mask)   #  extract light curve and mask
lc.plot(ax=axes[0][1], c='k')
#flat_lc = lc.flatten(window_length=401).remove_outliers(sigma=1)   # flatten light curve
flat_lc = lc.flatten(window_length=401)   # flatten light curve
flat_lc.plot(ax=axes[1][0], c='k')
#lc.plot(ax=axes[0][1], c='k')

#-------------------------------------------
#--  Periodogram
#-------------------------------------------
pg = flat_lc.to_periodogram(method='bls', period=np.arange(2, 20, 0.001))
pg.plot(ax=axes[1][1], c='k')
periodmax = pg.period_at_max_power  # find peak
print('Best fit period: {:.5f}'.format(periodmax))

#-------------------------------------------
#--  Folded lightcurve 
#-------------------------------------------
fold_lc = flat_lc.fold(period=periodmax)
binned_lc = fold_lc.bin(time_bin_size=0.002)
#-- Folded flux
axes[2][0].tick_params(which='both', axis='both',       # ticks inside box
                    direction='in', top=True, right=True) 
fold_lc.scatter(ax=axes[2][0], c='k')

#-- Eclipse close-up
axes[2][1].axis([4.05, 4.45, 0.995, 1.003])
axes[2][1].xaxis.set_minor_locator(MultipleLocator(0.01))
axes[2][1].tick_params(which='both', axis='both',       # ticks inside box
                    direction='in', top=True, right=True) 
axes[2][1].axhline(y=0.9974, color="blue", linestyle="--")  # vertical line
axes[2][1].axvline(x=4.16, color="blue", linestyle="--")  # vertical line
axes[2][1].axvline(x=4.29, color="blue", linestyle="--")  # vertical line
fold_lc.scatter(ax=axes[2][1], c='k')


plt.savefig('Exoplanet_KIC-4282872.png')
plt.show()

#---  End of code  ---