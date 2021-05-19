import matplotlib.pyplot as plt
import random as r

N=10**6

def middleX(x1,x2):
    return (x1+x2)/2

def middleY(y1,y2):
    return (y1+y2)/2

x0=r.random()
y0=r.random()

A=[0,0]
B=[1,0]
C=[0.5,1]

x=[x0]
y=[y0]

plt.figure(figsize=(8,6.9))

for i in range(N):
    T=r.choice([A,B,C])
    xp=middleX(x[i],T[0])
    yp=middleY(y[i],T[1])
    x.append(xp)
    y.append(yp)

plt.plot(x,y,'r,',ms=3)
plt.savefig('zad1.png',format='png')

plt.show()





