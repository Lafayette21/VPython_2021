import numpy as np
import math

def silnia(n):
    if n==int(n):
        if n==0 or n==1:
            return 1
        else:
            return n*silnia(n-1)
    else:
        if n==0.5:
            return math.pi/2
        else:
            return (n/2)*silnia(n-1)


