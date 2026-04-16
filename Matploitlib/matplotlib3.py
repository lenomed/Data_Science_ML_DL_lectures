# Plot Appearances
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1,5,10)
y= np.cos(x)

fig = plt.figure()
axes = fig.add_axes([0.1,0.1,0.8,0.8])
axes.plot(x,y,lw='2', ls='--', color='blue', alpha=0.5,marker='o', markersize=10,
          markerfacecolor='yellow', markeredgecolor='green', markeredgewidth=2)
# the xlim or ylim is used to limit or set the amount of plots on a particular axis
axes.set_xlim([0,2])
axes.set_ylim([0,1])
plt.show()
