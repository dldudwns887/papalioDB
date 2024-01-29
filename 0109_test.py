a = int(input())


dp = [[0,0] for _ in range(41) ]
dp[0][1] = 0
dp[0][0] = 1
dp[1][1] = 1
dp[1][0] = 0

for i in range(2,41):
    dp[i][0] = dp[i-1][0] + dp[i-2][0] 
    dp[i][1] = dp[i-1][1] + dp[i-2][1]
    
    
n_list = []

for _ in range(a):
    n_list.append(int(input()))
    
for n in n_list:
    print(dp[n][0], end = ' ')
    print(dp[n][1])