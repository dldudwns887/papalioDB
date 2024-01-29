import numpy as np
from matplotlib import pyplot as plt
import math

x=np.linspace(0,4,15)
sigma=1
error = np.random.normal(0,sigma,len(x))
y=2+3*x+error


def cov(x_,y_):
    s=0
    for i in range(len(x_)):
        s += x_[i]*y_[i]
    return (s/len(x_))-((mean(x_)*mean(y_)))

def mean(x_):
    s=0
    
    for i in x_:
        s += i
    return s/len(x_)

def var(x_):
    s=0
    m = mean(x_)
    for i in x_:
        s+=(i-m)**2
    return s/len(x)

'''
1번 문제 
y=2+ax  베타0 2 베타1 a
2번 문제
y=b+3*x 베타0 b 베타 1 3

'''
beta0_1 = 2
beta1_2 = 3

beta1_1 = cov(x,y)/var(x)
beta0_2 = mean(y)-beta0_1*mean(x)

y_h_1 = beta1_1 + beta0_1*x
y_h_2 = beta1_2 + beta0_2*x

plt.figure(1)
plt.plot(x,y,'b.',label = 'real data')
plt.plot(x,y_h_1,'r-',label='estimation')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.figure(2)
plt.plot(x,y,'b.',label = 'real data')
plt.plot(x,y_h_2,'r-',label='estimation')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()