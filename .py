import matplotlib.pyplot as plt
import numpy as np

circle = plt.Circle((0, 0), 1, color='blue', fill=False)

fig, ax = plt.subplots()
ax.add_artist(circle)
ax.set_aspect('equal')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.axhline(0, color='black',linewidth=0.5)
ax.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.title('Circle')
plt.show()