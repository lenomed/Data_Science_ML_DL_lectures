import numpy as np
from matplotlib import pyplot as plt

x = np.arange(0,100)
y = x*2
z = x**2

## Exercise 1

##** Follow along with these steps: **
##* ** Create a figure object called fig using plt.figure() **
##* ** Use add_axes to add an axis to the figure canvas at [0,0,1,1]. Call this new axis ax. **
##* ** Plot (x,y) on that axes and set the labels and titles to match the plot below:**

fig = plt.figure()
axes = fig.add_axes([0.2,0.2,0.7,0.7])
axes.plot(x,y)
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('Title')
plt.show()

### Exercise 2** Create a figure object and put two axes on it, ax1 and ax2.
# Located at [0,0,1,1] and [0.2,0.5,.2,.2] respectively.**

fig = plt.figure()
axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes1.plot(x,y, 'r--')
axes2 = fig.add_axes([0.2,0.4,0.4,0.4])
axes2.plot(x,y, 'r--')
plt.tight_layout()
plt.show()

## Exercise 3

#** Create the plot below by adding two axes to a figure object
# at [0,0,1,1] and [0.2,0.5,.4,.4]**

figr = plt.figure()
axes_1 = figr.add_axes([0.1,0.1,0.8,0.8])
axes_2 = figr.add_axes([0.2,0.5,0.3,0.3])
plt.show()

#** Now use x,y, and z arrays to recreate the plot below. Notice the
# xlimits and y limits on the inserted plot:**

fig_for_lim = plt.figure()
axes_f1= fig_for_lim.add_axes([0.1,0.1,0.8,0.8])
axes_f1.plot(x,y, 'r')
axes_f2= fig_for_lim.add_axes([0.2,0.5,0.3,0.3])
axes_f2.plot(x,y, 'r')
axes_f2.set_xlim(10,20)
plt.show()

## Exercise 4

#** Use plt.subplots(nrows=1, ncols=2) to create the plot below.**

fig,ax = plt.subplots(1,2, figsize=(10,5))
ax[0].plot(x,y, 'r')
ax[1].plot(x,y, 'b')
plt.tight_layout()
plt.show()


