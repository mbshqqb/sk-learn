import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0,2*np.pi,0.1*np.pi)
ss=np.sin(x)
cc=np.cos(x)
plt.plot(x,ss)
plt.plot(x,cc)
plt.show()