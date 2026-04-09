def knapsack(wt,v,w):
    n = len(wt)
    dp = [[0 for _ in range(w+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for w in range(1, w+1):
            if wt[i-1] <= w:
                dp[i][w] = max(
                    v[i-1] + dp[i-1][w - wt[i-1]],
                    dp[i-1][w]
                )
            else:
                dp[i][w] = dp[i-1][w]
    
    return dp[n][w]

wt = [1, 3, 4, 5]
v= [10, 40, 50, 70]
c= 8

print(knapsack(wt,v,c)) 