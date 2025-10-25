import matplotlib.pyplot as plt

ax1=plt.subplot2grid((3, 3), (0, 0), colspan=3)
ax2=plt.subplot2grid((3, 3), (1, 0), colspan=2)
ax3=plt.subplot2grid((3, 3), (1, 2), rowspan=2)
plt.show()