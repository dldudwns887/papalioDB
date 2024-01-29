'''
100번중 56번을 던졌을때 이항 분포 확률을 구하고 거기서 likelihood_f을 구한다. (최대가능우도)

'''


import numpy as np
import math
from matplotlib import pyplot as plt


def nCk(n,k,p):
    
    likehood= math.factorial(n)/(math.factorial(k)*math.factorial(n-k)) * p**k*(1-p)**(n-k)
    
    return likehood


p=np.linspace(0.4,0.8,50)
n=100
k=56

likehood_f=[ nCk(n,k,p_) for p_ in p]

plt.plot(p,likehood_f,'b-')
plt.show()


