"""
Created by Jerome Larson
"""

import matplotlib.pyplot as plt

ngc5024 = plt.imread("NGC 5024.png")
ngc5904 = plt.imread("NGC 5904.png")
ngc6229 = plt.imread("NGC 6229.png")
ngc6341 = plt.imread("NGC 6341.png")

fig, ax = plt.subplots(2,2, layout='constrained')
ax[0, 0].axis('off')
ax[0, 0].imshow(ngc5024, cmap='gray')
ax[0, 0].set_title("NGC 5024")

ax[0, 1].axis('off')
ax[0, 1].imshow(ngc5904, cmap='gray')
ax[0, 1].set_title("NGC 5904")

ax[1, 0].axis('off')
ax[1, 0].imshow(ngc6229, cmap='gray')
ax[1, 0].set_title("NGC 6229")

ax[1, 1].axis('off')
ax[1, 1].imshow(ngc6341, cmap='gray')
ax[1, 1].set_title("NGC 6341")
plt.savefig("All Clusters Together.png", transparent=True, dpi=1000)
plt.show()
