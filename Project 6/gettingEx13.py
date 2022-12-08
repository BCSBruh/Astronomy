import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator)
from lightkurve import search_targetpixelfile

def mass(gsun, gstar, rstar):
    logM = gstar - gsun + 2*np.log(rstar)
    print(2*np.log(rstar), ", ", (gstar - gsun))
    return np.exp(logM)

stardes1 = 'KIC 757450'   # Kepler-818 b , quarter=8
tpf1 = search_targetpixelfile(stardes1, author='Kepler', quarter=8).download()

stardes2 = 'KIC 8191672'   # Kepler-818 b , quarter=8
tpf2 = search_targetpixelfile(stardes2, author='Kepler', quarter=8).download()

gSun = np.log(27400)

star_logg1 = tpf1.get_header()[50]   # log(g) star surface gravity
print('Stellar surface gravity, log(g1) =', star_logg1)

star_logg2 = tpf2.get_header()[50]   # log(g) star surface gravity
print('Stellar surface gravity, log(g2) =', star_logg2)

star_rad1 = tpf1.get_header()[54]   # stellar radius
star_teff1 = tpf1.get_header()[49]   # stellar effective temperature

star_rad2 = tpf2.get_header()[54]   # stellar radius
star_teff2 = tpf2.get_header()[49]   # stellar effective temperature

print('Mass of Star 1 = ', mass(gSun, star_logg1, star_rad1))
print('Mass of Star 2 = ', mass(gSun, star_logg2, star_rad2))
