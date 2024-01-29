import random 
import numpy as np
import matplotlib.pyplot as plt
def sigmoid_f(a,x_d,b):
    return 1 / (1 + np.exp(a * x_d + b))

def cost_f(a,b,x_d,y_d):
    y=sigmoid_f(a,x_d,b)
    return -np.mean(y_d * np.log(y) + (1 - y_d) * np.log(1 - y))
#이건 a찾는거
def partial_dif(a,b,x_d,y_d,delta):
    y = cost_f(a, b, x_d, y_d)
    y_delta = cost_f((a + delta), b, x_d, y_d)
    gradient_a = (y_delta - y) / delta
    return gradient_a


x_data = np.array([2, 4, 6, 8, 10, 12, 14])
y_data = np.array([0, 0, 0, 1, 1, 1, 1])
learning_rate = 0.03
delta=0.001
tol = 0.00000005

a_i = np.random.rand(1)
b_i = 32
c_y = cost_f(a_i,b_i,x_data,y_data)
i_ter=0



while(True):
    grad_a=partial_dif(a_i,b_i,x_data,y_data, delta)
    a_n=a_i+(-grad_a*learning_rate)
    n_y=cost_f(a_n,b_i,x_data,y_data)
    i_ter += 1
    if( abs(c_y-n_y) <= tol):
        print('a*=',a_n)
        break
    a_i=a_n
    c_y=n_y
    #print('i_ter',i_ter, 'a=',a_i)
    

x_test=np.linspace(min(x_data),max(x_data),40)
y_test = 1/(1+np.exp(a_i*x_test+b_i))
plt.figure(1)
plt.plot(x_data,y_data,'ok',x_test,y_test,'r--')
plt.xlabel('x')
plt.ylabel('y')
plt.show()