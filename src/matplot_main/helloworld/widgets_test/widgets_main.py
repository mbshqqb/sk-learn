import numpy as np
import matplotlib.pyplot as plt
import matplotlib.widgets as widgets
r=2
n=np.arange(0,2,1/180)
x=np.sin(np.pi*n)*r
y=np.cos(np.pi*n)*r

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)
line,=plt.plot(x,y)
plt.plot(x-1,y)
def next(event):
    plt.plot(x,y+1)#为什么把图绘到了button上？？？？？？？？？
    line.set_ydata(y+1)
    plt.draw()
ax_btn = plt.axes([0.81, 0.05, 0.1, 0.075])
btn=widgets.Button(ax_btn,'Previous')
btn.on_clicked(next)

plt.show()