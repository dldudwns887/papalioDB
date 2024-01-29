import numpy as np
import math
from matplotlib import pyplot as plt


p=np.linspace(0.4,0.8,50)


try_count = 100
front_count=56
nCk_result = lambda p : math.factorial(try_count)/(math.factorial(front_count)*math.factorial(try_count-front_count))*p**front_count*(1-p)**(try_count-front_count)
likehood_f = [nCk_result(p_) for p_ in p]

print(likehood_f.index(max(likehood_f)))

try_count2 = 50
front_count2=30
nCk_result2 = lambda p : math.factorial(try_count2)/(math.factorial(front_count2)*math.factorial(try_count2-front_count2))*p**front_count2*(1-p)**(try_count2-front_count2)
likehood_f2 = [nCk_result2(p_) for p_ in p]
print(likehood_f2.index(max(likehood_f2)))



combined_likelihood = np.array(likehood_f) * np.array(likehood_f2)


max_likelihood_index = np.argmax(combined_likelihood)
max_p = p[max_likelihood_index]

print(f"probability {max_p:.4f}")
print("index",max_likelihood_index)

'''
100번 던졌을때 56번 앞면 나올 확률 20번째에서 최대로함

50번 던졌을때 30번 앞면 나올 확률 24번째에서 최대로함 

이 2개를 통해 앞면이 나올 확률을 구해야함

'''

