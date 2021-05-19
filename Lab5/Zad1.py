import numpy as np
import random as r

N=1000

f=open('Wyniki1.txt','w')
pr=[]
k=0

for n in range(1,367):
    suma=0
    a=[[r.randint(0,365) for i in range(n)] for j in range(N)]
    for room in a:
        if any(room.count(el)>1 for el in room):
            suma+=1
        pr.append(suma/N)
    f.write(str(n)+') '+str(suma/N)+'\n')



#print(pr)
f.close()
