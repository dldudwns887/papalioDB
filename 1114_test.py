import numpy as np
import math
from matplotlib import pyplot as plt

x=np.linspace(0,4,15)
sigma=1
error = np.random.normal(0,sigma,len(x))
y = 1 + 2*x + error


gauss = lambda x, m : 1/(2*math.pi)**0.5*math.exp(-(x-m)**2/2)
a = np.linspace(0,3,10)
hood = []
for i in range(len(a)):
    a_h = a[i]
    hood_f=0
    for j in range(len(x)):
        x_data=x[j]
        m = 1+a_h*x_data
        hood_f+=math.log10(gauss(y[j],m))
    hood.append(hood_f)
    
    
max_a = a[hood.index(max(hood))]


y_h=1+max_a*x


plt.figure(1)
plt.plot(a,hood,'b-')
plt.xlabel('a')
plt.ylabel('ML_f')



plt.figure(2)
plt.plot(x, y, 'b.', label='real data')
plt.plot(x, y_h, 'r-', label='estimation')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()


