import matplotlib.pyplot as plt
import numpy as np
r=2
n=np.arange(0,2,1/180)
x=np.sin(np.pi*n)*r
y=np.cos(np.pi*n)*r
plt.plot(x,y)
plt.show()