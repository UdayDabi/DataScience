import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.0, 2, 0.01)      # step fix
y1 = np.sin(2 * np.pi * x)
y2 = 1.2 * np.sin(4 * np.pi * x)

fig, ax = plt.subplots(1, sharex=True)
ax.plot(x, y1, x, y2, color='black')

ax.fill_between(x, y1, y2, where=(y2 >= y1), color='blue')
ax.fill_between(x, y1, y2, where=(y2 < y1), color='red')

ax.set_title('fill_between where')
plt.show()
