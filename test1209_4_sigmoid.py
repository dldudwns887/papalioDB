import numpy as np
from matplotlib import pyplot as plt
import random
import math


def sigmoid(a,x):
    
    return 1/(1+np.exp(a*x+32))

def cost(a,x_data,y_data):
    y=sigmoid(a,x_data)
    z= (-np.mean(y_data*np.log(y)+(1-y)*np.log(1-y)))
    return z

def difference_f(a,x_data,y_data,delta):
    y = cost(a,x_data,y_data)
    y_delta = cost((a+delta),x_data,y_data)
    return (y_delta-y)/delta

delta = 0.001
learning_rate = 0.3
tol = 0.00000005 # 이 값보다 작아져야 최적화



x_data = np.array([2,4,6,8,10,12,14])
y_data = np.array([0,0,0,1,1,1,1])
a_i = np.random.rand(1)

c_y=cost(a_i,x_data,y_data)
count = 0
while(True):
    grad_a = difference_f(a_i,x_data,y_data,delta)
    a_n = a_i + (-grad_a * learning_rate)
    n_y = cost(a_n,x_data,y_data)
    count+=1
    if(abs(c_y - n_y) <= tol):
        print('a = ', a_n)
        break
    a_i = a_n
    c_y = n_y
    
    if(count % 10 == 0):
        
        print("count : ",count , "a =", a_n)