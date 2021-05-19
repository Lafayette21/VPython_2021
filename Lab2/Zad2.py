import random as rnd
import math

def MonteCarloPi(n):
    N_okrag=0
    N_kwadrat=0
    while N_kwadrat<n:
        x=rnd.random()
        y=rnd.random()
        if x*x+y*y<=1:
            N_okrag+=1
        N_kwadrat+=1
    return 4*N_okrag/N_kwadrat


f=open('wyniki2.txt','w')
licznik=0;
for i in range(1,101):
    pi=MonteCarloPi(i)
    stosunek=pi/math.pi
    f.write(str(i)+') '+str(pi)+'   '+str(stosunek)+'\n')
    if math.fabs(1-stosunek)<0.05 and licznik!=1:
        print('Wystarczy '+str(i)+' strzalow')
        licznik+=1;
        
for x in range(3,7):
    pi=MonteCarloPi(10**x)
    stosunek=pi/math.pi
    f.write('10**'+str(x)+') '+str(pi)+'    '+str(stosunek)+'\n')

f.close()
 

               
