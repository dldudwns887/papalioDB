import numpy as np
import math
from matplotlib import pyplot as plt

x = np.linspace(0,4,30)
sigma = 1
error = np.random.normal(0,sigma,len(x))
y = 2 + 3*x + error

def cov(x_,y_):
    s=0
    for i in range(len(x_)):
        s+=x_[i]*y_[i]
    return (s/len(x_))-(mean(x_)*mean(y_))

def mean(x_):
    s=0
    for i in x_:
        s+=i
    return s/len(x_)
    return 

def var(x_):
    s=0
    m=mean(x_)
    for i in x_:
        s+=(i-m)**2
    return s/len(x_)

beta1 = cov(x,y)/var(x)
beta0 = mean(y)-beta1*mean(x)
print(beta1,beta0)

y_h = beta0+beta1*x


plt.figure(1)
plt.plot(x, y, 'b.', label='real data')
plt.plot(x, y_h, 'r-', label='estimation')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
