# 주어진 코드를 수정하여 a와 b 모두를 업데이트 하는 경사 하강법 구현

import numpy as np
import matplotlib.pyplot as plt
import random

# 주어진 선형 함수
def func_(a, b, x):
    return b + a * x

# 평균 제곱근 오차(RMSE) 계산 함수
def RMSE(a, b, x, y):
    return np.sqrt(np.mean((y - func_(a, b, x))**2))
    return 
# a에 대한 RMSE 그래디언트 계산 함수
def grad_a(a, b, x, y, delta):
    y_delta = RMSE(a + delta, b, x, y)
    y = RMSE(a, b, x, y)
    gradient = (y_delta - y) / delta
    return gradient

# b에 대한 RMSE 그래디언트 계산 함수
def grad_b(a, b, x, y, delta):
    y_delta = RMSE(a, b + delta, x, y)
    y = RMSE(a, b, x, y)
    gradient = (y_delta - y) / delta
    return gradient

# 데이터 생성
x = np.linspace(0, 4, 15)
sigma = 1
error = np.random.normal(0, sigma, len(x))
y = 1 + 2 * x + error

# 초기 파라미터 a와 b 설정
a = random.random()
b = random.random()

# 학습률, 변화량, 수렴 조건
learning_rate = 0.001
delta = 0.0001
eps = 0.00001
iter_count = 0

# 경사 하강법 실행
while True:
    # 기울기 계산
    g_d_a = grad_a(a, b, x, y, delta)
    g_d_b = grad_b(a, b, x, y, delta)
    
    # 파라미터 업데이트
    a_new = a + (-g_d_a * learning_rate)
    b_new = b + (-g_d_b * learning_rate)
    
    # RMSE 계산
    rmse_new = RMSE(a_new, b_new, x, y)
    
    # 수렴 조건 확인
    if abs(a_new - a) <= eps and abs(b_new - b) <= eps:
        print(f'Convergence after {iter_count} iterations:')
        print(f'a* = {a_new}, b* = {b_new}, min of RMSE = {rmse_new}')
        break
    
    # 값 업데이트
    a, b = a_new, b_new
    
    # 반복 횟수 증가
    iter_count += 1
    if iter_count % 100 == 0:
        print(f'iter: {iter_count}, a = {a_new}, b = {b_new}, RMSE = {rmse_new}')

# 최종 결과 그래프로 표시
plt.scatter(x, y, label='Real Data', color='blue')
plt.plot(x, func_(a, b, x), label='Estimated Regression Line', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
