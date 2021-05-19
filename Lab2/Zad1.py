import math

def Leibnitz(n):
    suma=0;
    for i in range(0,n):
        pomoc=1/(2*i+1)
        if i%2==0:
            suma+=pomoc
        else:
            suma-=pomoc;
    return 4*suma;

f=open('wyniki1.txt','w')
for i in range(1,101):
    pi=Leibnitz(i)
    stosunek=pi/math.pi
    f.write(str(i)+') '+str(pi)+'   '+str(stosunek)+'\n')

for i in range(3,8):
    pi=Leibnitz(10**i)
    stosunek=pi/math.pi
    f.write('10**'+str(i)+') '+str(pi)+'   '+str(stosunek)+'\n')


f.close()
