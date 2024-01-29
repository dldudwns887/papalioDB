import random
import matplotlib.pyplot as plt
total = 10000
n = 5
rand_v = []
for i in range(total):
    s=0
    for j in range(n):
        s+=random.randint(1,n)
    rand_v.append(s)
    
#pmf
max_val = n*5
pmf = [rand_v.count(i)/total for i in range(n, max_val+1)]    

plt.bar(range(n, max_val+1), pmf)
plt.xlabel('수 합친거')
plt.ylabel('확률')
plt.title('pmf')
plt.show()
