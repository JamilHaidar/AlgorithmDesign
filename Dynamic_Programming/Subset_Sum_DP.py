#Goal: determine if there is a subset of the given set with sum equal to given sum
values = [2,5,4,10,7]
sum = 6
n = len(values)
dp = [[False for _ in range(sum+1)] for _ in range(n+1)]
for i in range(n+1):
    dp[i][0] = True
for i in range(1,n+1):
    for j in range(1,sum+1):
        if j<values[i-1]:
            dp[i][j] = dp[i-1][j]
        elif j>=values[i-1]:
            dp[i][j] = dp[i-1][j] or dp[i-1][j-values[i-1]]
print(dp[n][sum])