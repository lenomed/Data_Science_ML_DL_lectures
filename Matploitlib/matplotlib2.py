import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 0.1)
y = np.sin(x)
# using subplots instead of creating or asigningfigure to variables as many times as the axes you want
# it is use for subplots that you waant to arrange in rows and columns

fig,axes = plt.subplots(nrows=1,ncols=2)
axes[0].plot(x,y, 'r')
axes[1].plot(y,x, 'b')
plt.tight_layout
plt.show()

#figure size aspecr ratio and DPI
fig2 = plt.figure( figsize = (8,5)) # you can still replace figure with sub plot here incase you are creating a subplot
axes2 = fig2.add_axes([0.1,0.1,0.8,0.8])
axes2.plot(x,x, 'b', label = 'arrange(0,10')
axes2.plot(y,y, 'r--', label = 'sing(x)')
axes2.legend(loc = 'best')# you can use a tuple here to specify the position of your legend
###saving a pic
##fig2.savefig('test.png', dpi=300) # saving an image
plt.show()



