from vpython import *

scene=canvas()

MS=2*(10**30)
G=6.67*(10**(-11))
MZ=6*(10**24)
#predkosci poczatkowe
VSp=vector(0,20,0)*(10**3)
VMEp=vector(0,47,0)*(10**3)
VWp=vector(0,35,0)*(10**3)
VMAp=vector(0,24,0)*(10**3)

dt=3600

Sun=sphere(pos=vector(0,0,0),radius=10*(10**9), color=color.yellow, make_trail=True)
Mercury=sphere(pos=vector(70,0,0)*(10**9),radius=2*(10**9), color=color.magenta, make_trail=True)
Wenus=sphere(pos=vector(110,0,0)*(10**9),radius=2.5*(10**9), color=color.cyan, make_trail=True)
Earth=sphere(pos=vector(150,0,0)*(10**9),radius=3*(10**9),color=color.blue)
Mars=sphere(pos=vector(250,0,0)*(10**9),radius=3*(10**9),color=color.red, make_trail=True)


for i in range(10000):
    rate(100)
#Slonce Masa ziemi przyjeta jako masa slonca (przy rzeczywistej byla za slaba sila)
    RS=Sun.pos
    a=-(G*MS/(mag(RS-Earth.pos)**3))*(RS-Earth.pos)
    VSn=VSp+a*dt
    Sun.pos=RS+VSn*dt
    VSp=VSn
#Mercury 
    RMEp=Mercury.pos
    a=-((G*MS)/(mag(RMEp-RS)**3))*(RMEp-RS)
    VMEn=VMEp+a*dt
    Mercury.pos=RMEp+VMEn*dt
    VMEp=VMEn
#Wenus
    RW=Wenus.pos
    a=-((G*MS)/(mag(RW-RS)**3))*(RW-RS)
    VWn=VWp+a*dt
    Wenus.pos=RW+VWn*dt
    VWp=VWn
#Mars
    RMA=Mars.pos
    a=-((G*MS)/(mag(RMA-RS)**3))*(RMA-RS)
    VMAn=VMAp+a*dt
    Mars.pos=RMA+VMAn*dt
    VMAp=VMAn
