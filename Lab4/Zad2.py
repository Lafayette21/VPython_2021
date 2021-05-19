import Zad1 as z1
import numpy as np
import math


def MonteCarlo(n,wymiar):
    N_O=0
    N_K=0
    while N_K<n:
        a=np.array(np.random.random(wymiar))
        if np.sum(a**2)<=1:
            N_O+=1
        N_K+=1
    return N_O

def Objetosc(N):
    return ((math.pi)**(N/2))/z1.silnia(N/2)

#main
n=10**6
f=open('wyniki.txt','w')
for i in range(2,19):
    pomoc=MonteCarlo(n,i)
    wyliczona=(2**i)*(pomoc/n)
    real=Objetosc(i);
    f.write(str(i)+')  '+str(wyliczona)+'  '+str(real)+'  '+str(wyliczona/real)+'  '+str(pomoc)+'\n')
    
f.close()        
        
        
