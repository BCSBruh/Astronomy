import matplotlib.pyplot as plt
import numpy as np
from lightkurve import search_targetpixelfile as stp

stardes = 'KIC 4282872'
tpf = stp(stardes, author='kepler', cadence='long', quarter=11).download()

tpf_header = tpf.get_header()
star_rad = tpf.get_header()[54]
star_teff = tpf.get_header()[49]
print('Stellar radius = ', star_rad)
print('Stellar effective temperature = ', star_teff)

fig, axes = plt.subplots(2, 3, figsize=(16, 9), constrained_layout=True)

tpf.plot(ax=axes[0][0], frame=0)
lc = tpf.to_lightcurve()
lc.plot(ax=axes[1][0], c='k')

flat_lc = lc.flatten(window_length=401)
flat_lc.plot(ax=axes[0][1], c='k')

pg = flat_lc.to_periodogram(method='bls', period=np.arange(2, 20, 0.001))
pg.plot(ax=axes[1][1], c='k')
periodmax = pg.period_at_max_power

fold_lc = flat_lc.fold(period=periodmax)
axes[1][2].axis([4.05, 4.45, 0.995, 1.003])
fold_lc.scatter(ax=axes[1][2], c='k')

#plt.savefig('HelloLightkurvePlot.png', dpi=250)
plt.show()
