import math
import random
import matplotlib.pyplot as plt
from matplotlib import animation

N=10000
x0=[]
y0=[]
x=[]

fig, a=plt.subplots()

for i in range(N+1):
    x0.append(10*random.random())
    y0.append(10*random.random())
    x.append(0)

def run(frame):
	plt.clf()
	for i in range(N+1):
		x[i]=x0[i]+2*math.sin(x0[i]-frame)
	plt.scatter(x,y0,s=1,color='r')
	ax=plt.gca()
	ax.set_aspect(1)
	plt.xlim([1,9])
	plt.ylim([1,9])
	ax.set_facecolor('xkcd:black')
    
ani=animation.FuncAnimation(fig,run,interval=1)
writervideo = animation.FFMpegWriter(fps=10)
ani.save('swani.mp4', writer=writervideo)
plt.show()
