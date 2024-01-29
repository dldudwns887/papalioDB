import math
from matplotlib import pyplot as plt
import numpy as np
import random

def dif(x,delta):
    y_delta = func_(x+delta)
    grad = (y_delta-func_(x))/delta
    return grad


def func_(x):
    
    return x**2+x

learning_rate = 0.001
delta=0.000001
eps=0.000001

x_i=random.random() 
y_i=func_(x_i)

i_ter = 0


while(True):
    
    #기울기 구하기 (초기값, 델타값)
    g_d=dif(x_i,delta)
    #반댓방향 x 값 업데이트(초기 값 +  (-기울기 * learning_rate))
    x_n=x_i + (-g_d * learning_rate)
    #반댓방향 x에 대한 y 값 구하기
    y_n = func_(x_n)
    i_ter +=1
    if(abs(x_i-x_n) < eps):
        print(x_n,y_n)
        break
    x_i = x_n
    y_i = y_n
    if(i_ter%100)==0:
        print('i_ter : ',i_ter, 'x=',x_n,'f(x)=',y_n)
        
