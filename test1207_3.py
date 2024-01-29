# 주어진 문제에 맞게 코드를 수정합니다.
import numpy as np
import math
from matplotlib import pyplot as plt
# 데이터 생성
x = np.linspace(0, 4, 15)
sigma = 1
error = np.random.normal(0, sigma, len(x))
y = 1 + 2 * x + error

# 정규 분포 확률 밀도 함수
def gauss(y, m):
    return 1 / (np.sqrt(2 * math.pi) * sigma) * np.exp(-((y - m) ** 2) / (2 * sigma ** 2))

# 가능한 a와 b 값들의 범위를 설정
a_values = np.linspace(0, 4, 10)
b_values = np.linspace(0, 4, 10)

# 최대 우도를 저장할 변수와 a, b 값을 저장할 변수 초기화
max_likelihood = -np.inf
best_a = None
best_b = None

# 가능한 a, b 값들에 대해 우도 계산
for a_h in a_values:
    for b_h in b_values:
        likelihood_f = 0
        # 각 데이터 포인트에 대한 우도 계산
        for x_val, y_val in zip(x, y):
            m = b_h + a_h * x_val
            likelihood_f += math.log10(gauss(y_val, m))
        # 최대 우도 업데이트
        if likelihood_f > max_likelihood:
            max_likelihood = likelihood_f
            best_a = a_h
            best_b = b_h

# 최대 우도를 가지는 a, b를 사용하여 회귀선을 구합니다.
y_h = best_b + best_a * x

# 결과를 출력합니다.
print(f"a: {best_a}")
print(f"b: {best_b}")

# 그래프를 그립니다.
plt.figure(figsize=(10, 5))
plt.scatter(x, y, label='real data')
plt.plot(x, y_h, 'r-', label=f'회귀선 (y={best_b:.2f} + {best_a:.2f}*x)')
plt.title('test')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
