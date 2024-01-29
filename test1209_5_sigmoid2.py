# 로지스틱 회귀 모델을 위한 경사 하강법을 구현하는 코드입니다.

# 필요한 라이브러리를 가져옵니다.
import numpy as np
from matplotlib import pyplot as plt
import random

# 시그모이드 함수를 정의합니다.
def sigmoid(a, b, x):
    return 1 / (1 + np.exp(-(a*x + b)))

# 비용 함수를 정의합니다.
def cost(a, b, x_data, y_data):
    y = sigmoid(a, b, x_data)
    return -np.mean(y_data*np.log(y) + (1 - y_data)*np.log(1 - y))

# 미분 함수를 정의합니다.
def difference_f(a, b, x_data, y_data, delta):
    cost_initial = cost(a, b, x_data, y_data)
    cost_a_delta = cost(a + delta, b, x_data, y_data)
    cost_b_delta = cost(a, b + delta, x_data, y_data)
    gradient_a = (cost_a_delta - cost_initial) / delta
    gradient_b = (cost_b_delta - cost_initial) / delta
    return gradient_a, gradient_b

# 학습률, 변화량, 수렴 기준을 정의합니다.
delta = 0.001
learning_rate = 0.1
tol = 0.00000005

# 데이터를 정의합니다.
x_data = np.array([2, 4, 6, 8, 10, 12, 14])
y_data = np.array([0, 0, 0, 1, 1, 1, 1])

# a와 b를 무작위 값으로 초기화합니다.
a_i = np.random.rand(1)
b_i = np.random.rand(1)

# 비용을 계산합니다.
c_y = cost(a_i, b_i, x_data, y_data)

# 카운터 변수를 초기화합니다.
count = 0

# 경사 하강법을 사용하여 a와 b를 최적화합니다.
while True:
    grad_a, grad_b = difference_f(a_i, b_i, x_data, y_data, delta)
    a_n = a_i - (grad_a * learning_rate)
    b_n = b_i - (grad_b * learning_rate)
    n_y = cost(a_n, b_n, x_data, y_data)
    count += 1
    if abs(c_y - n_y) <= tol:
        print(f'Converged after {count} iterations: a = {a_n}, b = {b_n}')
        break
    a_i, b_i = a_n, b_n
    c_y = n_y
    
    if count % 10 == 0:
        print(f'Iteration {count}: a = {a_n}, b = {b_n}, cost = {n_y}')

# 시그모이드 함수를 사용하여 예측값을 계산하고 플롯합니다.
x_test = np.linspace(min(x_data), max(x_data), 300)
y_test = sigmoid(a_n, b_n, x_test)

plt.plot(x_data, y_data, "b.",label="real data")
plt.plot(x_test, y_test, label='Sigmoid Function', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Logistic Regression Fit')
plt.show()
