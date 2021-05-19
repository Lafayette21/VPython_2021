import random
import time
lewo=10
prawo=10
i=0
licznik=0

print(' '*(lewo-1)+'Start'+' '*(prawo-1))
print('|'+' '*lewo+'*'+' '*prawo+'|'+str(i))
while True:
    time.sleep(0.06)
    x=random.randrange(-1,2,2)
    licznik+=1
    if int(x)==1:
        prawo-=1
        lewo+=1
        i+=1
    else:
        prawo+=1
        lewo-=1
        i-=1
    if i<0:
        print('|'+' '*lewo+'*'+' '*prawo+'|'+str(i))
    else:
        print('|'+' '*lewo+'*'+' '*prawo+'|+'+str(i))
    if lewo==0 or prawo==0:
        break
print('Rzucilismy '+str(licznik)+' razy')



