import matplotlib.pyplot as plt
import numpy as np
import random 

def dif(x,delta):
    y_delta=func_(x+delta)
    y=func_(x)
    gradient = (y_delta-y)/(delta)
    return gradient


def func_(x):
    return x**2+x


learning_rate = 0.001
delta=0.000001
eps=0.000001

x_i=random.random() 
y_i=func_(x_i)

i_ter = 0

while(True):
    g_d=dif(x_i,delta) #기울기계산
    x_n=x_i+(-g_d*learning_rate) #반대방향으로 x의 새로운 값 업데이트
    y_n=func_(x_n) # 새로운 x값의 함수 값
    i_ter+=1 #반복횟수
    if(abs(x_n-x_i) <= eps):
        print('x*=',x_n,', min of f(x)=',y_n)
        break
    x_i=x_n
    y_i=y_n
    if(i_ter%100)==0:
        print('i_ter : ',i_ter, 'x=',x_n,'f(x)=',y_n)



'''
x = np.linspace(-10,10,40)
y=[]
y_m=[]
delta=0.000001

y_m=dif(x,delta)
y=func_(x)

plt.figure(1)
plt.plot(x,y,label='x^2+1')
plt.plot(x,y_m,label="2x+1")

plt.xlabel('x axis')
plt.ylabel('y axis')

plt.legend(loc = 'upper right')
plt.grid()
plt.show()
'''