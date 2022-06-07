weights = [0,2,1,4,3]
values  = [0,3,6,4,1]
W = 8+1
N = 4+1
dp = [[0]*(W) for _ in range(N)]
for w in range(1,W):
    for n in range(1,N):
        if weights[n] <= w:
            dp[n][w] = max(dp[n-1][w], dp[n-1][w-weights[n]]+values[n])
        else:
            dp[n][w] = dp[n-1][w]
print(dp[-1][-1])
        