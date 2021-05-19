from vpython import *

scene=canvas()

MS=2*(10**30)
G=6.67*(10**(-11))
#predkosci poczatkowe
VMEp=vector(0,47,0)*(10**3)
VWp=vector(0,35,0)*(10**3)
VEp=vector(0,30,0)*(10**3)
VMAp=vector(0,24,0)*(10**3)

dt=3600


Sun=sphere(pos=vector(0,0,0),radius=10*(10**9), color=color.yellow)
Mercury=sphere(pos=vector(70,0,0)*(10**9),radius=2*(10**9), color=color.magenta, make_trail=True)
Wenus=sphere(pos=vector(110,0,0)*(10**9),radius=2.5*(10**9), color=color.cyan, make_trail=True)
Earth=sphere(pos=vector(150,0,0)*(10**9),radius=3*(10**9),color=color.blue, make_trail=True)
Mars=sphere(pos=vector(250,0,0)*(10**9),radius=3*(10**9),color=color.red, make_trail=True)

t=0

for i in range(10000):
#Mercury
    rate(100)
    RMEp=Mercury.pos
    a=-((G*MS)/(mag(RMEp)**3))*RMEp
    VMEn=VMEp+a*dt
    Mercury.pos=RMEp+VMEn*dt
    VMEp=VMEn
#Wenus
    RW=Wenus.pos
    a=-((G*MS)/(mag(RW)**3))*RW
    VWn=VWp+a*dt
    Wenus.pos=RW+VWn*dt
    VWp=VWn
#Earth
    RE=Earth.pos
    a=-((G*MS)/(mag(RE)**3))*RE
    VEn=VEp+a*dt
    Earth.pos=RE+VEn*dt
    VEp=VEn
#Mars
    RMA=Mars.pos
    a=-((G*MS)/(mag(RMA)**3))*RMA
    VMAn=VMAp+a*dt
    Mars.pos=RMA+VMAn*dt
    VMAp=VMAn

