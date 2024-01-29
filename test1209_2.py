import math
import random
from matplotlib import pyplot as plt
import numpy as np


def grad(a,x,delta,y):
    y_delta = RMSE(a+delta,x,y)
    y = RMSE(a,x,y)
    gradient = (y_delta - y) / delta
    return gradient

def mean(x):
    
    return sum(x)/len(x)

def RMSE(a,x,y):
    return (mean((y-func_(a,x))**2))**0.5
    
    

def func_(a,x):
    return 1+a*x



x=np.linspace(0,4,15)
sigma=1
error=np.random.normal(0,sigma,len(x))
y=1+2*x+error
a=random.random()
learning_rate = 0.001
delta=0.000001
eps=0.000001
i_ter = 0

while(True):
    #기울기 구하기 
    g_d = grad(a,x,delta,y)
    #새로운 a값 업데이트
    a_n = a+(-g_d*learning_rate)
    rmse = RMSE(a_n,x,y)
    i_ter +=1
    #eps 비교
    if(abs(a_n-a) <= eps):
        print("a*=",a_n, ", min of rmse = ", rmse)
        break
    a = a_n
    if(i_ter % 100) == 0 :
        print("i_ter :",i_ter, 'a=',a_n,'rmse = ',rmse)
    
    
    