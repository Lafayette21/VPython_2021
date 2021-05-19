import numpy as np
import matplotlib.pyplot as plt

N=10**6
x0=0
y0=0

x=[]
y=[]
x.append(x0)
y.append(y0)

p=np.array(np.random.random(N))

for i in p:
    if i<=0.85:
        xp=0.85*x0+0.04*y0
        yp=-0.04*x0+0.85*y0+1.6
    elif i>0.85 and i<=0.92:
        xp=0.2*x0-0.26*y0
        yp=0.23*x0+0.22*y0+1.6
    elif i>0.92 and i<=0.99:
        xp=-0.15*x0+0.28*y0
        yp=0.26*x0+0.24*y0+0.44
    else:
        x0=0
        y0=0.16*y0
    x0=xp
    y0=yp
    x.append(xp)
    y.append(yp)


plt.plot(x,y,',',color='Lime',ms=4,)
plt.axis([0,0.5,1,1.5])
ax=plt.gca()
ax.set_facecolor('k')

plt.savefig('kwadrat.png',format='png',facecolor='black',dpi=300)
plt.show()
