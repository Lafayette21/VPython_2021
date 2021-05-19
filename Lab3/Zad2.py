import math
#podpunkt 1

L=[x*2*math.pi/50 for x in range(51)]

#print(list(L))

#Popunkt2

def fun(x):
    return 50k,*math.sin(x)


W=[int(fun(i)) for i in L]

#print(W)

#Podpunkt3
f=open('zad1.txt','w')
for i in W:
    if i==0:
        f.write('0')
    elif i<0:
        f.write('-'*abs(i))
    else:
        f.write('+'*i)
    f.write('\n')
        
        
f.close()




