import matplotlib.pyplot as plt
from lightkurve import search_targetpixelfile as stp

stardes = 'KIC 4282872'
tpf = stp(stardes, author='kepler', cadence='long', quarter=11).download()

tpf_header = tpf.get_header()
star_rad = tpf.get_header()[54]
star_teff = tpf.get_header()[49]
print('Stellar radius = ', star_rad)
print('Stellar effective temperature = ', star_teff)

fig, axes = plt.subplots(2, 1, figsize=(6,9), constrained_layout=True)

tpf.plot(ax=axes[0], frame=0)
lc = tpf.to_lightcurve()
lc.plot(ax=axes[1], c='k')
plt.show()
plt.savefig('HelloLightkurvePlot.png', dpi=250)
