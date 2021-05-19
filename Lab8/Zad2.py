from vpython import *
import random as r

scene=canvas(width=550,height=580)

L=[]

for i in range(40):
    ball = sphere(pos=vector(0,0,0),radius=0.8, color=color.red)
    L.append(ball)

wallR=box(pos=vector(3.8,0,0), size=vector(0.5,7,7), color=color.blue)
wallL=box(pos=vector(-3.8,0,0),size=vector(0.5,7,7), color=color.green)
wallUp=box(pos=vector(0,3.5,0),size=vector(0.5,7,7), color=color.orange)
wallBot=box(pos=vector(0,-3.5,0),size=vector(0.5,7,7), color=color.red)
wallBack=box(pos=vector(0,0,-3.5),size=vector(0.5,7,7), color=color.cyan)

wallUp.rotate(angle=radians(90),axis=vector(0,0,1))
wallBot.rotate(angle=radians(90),axis=vector(0,0,1))
wallBack.rotate(angle=radians(90),axis=vector(0,1,0))

for i in L:
    i.vel=vector(r.random(),r.random(),r.random())



t=0
dt=0.005

while t<100:
    for i in L:
        rate(10000)
        i.pos=i.pos+i.vel*dt
        if abs(i.pos.x)>=wallR.pos.x-1:
            i.vel.x=-i.vel.x
            i.color=vector(r.random(),r.random(),r.random())
        elif i.pos.z<=wallBack.pos.z+1:
            i.vel.z=-i.vel.z
            i.color=vector(r.random(),r.random(),r.random())
        elif abs(i.pos.y)>=wallUp.pos.y-1:
            i.vel.y=-i.vel.y
            i.color=vector(r.random(),r.random(),r.random())
        elif i.pos.z>=2.5:
            i.vel.z=-i.vel.z
            i.color=vector(r.random(),r.random(),r.random())
    t=t+dt