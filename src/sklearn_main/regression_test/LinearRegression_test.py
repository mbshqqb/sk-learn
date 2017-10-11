import numpy as np
import matplotlib.pyplot as plt
import sklearn.linear_model as linear_model

x=np.linspace(0,10,100).reshape(100,1)
y=10-np.square(x-5)
plt.scatter(x,y)
plt.plot(x,y)

regression=linear_model.Ridge()
regression.fit(x, y)

z=regression.predict(x)

plt.plot(x,z)
plt.show()