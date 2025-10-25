from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

fig =plt.figure()
ax=plt.axes(projection='3d')
x =np.arange(10)
y=np.sin(x)
z=np.cos(x)

ax.plot(x,y,z)
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
print(x)

plt.show()
