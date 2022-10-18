"""
Created by Jerome Larson
"""

import numpy as np
import matplotlib.pyplot as plt

ngc5024 = np.genfromtxt("NGC 5024.csv", delimiter=",", skip_header=1, usecols=(10, 11))
ngc5904 = np.genfromtxt("NGC 5904.csv", delimiter=",", skip_header=1, usecols=(10, 11))
ngc6229 = np.genfromtxt("NGC 6229.csv", delimiter=",", skip_header=1, usecols=(10, 11))
ngc6341 = np.genfromtxt("NGC 6341.csv", delimiter=",", skip_header=1, usecols=(10, 11))

#Plot 1
g5024 = ngc5024[:, 0]
r5024 = ngc5024[:, 1]

colIndex5024 = g5024 - r5024

#Plot 2
g5904 = ngc5904[:, 0]
r5904 = ngc5904[:, 1]

colIndex5904 = g5904 - r5904

#Plot 3
g6229 = ngc6229[:, 0]
r6229 = ngc6229[:, 1]

colIndex6229 = g6229 - r6229

#Plot 4
g6341 = ngc6341[:, 0]
r6341 = ngc6341[:, 1]

colIndex6341 = g6341 - r6341

#Making Plots
fig, ax = plt.subplots(2,2, layout="constrained")

#Plot 1
ax[0, 0].scatter(colIndex5024, g5024, s=3, color='black')
ax[0, 0].plot(0.31, 20, marker='o', markerfacecolor='none', markeredgecolor='r', markeredgewidth=3, ms=20)
ax[0, 0].axvline(x=0.31, color='r', linestyle='dashed', label='Turnoff Line')
ax[0, 0].text(0.39, 20, "Turnoff Point", fontsize=10, color='r')
ax[0, 0].set_xlim(-0, 1.2)
ax[0, 0].set_ylim(16, 24)
ax[0, 0].invert_yaxis()
ax[0, 0].set_xlabel("g-r [mag]")
ax[0, 0].set_ylabel("g [mag]")
ax[0, 0].set_title("H-R Diagram of NGC 5024")
ax[0, 0].legend(loc='upper right', fontsize=8)

#Plot 2
ax[0, 1].scatter(colIndex5904, g5904, s=3, color='black')
ax[0, 1].plot(0.31, 18.2, marker='o', markerfacecolor='none', markeredgecolor='r', markeredgewidth=3, ms=20)
ax[0, 1].axvline(x=0.31, color='r', linestyle='dashed', label='Turnoff Line')
ax[0, 1].text(0.6, 18.2, "Turnoff Point", fontsize=10, color='r')
ax[0, 1].set_xlim(-0.5, 3)
ax[0, 1].invert_yaxis()
ax[0, 1].set_xlabel("g-r [mag]")
ax[0, 1].set_ylabel("g [mag]")
ax[0, 1].set_title("H-R Diagram of NGC 5904")
ax[0, 1].legend(loc='upper right', fontsize=8)

#Plot 3
ax[1, 0].scatter(colIndex6229, g6229, s=3, color='black')
ax[1, 0].plot(0.35, 21.2, marker='o', markerfacecolor='none', markeredgecolor='r', markeredgewidth=3, ms=20)
ax[1, 0].axvline(x=0.35, color='r', linestyle='dashed', label='Turnoff Line')
ax[1, 0].text(0.45, 21.2, "Turnoff Point", fontsize=10, color='r')
ax[1, 0].set_xlim(-0.3, 1.3)
ax[1, 0].set_ylim(18, 24)
ax[1, 0].invert_yaxis()
ax[1, 0].set_xlabel("g-r [mag]")
ax[1, 0].set_ylabel("g [mag]")
ax[1, 0].set_title("H-R Diagram of NGC 6229")
ax[1, 0].legend(loc='upper right', fontsize=8)

#Plot 4
ax[1, 1].scatter(colIndex6341, g6341, s=3, color='black')
ax[1, 1].plot(0.23, 19.5, marker='o', markerfacecolor='none', markeredgecolor='r', markeredgewidth=3, ms=20)
ax[1, 1].axvline(x=0.23, color='r', linestyle='dashed', label='Turnoff Line')
ax[1, 1].text(0.35, 19.5, "Turnoff Point", fontsize=10, color='r')
ax[1, 1].set_xlim(-0.2, 1.6)
ax[1, 1].set_ylim(18, 24)
ax[1, 1].invert_yaxis()
ax[1, 1].set_xlabel("g-r [mag]")
ax[1, 1].set_ylabel("g [mag]")
ax[1, 1].set_title("H-R Diagram of NGC 6341")
ax[1, 1].legend(loc='upper right', fontsize=8)

plt.savefig("All Clusters.png", dpi=1000)
plt.show()
