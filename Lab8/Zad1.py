from vpython import *
import random as r

scene=canvas(width=550,height=580)

ball = sphere(pos=vector(0,0,0),radius=0.8, color=color.red)

p=1

wallR=box(pos=vector(3.8,0,0), size=vector(p,7,7), color=color.blue)
wallL=box(pos=vector(-3.8,0,0),size=vector(p,7,7), color=color.green)
wallUp=box(pos=vector(0,3.5,0),size=vector(p,7,7), color=color.orange)
wallBot=box(pos=vector(0,-3.5,0),size=vector(p,7,7), color=color.red)
wallBack=box(pos=vector(0,0,-3.5),size=vector(p,7,7), color=color.cyan)

wallUp.rotate(angle=radians(90),axis=vector(0,0,1))
wallBot.rotate(angle=radians(90),axis=vector(0,0,1))
wallBack.rotate(angle=radians(90),axis=vector(0,1,0))


ball.vel=vector(r.random(),r.random(),r.random())
print(ball.vel.x,ball.vel.y,ball.vel.z)


t=0
dt=0.005


while t<100:
    rate(1000)
    ball.pos=ball.pos+ball.vel*dt
    if abs(ball.pos.x)>=wallR.pos.x-p*1.3:
        ball.vel.x=-ball.vel.x
        ball.color=vector(r.random(),r.random(),r.random())
    elif ball.pos.z<=wallBack.pos.z+p*1.3:
        ball.vel.z=-ball.vel.z
        ball.color=vector(r.random(),r.random(),r.random())
    elif abs(ball.pos.y)>=wallUp.pos.y-p*1.3:
        ball.vel.y=-ball.vel.y
        ball.color=vector(r.random(),r.random(),r.random())
    elif ball.pos.z>=3.5-p*1.3:
        ball.vel.z=-ball.vel.z
        ball.color=vector(r.random(),r.random(),r.random())
    t=t+dt
