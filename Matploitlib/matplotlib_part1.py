import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y =  x**2

plt.plot(x,y)
plt.ylabel('Y label')
plt.xlabel('X label')
plt.title('Title')
plt.show()

#creating multiple plots on thesame canvas
plt.subplot(1,2,1)
plt.plot(x,y, 'r')
plt.show()

plt.subplot(1,2,1)
plt.plot(x,y, 'b')
plt.show()

# figure method

fig = plt.figure()

axes = fig.add_axes([0.1,0.2,0.5,0.7])
axes.set_xlabel('X label')
axes.set_ylabel('Y label')
axes.set_title('Title')
axes.plot(x,y, 'r--')
plt.show()

############# plot  frame inside a frame
fig2 = plt.figure()

axes1 = fig2.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig2.add_axes([0.2,0.5,0.4,0.3])
axes1.set_xlabel('X1 label')
axes1.set_ylabel('Y1 label')
axes2.set_title('Title1')
axes1.plot(x,y, 'g--')
axes2.set_xlabel('X2 label')
axes2.set_ylabel('Y2 label')
axes2.set_title('Title2')
axes2.plot(x,y, 'r--')

plt.show()
























